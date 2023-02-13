import time

directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]


def get_instruction(data: list[str]) -> list[tuple[str, int]]:
    instructions: list = []
    for item in data:
        direction = item[0]
        amount = int(item[1:])
        instructions.append((direction, amount))
    return instructions


def solve_part1(data: list[str]) -> int:
    instructions = get_instruction(data)
    dire_index = 0
    pos = [0, 0]
    for instr, amount in instructions:
        if instr == "F":
            pos[0] += directions[dire_index][0] * amount
            pos[1] += directions[dire_index][1] * amount
        elif instr == "L":
            dire_index = (dire_index - amount // 90) % 4
        elif instr == "R":
            dire_index = (dire_index + amount // 90) % 4
        elif instr == "N":
            pos[1] += amount
        elif instr == "S":
            pos[1] -= amount
        elif instr == "E":
            pos[0] += amount
        elif instr == "W":
            pos[0] -= amount

    return abs(pos[0]) + abs(pos[1])


def rotate_waypoint(waypoint: list, instr: tuple) -> None:
    dire, amount = instr
    old_waypoint = waypoint.copy()
    if amount == 270:
        new_dire = "L" if dire == "R" else "R"
        dire = new_dire
        amount = 90
    if amount == 180:
        waypoint[0] = -waypoint[0]
        waypoint[1] = -waypoint[1]
    else:
        if dire == "L":
            waypoint[1] = old_waypoint[0]
            waypoint[0] = -old_waypoint[1]
        if dire == "R":
            waypoint[1] = -old_waypoint[0]
            waypoint[0] = old_waypoint[1]


def solve_part2(data: list[str]) -> int:
    instructions = get_instruction(data)
    pos = [0, 0]
    waypoint = [10, 1]
    for instr, amount in instructions:
        if instr == "F":
            pos[0] += waypoint[0] * amount
            pos[1] += waypoint[1] * amount
        elif instr == "L" or instr == "R":
            rotate_waypoint(waypoint, (instr, amount))

        elif instr == "N":
            waypoint[1] += amount
        elif instr == "S":
            waypoint[1] -= amount
        elif instr == "E":
            waypoint[0] += amount
        elif instr == "W":
            waypoint[0] -= amount

    return abs(pos[0]) + abs(pos[1])


def get_data(filename: str):
    with open(filename, "r") as file:
        data = [line.strip() for line in file.readlines()]
    return data


def main():
    data = get_data("d12_input.txt")

    start = time.perf_counter()
    print("Solution Day 12, Part1:", end="\t")
    print(solve_part1(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")

    start = time.perf_counter()
    print("Solution Day 12, Part2:", end="\t")
    print(solve_part2(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")


if __name__ == "__main__":
    main()
