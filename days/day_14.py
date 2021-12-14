from collections import Counter, defaultdict

from tqdm import tqdm

from util import read_file_into_list


def run():
    input_lines = read_file_into_list("../inputs/day14.txt")
    starting_polymer = input_lines[0]

    pair_counts = defaultdict(int)
    for l, r in zip(starting_polymer, starting_polymer[1:]):
        pair_counts[l + r] += 1

    rules = dict()
    for line in input_lines[2:]:
        key, val = line.split("->")
        rules[key.strip()] = val.strip()

    element_counts = defaultdict(int)
    for pair in pair_counts:
        l, r = pair
        element_counts[l] += 1
        element_counts[r] += 1

    for i in range(40):
        diff = defaultdict(int)
        for rule in rules:
            if pair_counts[rule] > 0:
                l, r = rule
                inserted_char = rules[rule]
                diff[rule] -= pair_counts[rule]
                diff[l+inserted_char] += pair_counts[rule]
                diff[inserted_char+r] += pair_counts[rule]

                element_counts[inserted_char] += pair_counts[rule]
        for d in diff:
            pair_counts[d] += diff[d]

    values = sorted(element_counts.values())
    print(values[-1] - values[0] + 1)
    print(max(element_counts.values()) - min(element_counts.values()) + 1)


if __name__ == "__main__":
    run()
