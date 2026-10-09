# 👑 Owner : Rich Yui
# ===========================================================
# 🎆 Har bot command par reaction animation
# Koi bhi /command (start, play, ping, help ...) bheje to bot uske message
# par big reaction lagata hai. Har chat me 3 sec ka throttle (flood se bachne ke liye).
# ===========================================================

import asyncio
import re
import time

from pyrogram import filters

from ShiviMusic import app
from ShiviMusic.utils.reactions import react_on
from config import BANNED_USERS

_CMD = re.compile(r"^[/!.]([A-Za-z0-9_]+)(?:@(\w+))?")
_last: dict[int, float] = {}
_THROTTLE = 3.0


def _is_my_command(_, __, message) -> bool:
    text = message.text or ""
    m = _CMD.match(text)
    if not m or not message.from_user or message.from_user.is_bot:
        return False
    target = m.group(2)
    if target and target.lower() != (getattr(app, "username", "") or "").lower():
        return False  # kisi aur bot ka command
    return True


my_command = filters.create(_is_my_command)


async def _react(message):
    await react_on(message)


@app.on_message(my_command & ~BANNED_USERS, group=-10)
async def react_to_commands(client, message):
    now = time.time()
    if now - _last.get(message.chat.id, 0) < _THROTTLE:
        return
    _last[message.chat.id] = now
    asyncio.create_task(_react(message))  # background: command handler ko block nahi karta
