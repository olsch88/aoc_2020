import time
from collections import deque


def get_contents(line: str) -> tuple[str, list]:
    name: str = ""
    contents: list = []
    if "no other" in line:
        name = " ".join(line.split()[:2])
        return (name, contents)

    for i, part in enumerate(line.split(",")):
        if i == 0:
            name = " ".join(part.split()[:2])
            # print(name)
            contents.append(" ".join(part.split()[5:7]))
        else:
            contents.append(" ".join(part.split()[1:3]))
    # print(contents)
    return (name, contents)


def get_contents_with_numbers(line: str) -> tuple[str, dict]:
    name: str = ""
    contents: dict[str, int] = {}
    if "no other" in line:
        name = " ".join(line.split()[:2])
        # print(name)
        # print(contents)
        return (name, contents)

    for i, part in enumerate(line.split(",")):
        if i == 0:
            name = " ".join(part.split()[:2])
            # print(name)
            contents[" ".join(part.split()[5:7])] = int(part.split()[4])
        else:
            contents[" ".join(part.split()[1:3])] = int(part.split()[0])
    # print(contents)
    return (name, contents)


def find_shiny_bag(bag: dict) -> int:
    contents = bag.keys()
    cont: dict
    for cont in contents:
        if "shiny gold" in cont.keys():
            return 1
        else:
            for key in cont.keys():
                return find_shiny_bag(key)
    return 0


def solve_part1(data: list[str]) -> int:
    bags = {}
    for bag in data:
        name, cont = get_contents(bag)
        bags[name] = cont

    queue = deque()
    queue.append("shiny gold")
    contains_gold: set = set()

    while True:

        try:
            search_bag = queue.popleft()
        except IndexError:
            break
        for bag, contents in bags.items():
            if search_bag in contents:
                queue.append(bag)
                contains_gold.add(bag)

    return len(contains_gold)


def get_number_of_contents(bag: str, list_o_bags: dict[str, dict]) -> int:
    """This does not give the right anwer :("""

    if list_o_bags[bag] == {}:
        print(f"{bag} contains\tno other bags")
        return 1
    overall_count = 0
    sub_count = 0
    for sub_bag, count in list_o_bags[bag].items():
        sub_count += (get_number_of_contents(sub_bag, list_o_bags) * count) + 1

    print(f"{bag} contains")
    print(f"\t {sub_count} other bags")
    overall_count += sub_count
    return overall_count  # + #len(list_o_bags[bag])  # adding the bags themselfs


def get_number_of_contents_v2(bag: str, list_o_bags: dict[str, dict]) -> int:
    over_count = 0
    queue = deque()
    queue.append(bag)

    while True:
        try:
            next_bag = queue.popleft()
        except IndexError:
            break

        for sub_bag, count in list_o_bags[next_bag].items():
            over_count += count
            queue.extend([sub_bag] * count)
    return over_count


def solve_part2(data: list[str]) -> int:
    bags = {}
    for bag in data:
        name, cont = get_contents_with_numbers(bag)
        bags[name] = cont

    # count = get_number_of_contents("shiny gold", bags)
    count = get_number_of_contents_v2("shiny gold", bags)
    return count


def get_data(filename: str):
    with open(filename, "r") as file:
        data = [line.strip() for line in file.readlines()]
    return data


def main():
    data = get_data("d7_input.txt")

    start = time.perf_counter()
    print("Solution Day 7, Part1:", end="\t")
    print(solve_part1(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")

    start = time.perf_counter()
    print("Solution Day 7, Part2:", end="\t")
    print(solve_part2(data), end="\t\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")


if __name__ == "__main__":
    main()
