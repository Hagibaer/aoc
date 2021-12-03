from util import read_file_into_list


def run():
    input_lines = read_file_into_list("../inputs/day2.txt")
    horizontal, depth = get_final_position_part_1(input_lines)
    print(horizontal * depth)
    horizontal, depth = get_final_position_part_2(input_lines)
    print(horizontal * depth)


def get_final_position_part_1(instructions):
    horizontal = 0
    depth = 0
    for line in instructions:
        action, value = line.split(" ")
        value = int(value)
        if action == 'forward':
            horizontal += value
        elif action == 'down':
            depth += value
        else:
            depth -= value
    return horizontal, depth


def get_final_position_part_2(instructions):
    horizontal = 0
    depth = 0
    aim = 0
    for line in instructions:
        action, value = line.split(" ")
        value = int(value)
        if action == 'forward':
            horizontal += value
            depth += aim * value

        elif action == 'down':
            aim += value
        else:
            aim -= value
    return horizontal, depth


if __name__ == "__main__":
    run()
