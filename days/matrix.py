from typing import List


def _derive_columns(rows: List[List[int]]) -> List[List[int]]:
    col1 = list()
    col2 = list()
    col3 = list()
    col4 = list()
    col5 = list()

    for row in rows:
        col1.append(row[0])
        col2.append(row[1])
        col3.append(row[2])
        col4.append(row[3])
        col5.append(row[4])
    return [col1, col2, col3, col4, col5]


class Matrix:

    def __init__(self, rows: List[List[int]]):
        self.rows = rows
        self.columns = _derive_columns(rows)
        self.hits = dict()
        self.has_won = False
        self.winning_score = 0

    def mark_shot(self, number) -> None:
        marked_shot = False

        for i, row in enumerate(self.rows):
            if marked_shot:
                break
            for j, value in enumerate(row):
                if value == number:
                    self.hits[(i, j)] = True
                    marked_shot = True
                    if not self.has_won:
                        self.has_won = self.check_win(i, j)

                    if self.has_won:
                        self.winning_score = self.calculate_winning_score(number)
                    break

    def check_win(self, i, j) -> bool:
        row_indices = [(i, x) for x in range(5)]
        col_indices = [(x, j) for x in range(5)]

        row_shots = [self.hits.get(x, False) for x in row_indices]
        col_shots = [self.hits.get(x, False) for x in col_indices]

        if all(row_shots) or all(col_shots):
            return True

        return False

    def calculate_winning_score(self, number):
        hit_indicies = [x for x in self.hits.keys() if self.hits.get(x, False)]
        hit_values = [self.rows[x[0]][x[1]] for x in hit_indicies]
        return (sum([sum(x) for x in self.rows]) - sum(hit_values)) * number


if __name__ == '__main__':
    rows = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    m = Matrix(rows)
    print(m.columns)
    m.mark_shot(1)
    m.mark_shot(6)
    m.mark_shot(11)
    m.mark_shot(16)
    print(m.has_won)
    m.mark_shot(21)
    print(m.has_won)
    print(m.winning_score)