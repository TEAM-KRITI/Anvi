# 👑 Owner : Rich Yui
# ===========================================================
# 🎆 Reaction + message-effect helpers (animation)
# - react_on(msg)           : message par big (full-screen) reaction animation
# - reply_photo_effect(...) : private chat me message-effect ke saath photo
# ===========================================================

import random

from pyrogram.errors import FloodWait

# Telegram ke free reactions (har chat me allowed hote hain)
REACTIONS = ["👍", "🔥", "🥰", "🎉", "😍", "🤩", "💯", "⚡", "👏", "😎", "🏆", "🤝", "❤"]

# Message effects (sirf private chat): 👍 5107584321108051014 | ❤️ 5159385139981059251
# 🔥 5104841245755180586 | 🎉 5046509860389126442
EFFECT_IDS = [
    5107584321108051014,
    5159385139981059251,
    5104841245755180586,
    5046509860389126442,
]


async def react_on(msg, tries: int = 4) -> bool:
    """
    Kisi bhi message par big animated reaction lagao.
    NOTE: bot apne hi bheje message par react nahi kar sakta, isliye
    hamesha USER ke message par call karo (command message).
    Ek emoji fail ho (REACTION_INVALID) to agla try hota hai.
    """
    if not msg:
        return False
    pool = REACTIONS[:]
    random.shuffle(pool)
    for emoji in pool[:tries]:
        for big in (True, False):
            try:
                await msg.react(emoji, big=big)
                return True
            except FloodWait:
                return False
            except TypeError:
                # purani library jisme big= nahi hai
                try:
                    await msg.react(emoji)
                    return True
                except Exception:
                    break
            except Exception:
                continue
    return False


async def reply_photo_effect(message, effect_id: int = None, **kwargs):
    """Private chat me message-effect (full screen animation) ke saath photo bhejo.
    Param naam library ke hisaab se alag ho sakta hai, isliye dono try karte hain."""
    effect_id = effect_id or random.choice(EFFECT_IDS)
    for key in ("message_effect_id", "effect_id"):
        try:
            return await message.reply_photo(**kwargs, **{key: effect_id})
        except TypeError:
            continue
        except Exception as e:
            print(f"[effect] {type(e).__name__}: {e}")
            break
    return await message.reply_photo(**kwargs)
