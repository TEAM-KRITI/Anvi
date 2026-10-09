# 👑 Owner : Rich Yui
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums
import config


class BUTTONS(object):

    ABUTTON = [
        [
            InlineKeyboardButton(
                "Support",
                url="https://t.me/kirti_bots_support"
            ),
            InlineKeyboardButton(
                "Updates",
                url="https://t.me/kirti_bots"
            )
        ],
        [
            InlineKeyboardButton(
                "❍Owner",
                user_id=config.OWNER_ID
            ),
            InlineKeyboardButton(
                "Back",
                callback_data="settingsback_helper"
            )
        ]
    ]


    INFO_BUTTON = [
        [
            InlineKeyboardButton(
                "Repo",
                callback_data="gib_source"
            ),
            InlineKeyboardButton(
                "Yt-API",
                callback_data="bot_info_data"
            ),
            InlineKeyboardButton(
                "Language",
                callback_data="LG"
            )
        ],
        [
            InlineKeyboardButton(
                "Privacy",
                url="https://files.catbox.moe/u21pts.jpg"
            ),
            InlineKeyboardButton(
                "Back",
                callback_data="settingsback_helper"
            )
        ]
    ]


    INFO_NEW = [
        [
            InlineKeyboardButton(
                "Back",
                callback_data="settings_back_helper"
            )
        ]
    ]
