from utils import Input
from functools import reduce
from typing import  Callable


class CampCleanup:

    def __init__(self, input: list[str]):
        self.input = list(map(lambda row: tuple(map(int, "-".join(row.split(",")).split("-"))), input))


    def get_range(self, pair: tuple) -> tuple[range, range]:
        return range(pair[0], pair[1] + 1), range(pair[2], pair[3] + 1)


    def is_contained(self, pairs: tuple, function: Callable) -> int:
        range_1, range_2 = self.get_range(pairs)

        if function(n in range_1 for n in range_2) \
        or function(n in range_2 for n in range_1):
            return 1

        return 0


    def solve(self, part: int) -> int:
        function = all if part == 1 else any
        return reduce(lambda acc, pairs: acc + self.is_contained(pairs=pairs, function=function), self.input, 0)


#### main ####
if __name__ == "__main__":
    input = Input(day=4).get_list(split_by="\n")
    cleaner = CampCleanup(input)

    print(
    "Result part 1: ", cleaner.solve(part=1),
    "\nResult part 2: ", cleaner.solve(part=2)
    )


