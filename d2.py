import time


def solve_part1(data: list[str]) -> int:
    valid_count: int = 0
    code: str

    for line in data:
        numbers, letter, code = get_parts(line)
        if code.count(letter) >= numbers[0] and code.count(letter) <= numbers[1]:
            valid_count += 1

    return valid_count


def solve_part2(data: list[str]) -> int:
    valid_count: int = 0
    code: str
    for line in data:
        numbers, letter, code = get_parts(line)
        case1 = code[numbers[0] - 1] == letter
        case2 = code[numbers[1] - 1] == letter
        if case1 ^ case2:
            valid_count += 1

    return valid_count


def get_data(filename: str) -> list[str]:
    with open(filename, "r") as file:
        data = [line.strip() for line in file.readlines()]
    return data


def get_parts(line: str) -> tuple:
    parts = line.split()
    numbers = (int(parts[0].split("-")[0]), int(parts[0].split("-")[1]))
    letter = parts[1][:-1]
    code = parts[2]

    return (numbers, letter, code)


def main():
    data = get_data("d2_input.txt")

    start = time.perf_counter()
    print("Solution Day 2, Part1:", end="\t")
    print(solve_part1(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")

    start = time.perf_counter()
    print("Solution Day 2, Part2:", end="\t")
    print(solve_part2(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")


if __name__ == "__main__":
    main()
