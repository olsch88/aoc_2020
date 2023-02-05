from itertools import permutations
import time


def solve_part1(data: list[int]) -> int:
    combinations = permutations(data, 2)
    for pair in combinations:
        if pair[0] + pair[1] == 2020:
            return pair[0] * pair[1]

    return 0


def solve_part2(data: list[int]) -> int:
    combinations = permutations(data, 3)
    for triple in combinations:
        if triple[0] + triple[1] + triple[2] == 2020:
            return triple[0] * triple[1] * triple[2]

    return 0


def main():
    with open("d1_input.txt", "r") as file:
        list_o_nums = [int(line) for line in file.readlines()]

    start = time.perf_counter()
    print("Solution Day 1, Part1:", end="\t")
    print(solve_part1(list_o_nums), end="\t\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")

    start = time.perf_counter()
    print("Solution Day 1, Part2:", end="\t")
    print(solve_part2(list_o_nums), end="\t\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")


if __name__ == "__main__":
    main()
