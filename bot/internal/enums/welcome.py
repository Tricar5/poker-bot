from enum import StrEnum

from bot.internal.enums.base import ExtendedEnum


class WelcomeOptions(StrEnum, ExtendedEnum):
    INFO = 'Информация'
    REGISTRATION = 'Регистрация'

class RegistrationConfirmationOptions(StrEnum, ExtendedEnum):
    AGREE = 'Подтверждаю'
    RETRY = 'Ввести логин повторно'
    CANCEL = 'Отмена'
