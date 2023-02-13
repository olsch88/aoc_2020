import time
import numpy as np

char_map = {".": 0, "L": 1, "#": 2}


def get_layout(data: list[str]) -> np.ndarray:
    layout = np.zeros((len(data) + 2, len(data[0]) + 2), dtype=np.int8)
    for y, line in enumerate(data, start=1):
        for x, seat in enumerate(line, start=1):
            layout[y, x] = char_map[seat]
    return layout


def get_neibours(grid: np.ndarray) -> dict:
    neigbours: dict[tuple, list] = {}
    neig_x = []
    neig_y = []
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            neigbours[(y, x)] = []
            if x > 0:
                neigbours[(y, x)].append((y, x - 1))
    return neigbours


def process_step(layout: np.ndarray) -> np.ndarray:
    old_layout = np.copy(layout)
    empty_seatsy, empty_seatsx = np.where(old_layout == 1)
    for y, x in zip(empty_seatsy, empty_seatsx):
        count_full = np.sum(
            np.where(old_layout[y - 1 : y + 2, x - 1 : x + 2] == 2, 1, 0)
        ) - np.sum(np.where(old_layout[y, x] == 2, 1, 0))
        if count_full == 0:
            layout[y, x] = 2
    occupied_seatsy, occupied_seatsx = np.where(old_layout == 2)
    for y, x in zip(occupied_seatsy, occupied_seatsx):
        count_full = np.sum(
            np.where(old_layout[y - 1 : y + 2, x - 1 : x + 2] == 2, 1, 0)
        ) - np.sum(np.where(old_layout[y, x] == 2, 1, 0))

        if count_full >= 4:
            layout[y, x] = 1
    return layout


def solve_part1(data: list[str]) -> int:
    layout = get_layout(data)
    count = 0
    while True:
        old_layout = layout.copy()

        layout = process_step(layout)

        if np.all(layout == old_layout):
            return np.sum(np.where(layout == 2, 1, 0))


def solve_part2(data: list[str]) -> int:
    return 0


def get_data(filename: str):
    with open(filename, "r") as file:
        data = [line.strip() for line in file.readlines()]
    return data


def main():
    data = get_data("d11_input.txt")

    start = time.perf_counter()
    print("Solution Day 11, Part1:", end="\t")
    print(solve_part1(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")

    start = time.perf_counter()
    print("Solution Day 11, Part2:", end="\t")
    print(solve_part2(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")


if __name__ == "__main__":
    main()
