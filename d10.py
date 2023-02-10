import time
from collections import Counter


def solve_part1(data: list[int]) -> int:

    jolt_divs = [1, 3]
    for i, jolt in enumerate(data):
        if i == 0:
            continue
        jolt_divs.append(jolt - data[i - 1])
    counts = Counter(jolt_divs)
    return counts[1] * counts[3]


def solve_part2(data: list[int]) -> int:
    return 0


def get_data(filename: str):
    with open(filename, "r") as file:
        data = [int(line) for line in file.readlines()]
    data.sort()
    return data


def main():
    data = get_data("d10_input.txt")

    start = time.perf_counter()
    print("Solution Day 10, Part1:", end="\t")
    print(solve_part1(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")

    start = time.perf_counter()
    print("Solution Day 10, Part2:", end="\t")
    print(solve_part2(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")


if __name__ == "__main__":
    main()
