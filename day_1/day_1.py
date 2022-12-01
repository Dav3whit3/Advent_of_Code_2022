from utils import get_input


def solve(input: bytes, n_last_elves: int) -> int:

    to_string           : str = input.decode("utf-8")
    clean_input         : list = to_string.strip().replace("\n\n", " ").split(" ")
    sorted_summatory    : list = sorted(map(lambda elf: sum(int(val) for val in elf.split("\n")), clean_input))

    return sum(sorted_summatory[-n_last_elves:])



#### main ####
if __name__ == "__main__":

    input = get_input(day=1)
    print(solve(input.content, n_last_elves=1))
    print(solve(input.content, n_last_elves=3))