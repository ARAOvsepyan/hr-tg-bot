from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from data import START_QUIZ_MESSAGE
from data.messages import WELCOME_MESSAGE, HR_INTRO
from keyboards import yes_no_kb
from utils.states import DialogStates

start_router = Router()

@start_router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(DialogStates.waiting_welcome_response)
    await message.answer(WELCOME_MESSAGE, reply_markup=yes_no_kb())

@start_router.message(
    F.text.lower() == "да",
    DialogStates.waiting_welcome_response
)
async def handle_welcome_yes(message: Message, state: FSMContext):
    await state.set_state(DialogStates.waiting_hr_intro_response)
    await message.answer(HR_INTRO, reply_markup=yes_no_kb())

@start_router.message(
    F.text.lower() == "нет",
    DialogStates.waiting_welcome_response
)
async def handle_welcome_no(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Может быть в другой раз!", reply_markup=ReplyKeyboardRemove())

@start_router.message(
    F.text.lower() == "да",
    DialogStates.waiting_hr_intro_response
)
async def handle_hr_intro_yes(message: Message, state: FSMContext):
    await state.set_state(DialogStates.quiz_1)
    await message.answer(START_QUIZ_MESSAGE)
    from .quiz import start_quiz
    await start_quiz(message, state)

@start_router.message(
    F.text.lower() == "нет",
    DialogStates.waiting_hr_intro_response
)
async def handle_hr_intro_no(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Хорошо, если передумаешь - напиши /start")