from util import read_file_into_list
from typing import List


def run():
    input_lines = read_file_into_list("../inputs/day1.txt", to_int=True)
    num_increases = count_num_increases(input_lines)
    print(f"Num increases {num_increases}")

    new_list = to_three_window_list(input_lines)
    print(f"new list {new_list}")
    print(f"Num increases three window: {count_num_increases(new_list)}")


def count_num_increases(l: List[int]) -> int:
    n_increases = 0
    length = len(l)

    for i, val in enumerate(l):
        if i == length - 1:
            break
        if val < l[i + 1]:
            n_increases += 1
    return n_increases


def to_three_window_list(l):
    new_list = []
    length = len(l)

    for i, val in enumerate(l):
        if i == length - 2:
            break
        new_list.append(sum([val, l[i + 1], l[i + 2]]))

    return new_list
