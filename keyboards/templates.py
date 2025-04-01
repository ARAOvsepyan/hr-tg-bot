from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton
)

def yes_no_kb() -> ReplyKeyboardMarkup:
    """Шаблон клавиатуры Да/Нет"""
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Да"),
        KeyboardButton(text="Нет")
    )
    return builder.as_markup(resize_keyboard=True)

def agree_disagree_kb() -> InlineKeyboardMarkup:
    """Шаблон inline-клавиатуры Согласен/Не согласен"""
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="✅ Согласен", callback_data="agree"),
        InlineKeyboardButton(text="❌ Не согласен", callback_data="disagree")
    )
    return builder.as_markup()

def contact_share_kb() -> ReplyKeyboardMarkup:
    """Клавиатура для запроса контакта"""
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📱 Отправить контакт", request_contact=True)]],
        resize_keyboard=True
    )