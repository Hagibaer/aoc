from collections import Counter
from util import read_file_into_list


def run():
    input_lines = read_file_into_list("../inputs/day8.txt")
    codes = [x.split('|')[1].strip() for x in input_lines]
    patterns = [x.split('|')[0].strip() for x in input_lines]
    output_vals = [x.split(' ') for x in codes]
    lengths = [len(item) for sublist in output_vals for item in sublist]
    c = Counter(lengths)
    maps = [deduce_map(x.split(' ')) for x in patterns]
    print(f"Task 1: {c[2] + c[3] + c[4] + c[7]}")
    print(f"Task 2: {sum([derive_number(values, num_map) for values, num_map in zip(output_vals, maps)])}")


def derive_number(patterns, n_map):
    n = [n_map["".join(sorted(k))] for k in patterns]
    return int("".join(map(str, n)))


def deduce_map(signal_patterns):
    map = dict()
    for item in signal_patterns:
        # First get trivial ones
        if len(item) == 2:
            map[1] = item
        if len(item) == 4:
            map[4] = item
        if len(item) == 3:
            map[7] = item
        if len(item) == 7:
            map[8] = item

    for item in signal_patterns:
        if len(item) == 5:
            if set(map[1]).issubset(item):
                map[3] = item
            elif set(map[4]).difference(set(map[1])).issubset(item):
                map[5] = item
            else:
                map[2] = item

        if len(item) == 6:
            if set(map[1]).issubset(item) and set(map[4]).issubset(item):
                map[9] = item
            elif not set(map[1]).issubset(item):
                map[6] = item
            else:
                map[0] = item

    return {''.join(sorted(pattern)): number for number, pattern in map.items()}


if __name__ == "__main__":
    run()
