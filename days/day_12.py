from collections import defaultdict

from util import read_file_into_list


def run():
    input_lines = read_file_into_list("../inputs/day12.txt")
    neighbor_matrix = defaultdict(list)
    for line in input_lines:
        from_point, to_point = line.split('-')
        neighbor_matrix[from_point].append(to_point)
        # bc graph is not directed
        neighbor_matrix[to_point].append(from_point)
    print(f"Solution Part 1: {walk('start', neighbor_matrix, [], False)}")
    print(f"Solution Part 2: {walk('start', neighbor_matrix, [], True)}")


def walk(pos, caves, visited, allow_revisit_small):
    if pos == "end":
        return 1
    count = 0
    visited.append(pos)
    for c in caves[pos]:
        if c == "start":
            continue
        is_small = c.islower()
        visited_before = c in visited
        revisiting_small = is_small and visited_before
        allow_visit = not is_small or not visited_before or allow_revisit_small
        allow_revisit_small_c = allow_revisit_small and not revisiting_small
        if allow_visit:
            count += walk(c, caves, visited, allow_revisit_small_c)
    visited.pop()
    return count


if __name__ == "__main__":
    run()
