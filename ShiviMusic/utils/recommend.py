# 👑 Owner : Rich Yui
# ===========================================================
# 🎧 RECOMMENDATIONS — queue khatam hone par "tap below to play
# next track" wala message (Previous + 5 songs + Random AI track)
# ===========================================================

import asyncio
import re

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from py_yt import VideosSearch

from ShiviMusic.utils.autoplay import (
    _extract_candidates,
    _extract_mix_candidates,
    _fetch_mix_sync,
)

_NOISE = re.compile(
    r"\((.*?)\)|\[(.*?)\]|\b(?:official|video|audio|lyrical|lyrics|full song|"
    r"hd|4k|music video)\b|\bfeat\.?.*$",
    re.I,
)


def short_title(title: str, limit: int = 30) -> str:
    t = _NOISE.sub("", title or "")
    t = re.sub(r"\s*[|\-–—].*$", lambda m: m.group(0) if len(t) <= limit else "", t)
    t = re.sub(r"\s+", " ", t).strip(" -|")
    t = t or (title or "")
    return (t[: limit - 1] + "…") if len(t) > limit else t


async def _search_fallback(seed_vidid: str, seed_title: str, n: int) -> list:
    """yt_dlp Mix fail (cookies/bot-check) ho to title search se recommendations."""
    try:
        if not seed_title:
            res = await VideosSearch(
                f"https://www.youtube.com/watch?v={seed_vidid}", limit=1
            ).next()
            items = res.get("result", []) if isinstance(res, dict) else []
            seed_title = items[0]["title"] if items else ""
        if not seed_title:
            return []
        res = await VideosSearch(seed_title, limit=15).next()
        items = res.get("result", []) if isinstance(res, dict) else []
    except Exception as e:
        print(f"[RECOMMEND SEARCH ERROR] {type(e).__name__}: {e}")
        return []
    cands = _extract_candidates(items, 0, skip_history=True)
    return [c for c in cands if c["vidid"] != seed_vidid][:n]


async def fetch_recommendations(seed_vidid: str, n: int = 5, seed_title: str = None) -> list:
    if not seed_vidid:
        return []
    loop = asyncio.get_event_loop()
    cands = []
    try:
        entries = await loop.run_in_executor(None, _fetch_mix_sync, seed_vidid, 25)
        cands = _extract_mix_candidates(entries, 0, skip_history=True)
        cands = [c for c in cands if c["vidid"] != seed_vidid]
    except Exception as e:
        print(f"[RECOMMEND ERROR] {e}")
    if not cands:
        cands = await _search_fallback(seed_vidid, seed_title, n)
    return cands[:n]


def recommend_text(prev_title: str) -> str:
    return (
        "<b>Queue ended</b>\n"
        "<blockquote>"
        f"<b>👑 previous:</b> <code>{prev_title[:40]}…</code>\n"
        "<b>💡 tap below to play next track</b>"
        "</blockquote>"
    )


def recommend_markup(tracks: list, seed_vidid: str) -> InlineKeyboardMarkup:
    rows = [
        [
            InlineKeyboardButton(
                f"👑 {short_title(t['title'])}",
                callback_data=f"RecPlay {t['vidid']}",
            )
        ]
        for t in tracks
    ]
    rows.append(
        [
            InlineKeyboardButton(
                "Play random ai track",
                callback_data=f"RecRand {seed_vidid}",
            )
        ]
    )
    rows.append([InlineKeyboardButton("• Close •", callback_data="close")])
    return InlineKeyboardMarkup(rows)


async def send_recommendations(app, original_chat_id: int, popped: dict) -> bool:
    """Queue khatam hone par call.py / skip.py se call hota hai."""
    try:
        seed = popped.get("vidid")
        print(f"[RECOMMEND] queue ended, seed={seed}, chat={original_chat_id}")
        tracks = await fetch_recommendations(seed, seed_title=popped.get("title"))
        if not tracks:
            print("[RECOMMEND] koi track nahi mila (yt_dlp/cookies/network check karo)")
            return False
        await app.send_message(
            original_chat_id,
            recommend_text(popped.get("title") or "—"),
            reply_markup=recommend_markup(tracks, seed),
        )
        print(f"[RECOMMEND] {len(tracks)} tracks bhej diye")
        return True
    except Exception as e:
        print(f"[RECOMMEND ERROR] {type(e).__name__}: {e}")
        return False
