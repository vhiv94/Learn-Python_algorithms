from functools import reduce


def num_possible_orders(num_posts: int) -> int:
    result: int = 1
    for i in range(num_posts, 0, -1):
        result *= i
    return result


run_cases = [(2, 2), (3, 6), (5, 120)]

submit_cases = run_cases + [
    (1, 1),
    (6, 720),
    (7, 5040),
    (8, 40320),
    (9, 362880),
    (11, 39916800),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * num_posts: {input1}")
    result = num_possible_orders(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False