import os
import dotenv
dotenv.load_dotenv()
import requests
from functools import reduce


headers = {
    "cookie": str(os.getenv("COOKIE"))
}
input = requests.get("https://adventofcode.com/2022/day/1/input", headers=headers)


def solve(input: bytes, n_last_elves: int) -> int:

    to_string           : str = input.decode("utf-8")
    clean_input         : list = to_string.strip().replace("\n\n", " ").split(" ")
    sorted_summatory    : list = sorted(map(lambda elf: sum(int(val) for val in elf.split("\n")), clean_input))

    return sum(sorted_summatory[-n_last_elves:])


print(solve(input.content, n_last_elves=1))
print(solve(input.content, n_last_elves=3))