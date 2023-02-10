import time


def get_instructions(data: list[str]) -> list[tuple[str, int]]:
    instr = []
    for line in data:
        parts = line.split()
        instr.append((parts[0], int(parts[1])))
    return instr


def find_loop_acc(instructions: list[tuple[str, int]]) -> tuple[bool, int]:
    acc = 0
    pos = 0
    visited_pos = set()
    while True:
        if pos in visited_pos:
            return (False, acc)
        visited_pos.add(pos)
        try:
            order, amount = instructions[pos]
        except IndexError:  # we are at the end of the instructions
            return (True, acc)
        if order == "acc":
            acc += amount
            pos += 1
        if order == "jmp":
            pos += amount
        if order == "nop":
            pos += 1
    return (False, 0)


def solve_part1(data: list[str]) -> int:

    instructions = get_instructions(data)
    return find_loop_acc(instructions)[1]

    # return 0


def solve_part2(data: list[str]) -> int:
    instructions = get_instructions(data)
    for i, instr in enumerate(instructions):
        if instr[0] == "nop":
            instructions[i] = ("jmp", instr[1])
            found, acc = find_loop_acc(instructions)
            if found:
                return acc
            instructions[i] = ("nop", instr[1])
        if instr[0] == "jmp":
            instructions[i] = ("nop", instr[1])
            found, acc = find_loop_acc(instructions)
            if found:
                return acc
            instructions[i] = ("jmp", instr[1])
    return 0


def get_data(filename: str):
    with open(filename, "r") as file:
        data = [line.strip() for line in file.readlines()]
    return data


def main():
    data = get_data("d8_input.txt")

    start = time.perf_counter()
    print("Solution Day 8, Part1:", end="\t")
    print(solve_part1(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")

    start = time.perf_counter()
    print("Solution Day 8, Part2:", end="\t")
    print(solve_part2(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")


if __name__ == "__main__":
    main()
