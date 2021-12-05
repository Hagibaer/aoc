from util import read_file_into_list


def run():
    input_lines = read_file_into_list("../inputs/day5.txt")
    diagram = dict()
    for line in input_lines:
        tmp = line.split('->')
        x1, y1 = tmp[0].strip().split(',')
        x2, y2 = tmp[1].strip().split(',')
        all_coords = generate_all_coordinates_for_line(int(x1), int(y1), int(x2), int(y2))
        for coord in all_coords:
            diagram[coord] = diagram.get(coord, 0) + 1

    num_overlapping_points = 0
    for val in diagram.values():
        if val >= 2:
            num_overlapping_points += 1

    print(f"Num overlapping points: {num_overlapping_points}")


def generate_all_coordinates_for_line(x1, y1, x2, y2):
    coords = list()
    x_coordinates, y_coordinates = None, None
    if x1 == x2:
        for val in range(min([y1, y2]), max([y1, y2]) + 1):
            coords.append((x1, val))

    if y1 == y2:
        for val in range(min([x1, x2]), max([x1, x2]) + 1):
            coords.append((val, y1))

    if x1 < x2:
        x_coordinates = list(range(x1, x2 + 1))
    elif x2 < x1:
        x_coordinates = list(range(x1, x2 - 1, -1))

    if y1 < y2:
        y_coordinates = list(range(y1, y2 + 1))
    elif y2 < y1:
        y_coordinates = list(range(y1, y2 - 1, -1))

    if x_coordinates and y_coordinates:
        coords.extend([(x, y) for x, y in zip(x_coordinates, y_coordinates)])

    return coords


if __name__ == "__main__":
    run()