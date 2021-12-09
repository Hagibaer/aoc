import math

from util import read_file_into_list


def run():
    input_lines = read_file_into_list("../inputs/day9.txt")
    low_points = []
    low_point_indices = []
    for i, row in enumerate(input_lines):
        for j, val in enumerate(row):

            if i - 1 < 0:
                top = 9
            else:
                top = input_lines[i - 1][j]
            if j - 1 < 0:
                left = 9
            else:
                left = input_lines[i][j - 1]
            if j + 1 >= len(row):
                right = 9
            else:
                right = input_lines[i][j + 1]
            if i + 1 >= len(input_lines):
                bottom = 9
            else:
                bottom = input_lines[i + 1][j]

            if any(int(x) < int(val) for x in [top, left, right, bottom]):
                continue
            else:
                if int(val) == 9:
                    continue
                low_points.append(val)
                low_point_indices.append((i, j))

    print(sum([int(x) + 1 for x in low_points]))

    basin_sizes = list()
    for low_point in low_point_indices:
        basin_members = [low_point]
        seen = set()
        seen.add(low_point)
        for (i, j) in basin_members:

            if i - 1 < 0:
                top = 9
            else:
                top = input_lines[i - 1][j]
                if int(top) != 9 and (i-1, j) not in seen:
                    basin_members.append((i-1, j))
                    seen.add((i-1, j))

            if j - 1 < 0:
                left = 9
            else:
                left = input_lines[i][j - 1]
                if int(left) != 9 and (i, j-1) not in seen:
                    basin_members.append((i, j - 1))
                    seen.add((i, j - 1))

            if j + 1 >= len(input_lines[i]):
                right = 9
            else:
                right = input_lines[i][j + 1]
                if int(right) != 9 and (i, j+1) not in seen:
                    basin_members.append((i, j + 1))
                    seen.add((i, j + 1))

            if i + 1 >= len(input_lines):
                bottom = 9
            else:
                bottom = input_lines[i + 1][j]
                if int(bottom) != 9 and (i + 1, j) not in seen:
                    basin_members.append((i + 1, j))
                    seen.add((i + 1, j))
        basin_sizes.append(len(basin_members))

    tmp = []
    for i in range(3):
        tmp.append(basin_sizes.pop(basin_sizes.index(max(basin_sizes))))

    print(math.prod(tmp))


if __name__ == "__main__":
    run()
