def get_num_guesses(length: int) -> int:
    result = 0
    for i in range(1, length + 1):
        result += 26 ** i
    return result


run_cases = [
    (1, 26),
    (2, 702),
    (3, 18278),
]

submit_cases = run_cases + [
    (4, 475254),
    (5, 12356630),
    (6, 321272406),
    (7, 8353082582),
    (8, 217180147158),
    (9, 5646683826134),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    result = get_num_guesses(input)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False