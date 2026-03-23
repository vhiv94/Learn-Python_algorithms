import time


def binary_search(target: int, arr: list[int]) -> bool:
    low = 0
    high = len(arr) - 1
    while low <= high:
        median = (low + high) // 2
        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median -1
    return False

        
run_cases = [
    (10, [i for i in range(200)], True),
    (-1, [i for i in range(20000)], False),
]

submit_cases = run_cases + [
    (15, [], False),
    (0, [0], True),
    (-1, [-2, -1], True),
    (105028, [i for i in range(2000000)], True),
    (2000001, [i for i in range(2000000)], False),
]


def test(target, arr, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * target: {target}")
    print(f" * arr length: {len(arr)} items")
    print(f"Expected:  {expected_output} & completed in less than 50 milliseconds")
    start = time.time()
    result = binary_search(target, arr)
    end = time.time()
    timeout = 0.05
    if (end - start) < timeout:
        print(f"binary_search completed in less than {timeout * 1000} milliseconds!")
        if result == expected_output:
            print(f"Actual: {result}")
            print("Pass")
            return True
        else:
            print(f"Actual: {result}")
            print("Fail")
            return False
    else:
        print(
            f"binary_search took too long ({(end - start) * 1000} milliseconds). Speed it up!"
        )
        print(f"Actual: {result}")
        print("Fail")
        return False