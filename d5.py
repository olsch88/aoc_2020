import time

row_to_bin = {"B": 1, "F": 0}
col_to_bin = {"R": 1, "L": 0}


def convert_row_to_binary(row: str) -> int:
    bin_str = ""
    for c in row:
        bin_str += str(row_to_bin[c])
    num = int(bin_str, base=2)

    return num


def convert_col_to_binary(col: str) -> int:
    bin_str = ""
    for c in col:
        bin_str += str(col_to_bin[c])
    num = int(bin_str, base=2)

    return num


def get_id(b_pass: str) -> int:
    return convert_row_to_binary(b_pass[:7]) * 8 + convert_col_to_binary(b_pass[7:])


def solve_part1(data: list[str]) -> int:
    id_max = 0
    for boarding_pass in data:
        id_value = get_id(boarding_pass)
        id_max = max(id_max, id_value)

    return id_max


def solve_part2(data: list[str]) -> int:
    ids = []
    for boarding_pass in data:
        ids.append(get_id(boarding_pass))
    for i in range(min(ids), max(ids)):
        if i not in ids:
            return i
    return 0


def get_data(filename: str):
    with open(filename, "r") as file:
        data = [line.strip() for line in file.readlines()]
    return data


def main():
    data = get_data("d5_input.txt")

    start = time.perf_counter()
    print("Solution Day 5, Part1:", end="\t")
    print(solve_part1(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")

    start = time.perf_counter()
    print("Solution Day 5, Part2:", end="\t")
    print(solve_part2(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")


if __name__ == "__main__":
    main()
