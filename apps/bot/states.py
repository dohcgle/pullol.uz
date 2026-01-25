from aiogram.fsm.state import State, StatesGroup

class ApplicationStates(StatesGroup):
    full_name = State()
    phone_number = State()
    region = State()
    credit_amount = State()
    collateral = State()
