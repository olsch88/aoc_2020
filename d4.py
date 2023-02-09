import time


def get_passport_data(data: list[str]):
    passports: list[dict] = []

    passport: dict[str, str] = {}
    for line in data:
        if line == "\n":
            passports.append(passport)
            passport: dict[str, str] = {}

        parts = line.split()
        for part in parts:
            passport[part.split(":")[0]] = part.split(":")[1]

    passports.append(passport)

    return passports


def is_passport_valid_part1(passport: dict) -> bool:
    keys = passport.keys()
    if len(keys) == 8:
        return True
    if len(keys) == 7 and "cid" not in keys:
        return True
    return False


def is_passport_valid_part2(passport: dict[str, str]) -> bool:
    if not is_passport_valid_part1(passport):
        return False
    # print(passport)
    if len(passport["byr"]) != 4:
        return False
    if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
        # print("invalid byr")
        return False
    if len(passport["iyr"]) != 4:
        return False
    if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
        # print("invalid iyr")
        return False
    if len(passport["eyr"]) != 4:
        return False
    if int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
        # print("invalid eyr")
        return False
    hgt = passport["hgt"]
    if hgt[-2:] == "in":

        if int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76:
            # print(hgt)
            # print(f"invalid hgt in: {int(hgt[:-2])} ")
            return False
    elif hgt[-2:] == "cm":
        if int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193:
            # print(f"invalid hgt cm: {int(hgt[:-2])} ")
            return False
    else:
        return False
    if passport["hcl"][0] != "#":
        return False
    if len(passport["hcl"][1:]) != 6:
        return False
    if not all(ch in "0123456789abcdef" for ch in passport["hcl"][1:]):
        print("invalid hcl")
        return False
    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        # print("invalid hcl")
        return False
    if len(passport["pid"]) != 9 or not passport["pid"].isnumeric():
        # print("invalid pid")
        return False
    return True


def solve_part1(data: list[str]) -> int:
    passports = get_passport_data(data)

    return sum([is_passport_valid_part1(pp) for pp in passports])


def solve_part2(data: list[str]) -> int:
    passports = get_passport_data(data)

    return sum([is_passport_valid_part2(pp) for pp in passports])


def get_data(filename: str):
    with open(filename, "r") as file:
        data = [line for line in file.readlines()]
    return data


def main():
    data = get_data("d4_input.txt")

    start = time.perf_counter()
    print("Solution Day 4, Part1:", end="\t")
    print(solve_part1(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")

    start = time.perf_counter()
    print("Solution Day 4, Part2:", end="\t")
    print(solve_part2(data), end="\t")
    print(f"Runtime: {time.perf_counter()-start:.3f} ")


if __name__ == "__main__":
    main()
