from pathlib import Path
import typing


class Numoperator:
    def __init__(self, filename: str):
        self.filename = filename
        self.nums = []

    def start(self):
        with open(self.filename, "r") as f:
            string = f.readline()
            while string != '':
                self.nums += (int(num) for num in string.split(' '))
                string = f.readline()

    def get_max(self):
        max_num = self.nums[0]
        for num in self.nums:
            if num > max_num:
                max_num = num
        return max_num

    def get_min(self):
        min_num = self.nums[0]
        for num in self.nums:
            if num < min_num:
                min_num = num
        return min_num

    def get_sum(self):
        sum = 0
        for num in self.nums:
            sum += num
        return sum

    def get_comp(self):
        comp = 1
        for num in self.nums:
            comp *= num
        return comp


if __name__ == '__main__':
    path = Path("/Users/arkhipowasilii/PycharmProjects/tz3/nums.txt")
    filename = "nums.txt"
    c = Numoperator(filename)
    c.start()
    print(c.get_comp())
    print(c.get_max())
