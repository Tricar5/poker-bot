from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from bot.handlers.welcome.fsm import WelcomeFSM
from bot.internal.enums.welcome import RegistrationConfirmationOptions, WelcomeOptions
from bot.internal.texts import welcome
from bot.keyboards.welcome import get_confirmation_keyboard, get_welcome_keyboard

router = Router()


@router.message(StateFilter(None), Command('start'))
async def cmd_start(message: Message) -> None:
    await message.answer(
        text=welcome.WELCOME_TEXT,
        reply_markup=get_welcome_keyboard(),
    )


@router.message(F.text == WelcomeOptions.INFO)
async def answer_rules(message: Message, state: FSMContext) -> None:
    await message.answer(
        text=welcome.WELCOME_RULES,
        reply_markup=get_welcome_keyboard(),
    )
    await state.set_state(WelcomeFSM.welcome)


@router.message(F.text == WelcomeOptions.REGISTRATION)
async def answer_ask_registration(message: Message, state: FSMContext) -> None:
    await message.answer(
        text=welcome.WELCOME_REGISTER,
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.set_state(WelcomeFSM.input_login)


@router.message(
    WelcomeFSM.input_login,
)
async def input_nickname(message: Message, state: FSMContext) -> None:
    await state.set_data({'login': message.text})
    await message.answer(
        text=f'Отлично, тогда зарегистрируем тебя под логином {message.text}',
        reply_markup=get_confirmation_keyboard(),
    )
    await state.set_state(WelcomeFSM.confirmation)

@router.message(
    WelcomeFSM.confirmation,
    F.text == RegistrationConfirmationOptions.AGREE.value,
)
async def answer_confirmed(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    await message.answer(
        text=welcome.SUCCESS_REGISTER.format(data['login']),
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )
    await state.clear()


@router.message(
    WelcomeFSM.confirmation,
    F.text == RegistrationConfirmationOptions.RETRY.value,
)
async def answer_retry(message: Message, state: FSMContext) -> None:
    await message.answer(
        text='Давай попробуем ещё раз. Введите ещё раз логин для регистрации',
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.set_data({'login': None})
    await state.set_state(WelcomeFSM.input_login)


@router.message(
    WelcomeFSM.confirmation,
    F.text == RegistrationConfirmationOptions.CANCEL.value,
)
async def answer_cancel(message: Message, state: FSMContext) -> None:
    await message.answer(
        text='Хорошо, конечно. Можем отложить регистрацию на потом',
        reply_markup=get_welcome_keyboard(),
    )
    await state.set_data({'login': None})
    await state.set_state(WelcomeFSM.welcome)
