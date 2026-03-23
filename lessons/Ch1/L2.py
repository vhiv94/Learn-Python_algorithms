from functools import reduce


def find_minimum(nums: list[float]) -> float:
    return reduce(lambda min, elem: elem if elem < min else min, nums, float("inf"))

find_minimum([5, 10, -20])