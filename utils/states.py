from aiogram.fsm.state import StatesGroup, State


class DialogStates(StatesGroup):
    # Состояния для начального диалога
    waiting_welcome_response = State()
    waiting_hr_intro_response = State()

    # Состояния для опроса
    quiz_1 = State()
    quiz_2 = State()
    quiz_3 = State()
    quiz_4 = State()
    quiz_5 = State()
    quiz_6 = State()
    quiz_7 = State()
    quiz_8 = State()
    quiz_9 = State()
    quiz_10 = State()
    quiz_result = State()  # Финальное состояние