from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.internal.enums.welcome import RegistrationConfirmationOptions, WelcomeOptions


def get_welcome_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=WelcomeOptions.INFO)
    kb.button(text=WelcomeOptions.REGISTRATION)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def get_confirmation_keyboard() -> ReplyKeyboardMarkup:
    row = [
        KeyboardButton(text=item) for item in RegistrationConfirmationOptions.list()
    ]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
