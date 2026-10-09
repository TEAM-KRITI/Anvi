# 👑 Owner : Rich Yui
# ===========================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀
# 
# This source code is under MIT License 📜
# ❌ Unauthorized forking, importing, or using this code
#    without giving proper credit will result in legal action ⚠️
# 
# 📩 DM for permission : @TheSigmaCoder
# ===========================================================

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ShiviMusic import app

@app.on_message(filters.command("privacy"))
async def privacy_command(client: Client, message: Message):
    await message.reply_photo(
          has_spoiler=True,
        photo="https://d.uguu.se/LbHGyjwp.jpg",
        caption="**Welcome to kirti bots privacy policy.**\n\n**⊚ click the below button then see privacy policy 🔏**",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Promo", url="https://t.me/Only_badnam?text=Hey%20baby%20%20😄%20I%20want%20paid%20promotion,%20give%20me%20price%20list%20😙")]
            ]
        )
    )

# ===========================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎
# 
# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Shivi-V2
# 📢 Telegram channel : t.me/Purvi_Bots
# ===========================================================
