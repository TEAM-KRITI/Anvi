# 👑 Owner : Rich Yui
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ShiviMusic import app
from config import BOT_USERNAME

start_txt = """**
<u> Welcome to team kriri repos </u>
 
 Repo is now private dude 😌
 
  You can my use public repos !! 

 || [Kirti x bots 💞](https://t.me/annu_support) ||
 
 Run 24x7 lag free without stop

 Owner : Rich Yui**
"""


@app.on_message(filters.command("repo"))
async def repo_command(_, msg):
    buttons = [
        [
            InlineKeyboardButton("✙ Add me baby ✙", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("• Help •", url="https://t.me/annu_support"),
            InlineKeyboardButton("• Dupport •", url="https://t.me/annu_support"),
        ],
        [
            InlineKeyboardButton("• Main bot •", url="https://t.me/Kirshnamusicbot?startgroup=true"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await msg.reply_photo(
        photo="https://files.catbox.moe/kbi6t5.jpg",
        caption=start_txt,
        reply_markup=reply_markup,
    )
