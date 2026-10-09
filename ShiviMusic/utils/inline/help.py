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

from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ShiviMusic import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data="settingsback_helper",
        ),
    ]

    mark = second if START else first

    def _b(text, cb):
        return InlineKeyboardButton(text=text, callback_data=f"help_callback {cb}")

    upl = InlineKeyboardMarkup(
        [
            [_b("ADMIN", "hb1"), _b("AUTH", "hb2"), _b("B-CHAT", "hb4")],
            [_b("G-CAST", "hb3"), _b("PLAYLIST", "hb10"), _b("PLAY", "hb5")],
            [_b("SUDO", "hb11"), _b("AC-VC", "hb7"), _b("START", "hb9")],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
            ]
        ]
    )
    return upl


def start_help_markup(_):
    import config

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_CHAT),
                InlineKeyboardButton(text="Uᴘᴅᴀᴛᴇs", url=config.SUPPORT_CHANNEL),
            ],
            [
                InlineKeyboardButton(text="Oᴡɴᴇʀ", url=f"tg://user?id={config.OWNER_ID}"),
                InlineKeyboardButton(text="Bᴀᴄᴋ", callback_data="settings_back_helper"),
            ],
        ]
    )


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons

# ===========================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎
# 
# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Shivi-V2
# 📢 Telegram channel : t.me/Purvi_Bots
# ===========================================================
