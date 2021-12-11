import itertools
from collections import defaultdict

from util import read_file_into_list


def run():
    input_lines = read_file_into_list("../inputs/day11.txt")
    octupus_map = defaultdict(lambda: defaultdict(int))
    flash_count = 0

    for i, row in enumerate(input_lines):
        for j, val in enumerate(row):
            octupus_map[i][j] = int(val)

    step = 0
    while True:
        step += 1
        seen = set()
        flash_coords = list()
        for i, row in enumerate(octupus_map.values()):
            for j, val in enumerate(row.values()):
                octupus_map[i][j] = val + 1
                if octupus_map[i][j] > 9:
                    flash_coords.append((i, j))
                    seen.add((i, j))

        for coord in flash_coords:
            i, j = coord
            all_neighbor_coords = get_neighbor_coords(i, j)
            for i_neighbor, j_neighbor in all_neighbor_coords:
                octupus_map[i_neighbor][j_neighbor] += 1
                if octupus_map[i_neighbor][j_neighbor] > 9 and not (i_neighbor, j_neighbor) in seen:
                    flash_coords.append((i_neighbor, j_neighbor))
                    seen.add((i_neighbor, j_neighbor))

        for coord in seen:
            i, j = coord
            octupus_map[i][j] = 0
            flash_count += 1

        if step == 100:
            print(f"Flash counts after 100 steps: {flash_count}")

        if len(seen) == 100:
            print(f"{step}  is the first time all flash")
            break


def get_neighbor_coords(i, j):
    x = (i - 1, i, i + 1)
    y = (j - 1, j, j + 1)
    return list(filter(lambda x: all(((0 <= val <= 9) for val in x)), itertools.product(x, y)))


if __name__ == "__main__":
    run()
