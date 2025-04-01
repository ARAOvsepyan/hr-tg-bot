import logging

from aiogram import Router
from aiogram.types import ErrorEvent
from aiogram.filters import ExceptionTypeFilter
from aiogram.exceptions import TelegramBadRequest

error_router = Router()
logger = logging.getLogger(__name__)

@error_router.error(ExceptionTypeFilter(TelegramBadRequest))
async def handle_telegram_error(event: ErrorEvent):
    if "message to edit not found" in str(event.exception):
        return
    await event.update.message.answer("Произошла ошибка API Telegram")


@error_router.error()
async def handle_all_errors(event: ErrorEvent):
    logging.error("Unhandled error", exc_info=event.exception)
    await event.update.message.answer(
        "⚠️ Произошла непредвиденная ошибка. Попробуйте позже."
    )