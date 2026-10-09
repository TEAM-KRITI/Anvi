# 👑 Owner : Rich Yui
# ===========================================================
# 🎵 SHIVI MUSIC - AUTO PLAY SETTINGS
# ===========================================================

from pyrogram import enums, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from ShiviMusic import app
from ShiviMusic.utils.database import (
    autoplay_off,
    autoplay_on,
    is_autoplay_on,
)
from config import BANNED_USERS


# ===========================================================
# 👑 ADMIN CHECK
# ===========================================================

async def _is_admin(chat_id: int, user_id: int) -> bool:
    try:
        member = await app.get_chat_member(
            chat_id,
            user_id,
        )

        return member.status in (
            enums.ChatMemberStatus.ADMINISTRATOR,
            enums.ChatMemberStatus.OWNER,
        )

    except Exception:
        return False


# ===========================================================
# 📝 AUTO PLAY PANEL TEXT
# ===========================================================

def autoplay_text(
    message: Message,
    status: bool,
) -> str:

    chat_id = message.chat.id
    group_name = message.chat.title or "Unknown"

    status_text = (
        "🟢 enable"
        if status
        else
        "🔴 disable"
    )

    return (
        "**Auto play setting panel**\n\n"
        f"🌼 **ID :**`{chat_id}`\n"
        f"🍂 **status :**{status_text}\n"
        f"🏖 **group :****{group_name}**\n\n"
        "▣ **tap to manage**\n"
        "**Change autoplay setting.**"
    )


# ===========================================================
# 🔘 AUTO PLAY BUTTONS
# ===========================================================

def autoplay_markup(
    chat_id: int,
    status: bool,
) -> InlineKeyboardMarkup:

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🟢 enable",
                    callback_data=f"autoplay_enable:{chat_id}",
                ),
                InlineKeyboardButton(
                    "🔴 disable",
                    callback_data=f"autoplay_disable:{chat_id}",
                ),
            ],
            [
                InlineKeyboardButton(
                    "Close",
                    callback_data=f"autoplay_close:{chat_id}",
                )
            ],
        ]
    )


# ===========================================================
# 🎵 /AUTOPLAY COMMAND
# ===========================================================

@app.on_message(
    filters.command(["autoplay", "aplay"])
    & filters.group
    & ~BANNED_USERS
)
async def autoplay_cmd(
    client,
    message: Message,
):

    chat_id = message.chat.id

    # =======================================================
    # /autoplay on
    # /autoplay off
    # =======================================================

    if len(message.command) > 1:

        if not message.from_user:
            return

        # ---------------------------------------------------
        # ADMIN CHECK
        # ---------------------------------------------------

        if not await _is_admin(
            chat_id,
            message.from_user.id,
        ):

            return await message.reply_text(
                "❌ **sirf admins hi"
                "Autoplay manage kar sakte hain.**"
            )

        mode = message.command[1].lower()

        # ---------------------------------------------------
        # ENABLE
        # ---------------------------------------------------

        if mode in ("on", "enable"):

            await autoplay_on(chat_id)

            return await message.reply_text(
                "🟢 **autoplay enabled"
                "Successfully.**"
            )

        # ---------------------------------------------------
        # DISABLE
        # ---------------------------------------------------

        if mode in ("off", "disable"):

            await autoplay_off(chat_id)

            return await message.reply_text(
                "🔴 **autoplay disabled"
                "Successfully.**"
            )

        # ---------------------------------------------------
        # WRONG COMMAND
        # ---------------------------------------------------

        return await message.reply_text(
            "**Usage**\n\n"
            "➤ `/autoplay` — **open settings**\n"
            "➤ `/autoplay on` — **enable**\n"
            "➤ `/autoplay off` — **disable**"
        )

    # =======================================================
    # OPEN AUTO PLAY PANEL
    # =======================================================

    status = await is_autoplay_on(chat_id)

    await message.reply_text(
        autoplay_text(
            message,
            status,
        ),
        reply_markup=autoplay_markup(
            chat_id,
            status,
        ),
    )


# ===========================================================
# 🟢 ENABLE / 🔴 DISABLE CALLBACK
# ===========================================================

@app.on_callback_query(
    filters.regex(
        r"^autoplay_(enable|disable):(-?\d+)$"
    )
    & ~BANNED_USERS
)
async def autoplay_toggle_callback(
    client,
    query: CallbackQuery,
):

    action = query.matches[0].group(1)
    chat_id = int(query.matches[0].group(2))

    # =======================================================
    # MESSAGE CHECK
    # =======================================================

    if not query.message:

        return await query.answer(
            "❌ message not found.",
            show_alert=True,
        )

    # =======================================================
    # CHAT CHECK
    # =======================================================

    if query.message.chat.id != chat_id:

        return await query.answer(
            "❌ this button is not for this chat.",
            show_alert=True,
        )

    # =======================================================
    # ADMIN CHECK
    # =======================================================

    if not await _is_admin(
        chat_id,
        query.from_user.id,
    ):

        return await query.answer(
            "❌ only admins can"
            "Change autoplay.",
            show_alert=True,
        )

    # =======================================================
    # ENABLE
    # =======================================================

    if action == "enable":

        await autoplay_on(chat_id)

        status = True

        await query.answer(
            "🟢 autoplay enabled",
            show_alert=False,
        )

    # =======================================================
    # DISABLE
    # =======================================================

    else:

        await autoplay_off(chat_id)

        status = False

        await query.answer(
            "🔴 autoplay disabled",
            show_alert=False,
        )

    # =======================================================
    # UPDATE PANEL
    # =======================================================

    try:

        await query.message.edit_text(
            autoplay_text(
                query.message,
                status,
            ),
            reply_markup=autoplay_markup(
                chat_id,
                status,
            ),
        )

    except Exception:
        pass


# ===========================================================
# ❌ CLOSE CALLBACK
# ===========================================================

@app.on_callback_query(
    filters.regex(
        r"^autoplay_close:(-?\d+)$"
    )
    & ~BANNED_USERS
)
async def autoplay_close_callback(
    client,
    query: CallbackQuery,
):

    chat_id = int(
        query.matches[0].group(1)
    )

    # =======================================================
    # MESSAGE CHECK
    # =======================================================

    if not query.message:
        return

    # =======================================================
    # CHAT CHECK
    # =======================================================

    if query.message.chat.id != chat_id:

        return await query.answer(
            "❌ this button is not for this chat.",
            show_alert=True,
        )

    # =======================================================
    # CLOSE PANEL
    # =======================================================

    try:

        await query.message.delete()

        await query.answer(
            "Panel closed",
            show_alert=False,
        )

    except Exception:

        await query.answer(
            "❌ I can't close this panel.",
            show_alert=True,
        )


# ===========================================================
# ©️ 2025-26 SHIVI MUSIC
# ===========================================================
