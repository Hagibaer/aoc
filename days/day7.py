from util import read_file_into_list
import statistics
import functools


def run():
    input_lines = read_file_into_list("../inputs/day7.txt")
    crab_positions = list(map(int, input_lines[0].split(',')))
    median = round(statistics.median(crab_positions))
    mean = round(statistics.mean(crab_positions))
    print(functools.reduce(lambda a, b: a + b, [abs(pos - median) for pos in crab_positions]))
    lower_mean_score = functools.reduce(lambda a, b: a + b, [calc_cost(pos, mean - 1) for pos in crab_positions])
    upper_mean_score = functools.reduce(lambda a, b: a + b, [calc_cost(pos, mean) for pos in crab_positions])
    if lower_mean_score < upper_mean_score:
        print(lower_mean_score)
    else:
        print(upper_mean_score)


def calc_cost(a, b):
    if a < b:
        diff = b - a + 1
        return sum(range(1, diff))
    else:
        diff = a - b + 1
        return sum(range(1, diff))


if __name__ == "__main__":
    run()
