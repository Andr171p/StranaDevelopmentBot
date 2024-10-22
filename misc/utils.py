from pathlib import Path


def read_file(file_path: str) -> str:
    with open(file=file_path, mode='r', encoding='utf-8') as file:
        text = file.readlines()
    return ''.join(text)


def get_root_path() -> Path:
    root_path = Path(__file__).resolve().parents[1]
    return root_path
