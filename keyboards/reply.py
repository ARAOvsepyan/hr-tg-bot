from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_kb() -> ReplyKeyboardMarkup:
    """Главное меню бота"""
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="5 треков HR"),
        KeyboardButton(text="Карьера в HR")
    )
    builder.row(
        KeyboardButton(text="HR-воркшопы"),
        KeyboardButton(text="Тренды HR 2025")
    )
    return builder.as_markup(resize_keyboard=True)

def quiz_options_kb(options: list[str]) -> ReplyKeyboardMarkup:
    """Генерирует клавиатуру с вариантами ответов"""
    builder = ReplyKeyboardBuilder()
    for option in options:
        builder.add(KeyboardButton(text=option))
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

def cancel_kb() -> ReplyKeyboardMarkup:
    """Клавиатура с одной кнопкой Отмена"""
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Отмена")]],
        resize_keyboard=True
    )