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

from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("» Connecting to your mongo database...")
try:
    _mongo_async_ = AsyncIOMotorClient(
        MONGO_DB_URI,
        maxPoolSize=100,
        minPoolSize=5,
        serverSelectionTimeoutMS=15000,
        compressors="zlib",
    )
    mongodb = _mongo_async_.Yukki
    LOGGER(__name__).info("» Connected to your mongo database.")
except:
    LOGGER(__name__).error("» Failed to connect to your mongo database.")
    exit()

# ===========================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎
# 
# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Shivi-V2
# 📢 Telegram channel : t.me/Purvi_Bots
# ===========================================================
