import os

from typing import List, Dict

from misc.utils import (
    get_root_path,
    read_file
)


class GigaChatPrompts:
    SYSTEM_PROMPT_PATH = fr"{get_root_path()}/llm/prompt/system/strana_development.txt"
    USER_PROMPTS_DIRECTORY_PATH = fr"{get_root_path()}/llm/prompt/user"

    def __init__(self, chat: str) -> None:
        self.chat = chat

    @classmethod
    def chats_path(cls) -> List[str]:
        chats_path = []
        for filename in os.listdir(cls.USER_PROMPTS_DIRECTORY_PATH):
            chats_path.append(filename)
        return chats_path

    @classmethod
    def system_prompt(cls) -> str:
        system_prompt = read_file(file_path=cls.SYSTEM_PROMPT_PATH)
        return system_prompt

    @classmethod
    def prompts(cls) -> Dict[str, str]:
        prompts = {}
        chats_path = cls.chats_path()
        for filename in chats_path:
            prompt = f"{cls.system_prompt()}\n{read_file(file_path=os.path.join(cls.USER_PROMPTS_DIRECTORY_PATH, filename))}"
            chat = filename.split('.')[0]
            prompts[chat] = prompt
        return prompts

    def prompt(self) -> str:
        prompts = self.prompts()
        prompt = prompts[self.chat]
        return prompt

