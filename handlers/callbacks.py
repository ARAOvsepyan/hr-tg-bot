import logging

from aiogram import Router, F
from aiogram.types import CallbackQuery

from data import HR_TRACKS, CAREER_PATHS, CAREER_DETAILS

callback_router = Router()

@callback_router.callback_query(F.data.startswith("track_"))
async def track_detail(callback: CallbackQuery):
    track_id = "_".join(callback.data.split("_")[1:])
    track = HR_TRACKS[track_id]

    current_kb = callback.message.reply_markup

    duties_list = "\n• ".join(track['duties'])
    text = (
        f"*{track['title']}*\n\n"
        f"{track['description']}\n\n"
        f"*Чем занимается:*\n• {duties_list}\n\n"
        f"{track['summary']}"
    )

    try:
        await callback.message.edit_text(
            text,
            reply_markup=current_kb,
            parse_mode="Markdown"
        )
    except Exception as e:
        logging.error(f"Ошибка редактирования сообщения: {e}")
        await callback.answer("Произошла ошибка")


@callback_router.callback_query(F.data == "hrbp_info")
async def hrbp_info(callback: CallbackQuery):
    await callback.message.answer(
        "HR Business Partner:\n\n"
        f"{CAREER_PATHS['senior']['roles'][0]}\n"
        "Стратегическая роль в компании"
    )
    await callback.answer()

@callback_router.callback_query(F.data.startswith("career_"))
async def career_detail(callback: CallbackQuery):
    career_detail = CAREER_DETAILS[callback.data]

    text = (
        f"<b>{career_detail['title']}</b>\n\n"
        f"{career_detail['text']}"
    )

    current_kb = callback.message.reply_markup

    try:
        await callback.message.edit_text(
            text,
            reply_markup=current_kb,
            parse_mode="HTML"
        )
    except Exception as e:
        logging.error(f"Ошибка редактирования сообщения: {e}")
        await callback.answer("Произошла ошибка")