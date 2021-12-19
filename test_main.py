from main import Numoperator
from random import randint
import pytest
from time import perf_counter
import os


def prepare():
    nums = [randint(-100, 100) for _ in range(randint(1, 30))]
    oper = Numoperator('')
    oper.nums = nums
    return oper, nums


def get_time(func: callable):
    t0 = perf_counter()
    func()
    t1 = perf_counter()
    return t1 - t0


def test_get_max():
    for _ in range(10):
        oper, nums = prepare()
        assert oper.get_max() == max(nums)


def test_get_min():
    for _ in range(10):
        oper, nums = prepare()
        assert oper.get_min() == min(nums)


def test_get_sum():
    for _ in range(10):
        oper, nums = prepare()
        assert oper.get_sum() == sum(nums)


def test_get_comp():
    for _ in range(10):
        oper, nums = prepare()
        res = 1
        for num in nums:
            res *= num
        assert oper.get_comp() == res


def test_speed():
    filename = f"{randint(1000, 1000000)}.txt"
    print("названиефункции(): время")
    for i in range(100, 100101, 10000):
        with open(filename, "w+") as f:
            nums = [str(randint(1, 1000)) for _ in range(i)]
            file_str = " ".join(nums)
            f.write(file_str)
        oper = Numoperator(filename)
        test_time = []
        for func in [oper.start, oper.get_max, oper.get_min, oper.get_sum, oper.get_comp]:
            test_time.append(get_time(func))
        print(f"Кол-во чисел: {i}. start(): {test_time[0]}, get_max(): {test_time[1]}, get_min(): {test_time[2]}, "
              f"get_sum(): {test_time[3]}, get_comp(): {test_time[4]}")

    if os.path.isfile(filename):
        os.remove(filename)
    else:
        print("Такого файла нет.")


if __name__ == '__main__':
    test_speed()
    test_get_max()
    test_get_min()
    test_get_comp()
    test_get_sum()
