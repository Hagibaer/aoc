from util import read_file_into_list
from collections import Counter, defaultdict


def simulate_growth(init_population, days):
    for _ in range(days):
        new_population = defaultdict(int)
        for d, num_fish in init_population.items():
            d -= 1
            if d < 0:
                new_population[6] += num_fish
                new_population[8] += num_fish
            else:
                new_population[d] += num_fish
        init_population = new_population
    return sum(init_population.values())


def run():
    input_lines = read_file_into_list("../inputs/day6.txt")
    fish_counter = Counter(map(int, input_lines[0].split(',')))
    print(simulate_growth(fish_counter, 256))


if __name__ == "__main__":
    run()
