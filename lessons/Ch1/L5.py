from functools import reduce


def summed(nums: list[int]) -> int:
    if nums == []:
        return 0
    return reduce(lambda acc, elem: acc + elem, nums, 0)


run_cases = [([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 2686826), ([12, 12, 12], 36)]

submit_cases = run_cases + [
    ([10, 200, 3000, 5000, 4], 8214),
    ([], 0),
    ([1], 1),
    ([123456789], 123456789),
    ([-1, -2, -3], -6),
    ([0, 0, 0, 0, 0], 0),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * nums: {input1}")
    result = summed(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False