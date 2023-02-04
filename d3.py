def solve_part1(data: list[str]) -> int:
    forrest = get_forest(data)
    count = traverse_forrest(forrest, 3, 1)
    return count


def solve_part2(data: list[str]) -> int:
    forrest = get_forest(data)
    counts = []
    counts.append(traverse_forrest(forrest, 1, 1))
    counts.append(traverse_forrest(forrest, 3, 1))
    counts.append(traverse_forrest(forrest, 5, 1))
    counts.append(traverse_forrest(forrest, 7, 1))
    counts.append(traverse_forrest(forrest, 1, 2))
    prod = 1
    for c in counts:
        prod *= c
    return prod


def get_data(filename: str) -> list[str]:
    with open(filename, "r") as file:
        data = [line.strip() for line in file.readlines()]
    return data


def get_forest(data: list[str]) -> list:
    forrest = [[] for _ in range(len(data))]
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            forrest[y].append(char)

    return forrest


def traverse_forrest(forrest, step_x: int, step_y: int):
    x = 0
    y = 0
    width = len(forrest[0])
    tree_count = 0
    while y < len(forrest) - step_y:
        x += step_x
        x = x % width
        y += step_y
        if forrest[y][x] == "#":
            tree_count += 1

    return tree_count


def main():
    data = get_data("d3_input.txt")

    print("Solution Day 3, Part1:")
    print(solve_part1(data))

    print("Solution Day 3, Part2:")
    print(solve_part2(data))


if __name__ == "__main__":
    main()
