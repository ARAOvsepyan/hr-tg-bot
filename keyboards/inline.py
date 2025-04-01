from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data import HR_TRACKS, WORKSHOPS_LIST

def hr_tracks_kb() -> InlineKeyboardMarkup:
    """Клавиатура с треками HR"""
    builder = InlineKeyboardBuilder()
    for track_id, track in HR_TRACKS.items():
        builder.add(InlineKeyboardButton(
            text=track['title'],
            callback_data=f"track_{track_id}"
        ))
    builder.adjust(2)
    return builder.as_markup()

def career_details_kb() -> InlineKeyboardMarkup:
    """Клавиатура для раздела карьеры"""
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text="Чем отличается HR BP от HR и HRD?",
            callback_data="career_hrbp_vs_hrd"
        ),
        InlineKeyboardButton(
            text="Как стать HR BP?",
            callback_data="career_become_hrbp"
        ),
        InlineKeyboardButton(
            text="HR Director",
            callback_data="career_hrd"
        ),
        InlineKeyboardButton(
            text="HR People Partner",
            callback_data="career_hrpp"
        )
    )
    builder.adjust(2, 2)
    return builder.as_markup()

def workshops_kb() -> InlineKeyboardMarkup:
    """Клавиатура для воркшопов"""
    builder = InlineKeyboardBuilder()
    for workshop in WORKSHOPS_LIST:
        builder.add(InlineKeyboardButton(
            text=workshop['button_text'],
            url=workshop['link']
        ))
    builder.adjust(2)
    return builder.as_markup()

def pagination_kb(page: int = 0, total_pages: int = 1) -> InlineKeyboardMarkup:
    """Клавиатура пагинации"""
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text="⬅️",
            callback_data=f"prev_{page}" if page > 0 else "empty"
        ),
        InlineKeyboardButton(
            text=f"{page+1}/{total_pages}",
            callback_data="current"
        ),
        InlineKeyboardButton(
            text="➡️",
            callback_data=f"next_{page}" if page < total_pages-1 else "empty"
        )
    )
    return builder.as_markup()