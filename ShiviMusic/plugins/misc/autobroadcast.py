# 👑 Owner : Rich Yui
# ===========================================================
# Auto Broadcast : photo + message har X ghante me sab served chats me
# Sirf SUDO users use kar sakte hain.
#
#   /setautobc   (photo/text par reply karke)  -> broadcast message set
#   /autobc on | off                            -> chalu / band
#   /autobc time <ghante>                       -> interval (min 1 ghanta)
#   /autobc users on | off                      -> users ko bhi bhejna
#   /autobc button on | off                     -> "Add me in your group" button
#   /autobc status                              -> current settings
#   /autobc test                                -> abhi turant bhejo (sirf yaha)
# ===========================================================

import asyncio
import time

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ShiviMusic import app
from ShiviMusic.core.mongo import mongodb
from ShiviMusic.misc import SUDOERS
from ShiviMusic.utils.database import get_served_chats, get_served_users

db = mongodb.autobroadcast
DEFAULT = {
    "_id": "cfg",
    "enabled": False,
    "interval": 6 * 3600,
    "photo": None,
    "text": None,
    "users": False,
    "button": True,
    "last": 0,
}


async def get_cfg() -> dict:
    data = await db.find_one({"_id": "cfg"})
    cfg = dict(DEFAULT)
    if data:
        cfg.update(data)
    return cfg


async def set_cfg(**kwargs):
    await db.update_one({"_id": "cfg"}, {"$set": kwargs}, upsert=True)


def build_markup(cfg):
    if not cfg["button"]:
        return None
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "➕ add me in your group ➕",
                    url=f"https://t.me/{app.username}?startgroup=true",
                )
            ]
        ]
    )


async def send_one(chat_id: int, cfg: dict) -> bool:
    markup = build_markup(cfg)
    try:
        if cfg["photo"]:
            await app.send_photo(
                chat_id, cfg["photo"], caption=cfg["text"] or "", reply_markup=markup
            )
        else:
            await app.send_message(
                chat_id,
                cfg["text"],
                reply_markup=markup,
                disable_web_page_preview=True,
            )
        return True
    except FloodWait as fw:
        if fw.value > 200:
            return False
        await asyncio.sleep(fw.value)
        return await send_one(chat_id, cfg)
    except Exception:
        return False


async def run_broadcast(cfg: dict):
    sent = 0
    for chat in await get_served_chats():
        if await send_one(int(chat["chat_id"]), cfg):
            sent += 1
        await asyncio.sleep(0.3)
    users_sent = 0
    if cfg["users"]:
        for user in await get_served_users():
            if await send_one(int(user["user_id"]), cfg):
                users_sent += 1
            await asyncio.sleep(0.3)
    await set_cfg(last=int(time.time()))
    return sent, users_sent


async def auto_loop():
    await asyncio.sleep(60)
    while True:
        try:
            cfg = await get_cfg()
            if cfg["enabled"] and (cfg["photo"] or cfg["text"]):
                if time.time() - cfg["last"] >= cfg["interval"]:
                    await run_broadcast(cfg)
        except Exception:
            pass
        await asyncio.sleep(60)


@app.on_message(filters.command("setautobc") & SUDOERS)
async def set_autobc(client, message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply_text(
            "Photo ya message par reply karke <code>/setautobc</code> bhejo.\n"
            "Caption/text reply wale message se hi liya jayega.",
        )
    photo = reply.photo.file_id if reply.photo else None
    body = reply.caption or reply.text
    text = body.html if body else None
    if not photo and not text:
        return await message.reply_text("Photo ya text wala message chahiye.")
    await set_cfg(photo=photo, text=text)
    await message.reply_text(
        "✅ Auto broadcast message set ho gaya.\n"
        "Check karne ke liye <code>/autobc test</code>, chalu karne ke liye <code>/autobc on</code>."
    )


@app.on_message(filters.command("autobc") & SUDOERS)
async def autobc_cmd(client, message):
    args = message.command[1:]
    cfg = await get_cfg()
    if not args or args[0] == "status":
        hrs = cfg["interval"] / 3600
        yes, no = "haan", "nahi"
        state = "ON ✅" if cfg["enabled"] else "OFF ❌"
        has_photo = yes if cfg["photo"] else no
        has_text = yes if cfg["text"] else no
        has_users = yes if cfg["users"] else no
        has_button = yes if cfg["button"] else no
        return await message.reply_text(
            "<b>Auto Broadcast</b>\n"
            f"Status : {state}\n"
            f"Interval : {hrs:g} ghante\n"
            f"Photo : {has_photo}\n"
            f"Message : {has_text}\n"
            f"Users ko bhi : {has_users}\n"
            f"Button : {has_button}"
        )
    cmd = args[0].lower()
    if cmd in ("on", "off"):
        if cmd == "on" and not (cfg["photo"] or cfg["text"]):
            return await message.reply_text("Pehle <code>/setautobc</code> se message set karo.")
        await set_cfg(enabled=(cmd == "on"), last=int(time.time()) if cmd == "on" else cfg["last"])
        return await message.reply_text(f"Auto broadcast {cmd.upper()} ✅")
    if cmd == "time" and len(args) > 1:
        try:
            hrs = float(args[1])
        except ValueError:
            return await message.reply_text("Ghante number me do. Example: <code>/autobc time 6</code>")
        if hrs < 1:
            return await message.reply_text("Minimum 1 ghanta rakho (flood se bachne ke liye).")
        await set_cfg(interval=int(hrs * 3600))
        return await message.reply_text(f"Interval {hrs:g} ghante set ✅")
    if cmd in ("users", "button") and len(args) > 1 and args[1].lower() in ("on", "off"):
        await set_cfg(**{cmd: args[1].lower() == "on"})
        return await message.reply_text(f"{cmd} {args[1].upper()} ✅")
    if cmd == "test":
        if not (cfg["photo"] or cfg["text"]):
            return await message.reply_text("Pehle <code>/setautobc</code> se message set karo.")
        ok = await send_one(message.chat.id, cfg)
        return await message.reply_text("Test bhej diya ✅" if ok else "Test fail ❌")
    await message.reply_text(
        "<code>/autobc on|off|status|test</code>\n"
        "<code>/autobc time 6</code>\n"
        "<code>/autobc users on|off</code>\n"
        "<code>/autobc button on|off</code>"
    )


asyncio.create_task(auto_loop())
