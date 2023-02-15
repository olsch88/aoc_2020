import time


def get_busses(data: str) -> list[int]:
    bus_list = []
    for part in data.split(","):
        try:
            bus_list.append(int(part))
        except ValueError:
            pass
    return bus_list


def solve_part1(data: list[str]) -> int:
    arrival = int(data[0])
    busses = get_busses(data[1])
    nearest_id = 0
    shortest_time = 999999
    for bus in busses:
        if bus - arrival % bus < shortest_time:
            shortest_time = bus - arrival % bus
            nearest_id = bus
    return nearest_id * shortest_time


def solve_part2(data: list[str]) -> int:
    return 0


def get_data(filename: str):
    with open(filename, "r") as file:
        data = [line.strip() for line in file.readlines()]
    return data


def main():
    data = get_data("d13_input.txt")

    start = time.perf_counter()
    print("Solution Day 13, Part1:", end="\t")
    print(solve_part1(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")

    start = time.perf_counter()
    print("Solution Day 13, Part2:", end="\t")
    print(solve_part2(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")


if __name__ == "__main__":
    main()
