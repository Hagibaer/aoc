import statistics
from collections import deque

from util import read_file_into_list

mapping = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">"
}

completion_value = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

illegal_chars_scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}


def run():
    input_lines = read_file_into_list("../inputs/day10.txt")
    violations = list()
    all_stacks = list()
    for i, line in enumerate(input_lines):
        all_stacks.append(deque())
        found_violation = False
        for char in line:
            if found_violation:
                continue
            if char in "({[<":
                all_stacks[i].append(char)
            elif char in ")}]>":
                top_symbol = all_stacks[i].pop()
                if mapping[top_symbol] != char:
                    violations.append(char)
                    found_violation = True
                    all_stacks[i] = None

    incomplete_stacks = list(filter(None, all_stacks))
    completed_stack_scores = [complete_stack_score(stack) for stack in incomplete_stacks]

    print(sum(illegal_chars_scores[x] for x in violations))
    print(statistics.median(completed_stack_scores))


def complete_stack_score(stack):
    complete = list()
    while stack:
        complete.append(mapping[stack.pop()])

    score = 0
    for char in complete:
        score *= 5
        score += completion_value[char]
    return score


if __name__ == "__main__":
    run()
