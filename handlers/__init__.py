from aiogram import Router

from .start import start_router
from .quiz import quiz_router
from .menu import menu_router
from .callbacks import callback_router
from .errors import error_router

router = Router()

# Подключение всех роутеров
router.include_router(start_router)
router.include_router(quiz_router)
router.include_router(menu_router)
router.include_router(callback_router)
router.include_router(error_router)

__all__ = ['router']