from collections import defaultdict

from util import read_file_into_list


def run():
    input_lines = read_file_into_list("../inputs/day13.txt")
    dots = defaultdict(lambda: defaultdict(int))
    instructions = list()
    for line in input_lines:
        if line == '':
            continue
        if line.startswith("fold"):
            (direction, line) = line.split(" ")[-1].split("=")
            instructions.append((direction, int(line)))
        else:
            x, y = line.split(',')
            dots[int(x)][int(y)] = 1

    for instruction in instructions:
        direction, line = instruction
        dots = fold(line, dots, direction)
        total = 0
        for key in dots.keys():
            total += sum(dots[key].values())

        print(f"Number of visible dots after this fold: {total}")

    visualize(dots)


def fold(line, dots, direction="x"):
    n_cols, n_rows = get_shape(dots)

    if direction == "y":
        for i in range(n_cols + 1):
            for j in range(line + 1, n_rows + 1):
                if dots[i][j] == 1:
                    dots[i][2 * line - j] = 1
                dots[i][j] = 0
    else:
        for i in range(line + 1, n_cols + 1):
            for j in range(n_rows + 1):
                if dots[i][j] == 1:
                    dots[2 * line - i][j] = 1
                dots[i][j] = 0

    return dots


def get_shape(dots):
    n_cols = max(dots.keys())
    n_rows = 0
    for x in dots.keys():
        val = max(dots[x].keys())
        if val > n_rows:
            n_rows = val
    return n_cols, n_rows


def visualize(dots):
    n_cols, n_rows = get_shape(dots)

    with open("vis.txt", "w") as f:
        for y in range(n_rows):
            for x in range(n_cols):
                if dots[x][y] == 1:
                    f.write("#")
                else:
                    f.write(" ")
            f.write("\n")


if __name__ == "__main__":
    run()
