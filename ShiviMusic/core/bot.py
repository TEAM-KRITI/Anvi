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

from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class Shivi(Client):
    def __init__(self):
        LOGGER(__name__).info(f"» Starting bot...")
        super().__init__(
            name="ShiviMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=(
                    f"<u><b>» {self.mention} bot started:</b></u>\n\n"
                    f"ID: <code>{self.id}</code>\n"
                    f"Name: {self.name}\n"
                    f"Username: @{self.username}"
                ),
            )
        except:
            LOGGER(__name__).error(
                "» Bot has failed to access the log group/channel. Make sure that you have added your bot to your log group/channel."
            )
        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "» Please promote your bot as an admin in your log group/channel."
            )
        LOGGER(__name__).info(f"✦ Music bot started as {self.name}")

    async def stop(self):
        await super().stop()

# ===========================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎
# 
# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Shivi-V2
# 📢 Telegram channel : t.me/Purvi_Bots
# ===========================================================
