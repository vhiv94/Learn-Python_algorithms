def exponential_growth(n: int, factor: int, days: int) -> list[int]:
    return list(map(lambda i: n * factor ** (i), range(days + 1)))


run_cases = [
    (10, 2, 4, [10, 20, 40, 80, 160]),
    (0, 2, 2, [0, 0, 0]),
    (20, 2, 6, [20, 40, 80, 160, 320, 640, 1280]),
]

submit_cases = run_cases + [
    (30, 3, 3, [30, 90, 270, 810]),
    (
        40,
        10,
        10,
        [
            40,
            400,
            4000,
            40000,
            400000,
            4000000,
            40000000,
            400000000,
            4000000000,
            40000000000,
            400000000000,
        ],
    ),
    (10, 5, 0, [10]),
    (1, 1, 5, [1, 1, 1, 1, 1, 1]),
]


def test(n, factor, days, expected):
    print("-" * 40)
    print(f"Inputs: \nn: {n}, factor: {factor}, days: {days}")
    print(f"Expected: {expected}")
    result = exponential_growth(n, factor, days)
    print(f"Actual:   {result}")
    if result == expected:
        print("Pass")
        return True
    print("Fail")
    return False