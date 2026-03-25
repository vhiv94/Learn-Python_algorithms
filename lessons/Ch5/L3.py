## O(n^2)
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)

def fib(n: int) -> int:
    if n <= 1:
        return n
    grandparent: int = 0
    parent: int = 1
    current: int = 1
    for _ in range(n - 1):
        current = parent + grandparent
        grandparent = parent
        parent = current
    return current


run_cases = [
    (1, 1),
    (10, 55),
    (20, 6765),
]

submit_cases = run_cases + [
    (0, 0),
    (40, 102334155),
    (70, 190392490709135),
    (160, 1226132595394188293000174702095995),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expected:  {expected_output}")
    result = fib(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False