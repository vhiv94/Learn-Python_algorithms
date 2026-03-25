import time


def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr


run_cases = [([4, 3, 2, 1], [1, 2, 3, 4]), ([9, 5, -3, 7], [-3, 5, 7, 9])]

submit_cases = run_cases + [
    ([], []),
    ([1], [1]),
    ([5, 3, 4, 1, 2], [1, 2, 3, 4, 5]),
    ([0, -2, -5, 3, 2, 1], [-5, -2, 0, 1, 2, 3]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expected: {expected_output}")
    start = time.time()
    result = insertion_sort(input1)
    end = time.time()
    timeout = 1.00
    if (end - start) < timeout:
        print(f"test completed in less than {timeout * 1000} milliseconds!")
        if result == expected_output:
            print(f"Actual: {result}")
            print("Pass")
            return True
        print(f"Actual: {result}")
        print("Fail")
        return False
    else:
        print(f"test took longer than {timeout * 1000} milliseconds!")
        print(f"Actual: {result}")
        print("Fail")
        return False