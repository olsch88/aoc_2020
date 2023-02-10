import time
from itertools import permutations


def is_sum_of_numbers(int_to_check: int, numbers: list[int]) -> bool:
    pairs = permutations(numbers, 2)
    for i, j in pairs:
        if i + j == int_to_check:
            return True
    return False


def solve_part1(data: list[int]) -> int:
    window_length = 25  # 5 for sample, 25 for input
    for i in range(window_length, len(data)):
        if not is_sum_of_numbers(data[i], data[i - window_length : i]):
            return data[i]
    return 0


def solve_part2(data: list[int]) -> int:
    target_value = solve_part1(data)
    for i in range(len(data)):
        for width in range(len(data) - i):
            if sum(data[i : i + width]) == target_value:
                return max(data[i : i + width]) + min(data[i : i + width])
    return 0


def get_data(filename: str) -> list[int]:
    with open(filename, "r") as file:
        data = [int(line) for line in file.readlines()]
    return data


def main():
    data = get_data("d9_input.txt")

    start = time.perf_counter()
    print("Solution Day 9, Part1:", end="\t")
    print(solve_part1(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")

    start = time.perf_counter()
    print("Solution Day 9, Part2:", end="\t")
    print(solve_part2(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")


if __name__ == "__main__":
    main()
