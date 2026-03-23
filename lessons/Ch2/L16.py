def average_followers(nums: list[int]) -> float:
    if not nums:
        return None
    return sum(nums)/len(nums)

run_cases = [
    ([1], 1),
    ([1, 2, 3, 4, 5, 6, 7], 4),
    ([12, 12, 12], 12),
    ([], None),
]

submit_cases = run_cases + [
    ([0], 0),
    ([100, 200, 300, 400, 500], 300),
    ([5, 10, 200, 3000, 5000], 1643),
    ([12_345, 618_222, 58_832_221, 2_180_831_475, 8_663_863_102], 2_180_831_473),
]


def test(input1, expected_output):
    try:
        print("---------------------------------")
        print(f"Inputs:")
        print(f" * nums: {input1}")
        print(f"Expected: {expected_output}")
        result = average_followers(input1)
        if expected_output is not None:
            result = int(result)
        print(f"Actual:   {result}")
        if result == expected_output:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print("Fail")
        print(e)
        return False