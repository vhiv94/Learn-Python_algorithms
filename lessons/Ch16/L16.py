import math


def prime_factors(n: int) -> list[int]:
    result = []
    while n % 2 == 0:
        n /= 2
        result.append(2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n /= i
            result.append(i)
    if n > 2:
        result.append(int(n))
    return result

# prime_factors(8)
# prime_factors(24)
# prime_factors(513)
# prime_factors(1999)

run_cases = [(8, [2, 2, 2]), (10, [2, 5]), (24, [2, 2, 2, 3]), (13, [13])]

submit_cases = run_cases + [
    (49, [7, 7]),
    (77, [7, 11]),
    (4, [2, 2]),
    (64, [2, 2, 2, 2, 2, 2]),
    (63, [3, 3, 7]),
    (36, [2, 2, 3, 3]),
    (27, [3, 3, 3]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    result = prime_factors(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False