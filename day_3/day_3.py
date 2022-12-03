from utils import get_input
from functools import reduce
from string import ascii_letters
from itertools import islice
from typing import Iterator


class RucksackManager:

    def __init__(self, input: list[str]):
        self.input = input

    # Utils
    def get_chunks(self, arr_range: Iterator[str], chunk_size: int):
        arr_range = iter(arr_range)
        return iter(lambda: tuple(islice(arr_range, chunk_size)), ())

    def get_letter_value(self, item: set) -> int:
        value = (i for i, value in enumerate(ascii_letters, start=1) if value == list(item)[0])

        return sum(value)

    # Part 1
    def get_shared_item_part_1(self, rucksuck: str) -> set:
        split = int(len(rucksuck) / 2)
        compartment_1 = rucksuck[:split]
        compartment_2 = rucksuck[split:]
        common_type = set(compartment_1).intersection(compartment_2)

        return common_type

    def get_shared_item_value(self, rucksuck: str) -> int:
        shared_item = self.get_shared_item_part_1(rucksuck)
        value = self.get_letter_value(shared_item)

        return value

    def solve_part_1(self) -> int:
        return reduce(lambda acc, value: acc + self.get_shared_item_value(value), self.input, 0)

    # Part 2
    def get_shared_item_value_part_2(self, rucksack: tuple):
        shared_item = set(rucksack[0]).intersection(set(rucksack[1])).intersection(set(rucksack[2]))
        value = self.get_letter_value(list(shared_item)[0])

        return value

    def solve_part_2(self) -> int:

        data = (rucksack for rucksack in self.input)
        chunks = self.get_chunks(data, 3)

        return reduce(lambda acc, value: acc + self.get_shared_item_value_part_2(value), chunks, 0)


#### main ####
if __name__ == "__main__":
    input = get_input(day=3)
    clean_input = input.decode("utf-8").strip().split("\n")


    rucksack_manager = RucksackManager(clean_input)
    print(
        rucksack_manager.solve_part_1(),
        rucksack_manager.solve_part_2()
    )
