from aiogram import Router, F
from aiogram.types import Message

from data import HR_TRACKS, CAREER_PATHS, WORKSHOPS_LIST, TRENDS_2025
from keyboards.inline import (
    hr_tracks_kb,
    career_details_kb,
    workshops_kb
)

menu_router = Router()

@menu_router.message(F.text == "5 треков HR")
async def show_tracks(message: Message):
    tracks_text = "\n\n".join(
        f"{track['title']}\n{track['info']}"
        for track in HR_TRACKS.values()
    )
    await message.answer(
        "🚀 Топ-5 HR-треков:\n\n" + tracks_text,
        reply_markup=hr_tracks_kb()
    )

@menu_router.message(F.text == "Карьера в HR")
async def show_career(message: Message):
    await message.answer(
        "📈 Карьерные уровни в HR:\n\n"
        f"{CAREER_PATHS}",
        parse_mode="HTML",
        reply_markup=career_details_kb()
    )

@menu_router.message(F.text == "HR-воркшопы")
async def show_workshops(message: Message):
    workshops_text = "\n\n".join(
        f"{ws['title']}"
        for ws in WORKSHOPS_LIST
    )
    await message.answer(
        "🎓 Доступные воркшопы:\n\n" + workshops_text,
        reply_markup=workshops_kb()
    )

@menu_router.message(F.text == "Тренды HR 2025")
async def show_trends(message: Message):
    text = TRENDS_2025
    await message.answer(
        text,
        disable_web_page_preview=True,
        parse_mode="HTML"
    )