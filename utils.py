import dotenv
dotenv.load_dotenv()
import os
import requests


def get_input(day: int):
    headers = {"cookie": str(os.getenv("COOKIE"))}
    return requests.get(f"https://adventofcode.com/2022/day/{day}/input", headers=headers)
