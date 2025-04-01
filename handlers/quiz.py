import logging

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

from data.quiz_questions import QUESTIONS, ANSWERS_SCORE, RESULT_THRESHOLDS, START_QUIZ_MESSAGE
from utils.states import DialogStates
from keyboards.reply import main_menu_kb, cancel_kb, quiz_options_kb

quiz_router = Router()
logger = logging.getLogger(__name__)


async def start_quiz(message: Message, state: FSMContext):
    """Начало опроса"""
    await state.set_state(DialogStates.quiz_1)
    await send_question(message, state)


async def send_question(message: Message, state: FSMContext):
    """Отправка текущего вопроса с вариантами ответов"""
    current_state = await state.get_state()
    if not current_state:
        return

    state_name = current_state.split(':')[-1]
    question_num = int(state_name.split('_')[-1])
    question = QUESTIONS[question_num]

    await message.answer(
        f"Вопрос {question_num}/10:\n\n{question['text']}",
        reply_markup=quiz_options_kb(question['options'])
    )

@quiz_router.message(Command("quiz"))
async def quiz(message: Message, state: FSMContext):
    await state.set_state(DialogStates.quiz_1)
    await message.answer(START_QUIZ_MESSAGE)
    await start_quiz(message, state)

# Обработчики для каждого вопроса
@quiz_router.message(DialogStates.quiz_1)
async def process_q1(message: Message, state: FSMContext):
    await state.update_data(q1=message.text)
    await state.set_state(DialogStates.quiz_2)
    await send_question(message, state)


@quiz_router.message(DialogStates.quiz_2)
async def process_q2(message: Message, state: FSMContext):
    await state.update_data(q2=message.text)
    await state.set_state(DialogStates.quiz_3)
    await send_question(message, state)


@quiz_router.message(DialogStates.quiz_3)
async def process_q2(message: Message, state: FSMContext):
    await state.update_data(q3=message.text)
    await state.set_state(DialogStates.quiz_4)
    await send_question(message, state)


@quiz_router.message(DialogStates.quiz_4)
async def process_q2(message: Message, state: FSMContext):
    await state.update_data(q4=message.text)
    await state.set_state(DialogStates.quiz_5)
    await send_question(message, state)


@quiz_router.message(DialogStates.quiz_5)
async def process_q2(message: Message, state: FSMContext):
    await state.update_data(q5=message.text)
    await state.set_state(DialogStates.quiz_6)
    await send_question(message, state)


@quiz_router.message(DialogStates.quiz_6)
async def process_q2(message: Message, state: FSMContext):
    await state.update_data(q6=message.text)
    await state.set_state(DialogStates.quiz_7)
    await send_question(message, state)


@quiz_router.message(DialogStates.quiz_7)
async def process_q2(message: Message, state: FSMContext):
    await state.update_data(q7=message.text)
    await state.set_state(DialogStates.quiz_8)
    await send_question(message, state)


@quiz_router.message(DialogStates.quiz_8)
async def process_q2(message: Message, state: FSMContext):
    await state.update_data(q8=message.text)
    await state.set_state(DialogStates.quiz_9)
    await send_question(message, state)


@quiz_router.message(DialogStates.quiz_9)
async def process_q2(message: Message, state: FSMContext):
    await state.update_data(q9=message.text)
    await state.set_state(DialogStates.quiz_10)
    await send_question(message, state)


@quiz_router.message(DialogStates.quiz_10)
async def process_q10(message: Message, state: FSMContext):
    await state.update_data(q10=message.text)
    await show_results(message, state)


async def show_results(message: Message, state: FSMContext):
    """Вычисление и вывод результатов"""
    data = await state.get_data()

    total_score = sum(
        ANSWERS_SCORE[q_num][data[f"q{q_num}"]]
        for q_num in range(1, 11)
    )

    if total_score >= RESULT_THRESHOLDS['high']:
        result = """Похоже, у тебя есть отличные задатки для профессии HR! Ты коммуникабелен(льна), умеешь решать конфликты и помогать людям. Продолжай развиваться, и у тебя все получится!"""
    else:
        result = """У тебя есть потенциал, но некоторые навыки нужно прокачать. Попробуй больше общаться с людьми, участвовать в командных проектах и учиться решать конфликты. Ты на правильном пути!"""

    await message.answer(
        f"Твой результат: {total_score}/20✅\n\n{result}",
        reply_markup=main_menu_kb()
    )
    await state.clear()


@quiz_router.message(F.text == "Прервать опрос")
async def cancel_quiz(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Опрос прерван. Нажми /quiz чтобы начать заново.",
        reply_markup=ReplyKeyboardRemove()
    )
