from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from typing import List, Tuple


def build_inline_kb(
        buttons: List[Tuple[str, str]],
        schema: List[int] = None
) -> InlineKeyboardMarkup:
    """
    Универсальный builder для inline-клавиатур
    :param buttons: Список кортежей (текст, callback_data)
    :param schema: Схема расположения кнопок (например [2, 1] - два в первом ряду, одна во втором)
    """
    builder = InlineKeyboardBuilder()
    for text, callback_data in buttons:
        builder.add(InlineKeyboardButton(text=text, callback_data=callback_data))

    if schema:
        builder.adjust(*schema)
    return builder.as_markup()


def build_dynamic_kb(items: list, prefix: str, per_row: int = 3):
    """Генератор клавиатур для динамических списков"""
    builder = InlineKeyboardBuilder()
    for item in items:
        builder.add(InlineKeyboardButton(
            text=item['name'],
            callback_data=f"{prefix}_{item['id']}"
        ))
    builder.adjust(per_row)
    return builder.as_markup()