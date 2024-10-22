from aiogram.filters.state import State, StatesGroup


class UserCommentForm(StatesGroup):
    comment = State()


class UserGigaChatMessageForm(StatesGroup):
    message = State()
