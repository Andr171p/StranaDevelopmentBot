from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage, SystemMessage
from langchain_community.chat_models.gigachat import GigaChat
from langchain_core.messages import BaseMessage

from llm.credentials import GigaChatCredentials

from typing import List


class GigaChatModel:
    llm: GigaChat = None
    conversation: ConversationChain = None
    messages: List[SystemMessage | HumanMessage | BaseMessage] = []

    @classmethod
    def model(cls) -> None:
        cls.llm = GigaChat(
            credentials=GigaChatCredentials.token,
            verify_ssl_certs=False
        )
        cls.conversation = ConversationChain(
            llm=cls.llm,
            verbose=False,
            memory=ConversationBufferMemory(llm=cls.llm)
        )

    @classmethod
    def prompt(cls) -> None:
        template = ...
        cls.conversation.prompt.template = template

    @classmethod
    def system_message(cls, message: str) -> None:
        cls.messages.append(
            SystemMessage(
                content=message
            )
        )

    @classmethod
    def answer(cls, message: str) -> str:
        answer = cls.conversation.predict(input=message)
        return answer

    @classmethod
    def dialog(cls, message: str) -> str:
        cls.messages.append(
            HumanMessage(
                content=message
            )
        )
        answer: BaseMessage = cls.llm(cls.messages)
        cls.messages.append(answer)
        return answer.content
