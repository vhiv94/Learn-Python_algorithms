from functools import reduce


def find_minimum(nums: list[float]) -> float:
    if nums == []:
        return None
    return reduce(lambda min, elem: elem if elem < min else min, nums, float("inf"))


run_cases = [
    ([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 1),
    ([12, 12, 12], 12),
    ([10, 200, 3000, 5000, 4], 4),
]

submit_cases = run_cases + [
    ([1], 1),
    ([1, 2, 3, 4, 5], 1),
    ([5, 4, 3, 2, 1], 1),
    ([100, 200, 300, 400, 500], 100),
    ([500, 400, 300, 200, 100], 100),
    ([], None),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = find_minimum(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False