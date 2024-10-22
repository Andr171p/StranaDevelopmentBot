import base64


class GigaChatCredentials:
    CLIENT_SECRET = "fcbf6221-f7bb-4f55-80ae-161f2653de98"
    CLIENT_ID = "32611b0c-3994-4238-8df6-2c66bddf1819"

    @classmethod
    @property
    def token(cls) -> str:
        credentials = f"{cls.CLIENT_ID}:{cls.CLIENT_SECRET}"
        encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
        return encoded_credentials
