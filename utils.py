import requests
from requests import Response
import os
import dotenv
dotenv.load_dotenv()


class Input:

    def __init__(self, day: int) -> None:
        self.endpoint: str = f"https://adventofcode.com/2022/day/{day}/input"
        self.headers: dict = {"cookie": str(os.getenv("COOKIE"))}
        self.response: Response = requests.get(self.endpoint, headers=self.headers)
        self.content: str = self.response.text

    def get_list(self, split_by: str = '') -> list[str]:
        return self.content.split(split_by)

    def get_string(self) -> str:
        return self.content
