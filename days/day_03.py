from util import read_file_into_list
from collections import Counter


def run():
    input_lines = read_file_into_list("../inputs/day3.txt")
    gamma_rate, epsilon_rate = get_part_1_rates(input_lines)

    print(gamma_rate)
    print(epsilon_rate)
    print(f"Puzzle solution: {gamma_rate * epsilon_rate}")

    oxygen = get_part_2_rates(input_lines, mode="oxygen")
    co2 = get_part_2_rates(input_lines, mode="co2")
    print(f"Oxygen {oxygen}\nCO2: {co2}")
    print(f"Product: {oxygen * co2}")


def get_part_1_rates(l):
    gamma_rate = list()
    for i in range(len(l[0])):
        gamma_rate.append(filter_bit(l, i, "oxygen"))
    epsilon_rate = ["0" if x == "1" else "1" for x in gamma_rate]

    return int("".join(gamma_rate), 2), int("".join(epsilon_rate), 2)


def get_part_2_rates(l, start_position=0, mode="oxygen") -> int:
    search_bit = filter_bit(l, position=start_position, mode=mode)
    new_list = keep_bits(l, search_bit, start_position)
    if len(new_list) == 1:
        return int(new_list[0], 2)
    else:
        return get_part_2_rates(new_list, start_position + 1, mode)


def filter_bit(l, position, mode="oxygen") -> str:
    position_bits = "".join([x[position] for x in l])
    c = Counter(position_bits)

    if c.get("1") == c.get("0"):
        if mode == "oxygen":
            return "1"
        else:
            return "0"

    if mode == "oxygen":
        return c.most_common()[0][0]

    else:
        return c.most_common()[1][0]


def keep_bits(l, bit, position):
    keep = list()
    for val in l:
        if val[position] == bit:
            keep.append(val)
    return keep


if __name__ == "__main__":
    run()
