from typing import List, Union
from days.matrix import Matrix
import re

def read_file_into_list(filepath: str, to_int: bool = False) -> List[Union[str, int]]:
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()
    if to_int:
        lines = [int(x) for x in lines]

    return lines


def read_matrix_input(filepath: str) -> List[Union[List[int], List[Matrix]]]:
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()

    shots = lines.pop(0)
    shots = [int(x) for x in shots.split(',')]

    matrices = list()
    tmp = list()

    for line in lines:
        if len(line) == 0 and len(tmp) == 5:
            matrices.append(Matrix(tmp))
            tmp = []
            continue
        elif len(line) == 0:
            continue

        line = line.strip()
        row = re.sub(' +', ',', line)
        tmp.append([int(x) for x in row.split(',')])

    matrices.append(Matrix(tmp))
    return [shots, matrices]


if __name__ == '__main__':
    shots, matrices = read_matrix_input("inputs/day4_test.txt")
    found_winner = False
    for shot in shots:
        if not found_winner:
            for matrix in matrices:
                matrix.mark_shot(shot)
                if matrix.has_won:
                    found_winner = True
                    print(f"Winning Score {matrix.winning_score}")
                    break
