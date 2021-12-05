from util import read_matrix_input


def run():
    part_1()
    part_2()


def part_1():
    shots, matrices = read_matrix_input("../inputs/day4.txt")
    found_winner = False
    for shot in shots:
        if not found_winner:
            for matrix in matrices:
                matrix.mark_shot(shot)
                if matrix.has_won:
                    found_winner = True
                    print(f"Winning Score {matrix.winning_score}")
                    break


def part_2():
    shots, matrices = read_matrix_input("../inputs/day4.txt")
    last_winner = None
    for shot in shots:
        for matrix in matrices:
            if matrix.has_won:
                continue

            matrix.mark_shot(shot)
            if matrix.has_won:
                last_winner = matrix

    print(f"Last winner score: {last_winner.winning_score}")


if __name__ == "__main__":
    run()
