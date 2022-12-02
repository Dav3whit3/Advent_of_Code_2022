from utils import get_input
from functools import reduce
from dataclasses import dataclass


@dataclass
class RPS:
    # Part 1
    HAND_VALUES        = {"A": 1, "B": 2, "C": 3}
    TRANSLATE_PART_1   = {"X": "A", "Y": "B", "Z": "C" }
    WINNER             = { "AB": "B", "AC": "A", "BC": "C" }

    # Part 2
    WIN_VALUES         = {"Y": 3, "Z": 6}
    TRANSLATE_PART_2   = {"A": {"X": "C", "Z": "B"}, "B": {"X": "A", "Z": "C"}, "C": {"X": "B", "Z": "A"}}

    def part_1(self, hand: str) -> int:

        elf, me = hand[0], self.TRANSLATE_PART_1[hand[1]]
        sorted_hand = "".join(sorted(elf + me))
        winner = None if len(set(sorted_hand)) == 1 else self.WINNER[sorted_hand]

        if not winner:     return self.HAND_VALUES[me] + 3
        elif winner == me: return self.HAND_VALUES[me] + 6

        return self.HAND_VALUES[me]


    def part_2(self, hand: str) -> int:

        elf, instruction = hand[0], hand[1]
        me = self.TRANSLATE_PART_2[elf].get(instruction, elf)

        return self.HAND_VALUES[me] + self.WIN_VALUES.get(instruction, 0)


    def solve(self, input_data: list[str], part: str) -> int:
        fn = getattr(self, part)
        return reduce(lambda acc, val: acc + fn(val) , input_data, 0)


#### main ####
if __name__ == "__main__":
    input = get_input(day=2)
    to_string = input.decode("utf-8").strip().split("\n")
    clean_input = [hand.replace(" ", "").strip() for hand in to_string]

    day_2 = RPS()
    print(
        day_2.solve(input_data=clean_input, part="part_1"),
        day_2.solve(input_data=clean_input, part="part_2")
    )

