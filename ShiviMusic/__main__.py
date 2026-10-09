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

import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from ShiviMusic import LOGGER, app, userbot
from ShiviMusic.core.call import Shivi
from ShiviMusic.misc import sudo
from ShiviMusic.plugins import ALL_MODULES
from ShiviMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("STRING SESSION NOT FILLED 🙃, PLEASE FILL A PYROGRAM SESSION...🙂")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ShiviMusic.plugins" + all_module)
    LOGGER("ShiviMusic.plugins").info("ALL PLUGINS LOADED SUCCESSFULLY....🥳..")
    await userbot.start()
    await Shivi.start()
    try:
        await Shivi.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("ShiviMusic").error(
            "PlZ START YOUR LOG GROUP/CHANNEL VOICECHAT... 😒\n\nMUSIC BOT STOP........🤕"
        )
        exit()
    except:
        pass
    await Shivi.decorators()
    LOGGER("ShiviMusic").info(
        "╔═════ஜ۩۞۩ஜ════╗\n☠︎︎ MADE BY KIRTI BOTS ☠︎︎\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ShiviMusic").info("STOP MUSIC BOT...🥹")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())

# ===========================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎
# 
# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Shivi-V2
# 📢 Telegram channel : t.me/Purvi_Bots
# ===========================================================
