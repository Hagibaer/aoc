# Note: Thats slow, don't use it for task two
def spawn_new_latern():
    return Lanternfish(days_left=8)


class Lanternfish:
    def __init__(self, days_left):
        self.days_left = days_left

    def count_one_day(self):
        if self.days_left == 0:
            self.days_left = 6
        else:
            self.days_left -= 1

    def __len__(self):
        return 1


def run():
    input_lines = [2,5,3,4,4,5,3,2,3,3,2,2,4,2,5,4,1,1,4,4,5,1,2,1,5,2,1,5,1,1,1,2,4,3,3,1,4,2,3,4,5,1,2,5,1,2,2,5,2,4,4,1,4,5,4,2,1,5,5,3,2,1,3,2,1,4,2,5,5,5,2,3,3,5,1,1,5,3,4,2,1,4,4,5,4,5,3,1,4,5,1,5,3,5,4,4,4,1,4,2,2,2,5,4,3,1,4,4,3,4,2,1,1,5,3,3,2,5,3,1,2,2,4,1,4,1,5,1,1,2,5,2,2,5,2,4,4,3,4,1,3,3,5,4,5,4,5,5,5,5,5,4,4,5,3,4,3,3,1,1,5,2,4,5,5,1,5,2,4,5,4,2,4,4,4,2,2,2,2,2,3,5,3,1,1,2,1,1,5,1,4,3,4,2,5,3,4,4,3,5,5,5,4,1,3,4,4,2,2,1,4,1,2,1,2,1,5,5,3,4,1,3,2,1,4,5,1,5,5,1,2,3,4,2,1,4,1,4,2,3,3,2,4,1,4,1,4,4,1,5,3,1,5,2,1,1,2,3,3,2,4,1,2,1,5,1,1,2,1,2,1,2,4,5,3,5,5,1,3,4,1,1,3,3,2,2,4,3,1,1,2,4,1,1,1,5,4,2,4,3]
    lanterns = [Lanternfish(x) for x in input_lines]
    tmp = []

    for day in range(80):
        for lanternfish in lanterns:
            if lanternfish.days_left == 0:
                tmp.append(spawn_new_latern())
            lanternfish.count_one_day()
        lanterns.extend(tmp)
        tmp = []
    print(len(lanterns))


if __name__ == "__main__":
    run()




