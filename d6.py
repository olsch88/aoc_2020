import time


def get_groups(data: list[str]) -> list[list[str]]:
    groups = []
    new_group = []
    for line in data:
        if line == "\n":
            groups.append(new_group)
            new_group = []

        else:
            new_group.append(line.strip())
    groups.append(new_group)
    return groups


def get_group_count_any(group: list[str]) -> int:
    letters = set()
    for line in group:
        for char in line:
            letters.add(char)
    return len(letters)


def get_group_count_all(group: list[str]) -> int:
    lines = [set(line) for line in group]
    total = set(lines[0])
    for line in lines:
        total = total.intersection(line)
    return len(total)


def solve_part1(data: list[str]) -> int:
    count = 0
    groups = get_groups(data)
    for gr in groups:
        count += get_group_count_any(gr)
    return count


def solve_part2(data: list[str]) -> int:
    count = 0
    groups = get_groups(data)
    for gr in groups:
        count += get_group_count_all(gr)
    return count


def get_data(filename: str):
    with open(filename, "r") as file:
        data = [line for line in file.readlines()]
    return data


def main():
    data = get_data("d6_input.txt")

    start = time.perf_counter()
    print("Solution Day 6, Part1:", end="\t")
    print(solve_part1(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")

    start = time.perf_counter()
    print("Solution Day 6, Part2:", end="\t")
    print(solve_part2(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")


if __name__ == "__main__":
    main()
