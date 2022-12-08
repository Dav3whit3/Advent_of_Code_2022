from utils import Input
input = Input(day=5).get_string()


def solve(data: str, n_distinct: int) -> int | None:
    for n in range(len(data)):
        marker = data[n : n + n_distinct]
        if len(marker) == len(set(marker)):
            return n + n_distinct

# #### main ####
if __name__ == "__main__":
    input = Input(day=6).get_string()
    print(
        "Result part 1: ", solve(input, 4),
        "\nResult part 2: ", solve(input, 14)
    )

"https://www.google-analytics.com/j/collect?v=1&_v=j98&aip=1&a=205088305&t=pageview&_s=1&dl=https://adventofcode.com/2022/day/6/answer&ul=en&de=UTF-8&dt=Day 6 - Advent of Code 2022&sd=24-bit&sr=3440x1440&vp=783x1043&je=0&_u=QACAAEABAAAAACAAI~&jid=&gjid=&cid=1538360304.1669116444&tid=UA-69522494-1&_gid=1105788993.1669886215&_slc=1&z=1126299987"