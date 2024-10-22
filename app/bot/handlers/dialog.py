from aiogram import F, Router
from aiogram.types import Message

from langchain.memory import ConversationBufferMemory

from llm.model.giga_chat import giga_chat_model

from app.bot.messages import ErrorMessage
from app.bot.keyboards.roles_menu import roles_menu_kb


dialog_router = Router()

user_conversation = {}


@dialog_router.message()
async def dialog_handler(message: Message) -> None:
    try:
        user_id = message.from_user.id
        user_message = message.text
        if user_id not in user_conversation:
            user_conversation[user_id] = ConversationBufferMemory()
        giga_chat_model.conversation.memory = user_conversation[user_id]
        answer = giga_chat_model.dialog(message=user_message)
        await message.answer(
            text=answer,
            reply_markup=await roles_menu_kb()
        )
    except Exception as _ex:
        await message.answer(
            text=ErrorMessage.MODEL_NOT_CREATED_MESSAGE,
            reply_markup=await roles_menu_kb()
        )
