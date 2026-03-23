def decayed_followers(initial_followers: int, fraction_lost_daily: float, days: int) -> float:
    return initial_followers * (1 - fraction_lost_daily) ** days

run_cases = [
    (200, 0.5, 1, 100),
    (200, 0.4, 2, 72),
    (200, 0.05, 3, 171),
]

submit_cases = run_cases + [
    (1000, 0.005, 2, 990),
    (1000, 0.05, 3, 857),
    (1200, 0.55, 8, 2),
    (1200, 0.09, 16, 265),
    (0, 0.5, 1, 0),
    (100, 0, 5, 100),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * initial_followers: {input1}")
    print(f" * fraction_lost_daily: {input2}")
    print(f" * days: {input3}")
    result = round(decayed_followers(input1, input2, input3))
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False