from aiogram.fsm.state import State, StatesGroup


class WelcomeFSM(StatesGroup):
    welcome = State()
    input_login = State()
    confirmation = State()
