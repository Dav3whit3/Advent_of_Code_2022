from utils import Input


def solve(input: str, n_last_elves: int) -> int:

    clean_input: list = input.replace("\n\n", " ").split(" ")
    sorted_summatory: list = sorted(map(lambda elf: sum(int(val) for val in elf.split("\n")), clean_input))

    return sum(sorted_summatory[-n_last_elves:])


#### main ####
if __name__ == "__main__":

    input = Input(day=1).get_string()

    print(solve(input, n_last_elves=1))
    print(solve(input, n_last_elves=3))
