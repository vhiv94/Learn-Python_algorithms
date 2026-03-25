import time


def merge_sort(arr: list[int]) -> list[int]:
    ## base case
    if len(arr) < 2:
        return arr
    
    ## split using recursion
    A = merge_sort(arr[:len(arr)//2])
    B = merge_sort(arr[len(arr)//2:])

    ## then merge
    final: list[int] = []
    i: int = 0
    j: int = 0
    while True:
        if A[i] < B[j]:
            final.append(A[i])
            i += 1
        else:
            final.append(B[j])
            j += 1

        if i == len(A):
            final.extend(B[j:])
            break
        elif j == len(B):
            final.extend(A[i:])
            break
    return final



run_cases = [([3, 2, 1], [1, 2, 3]), ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])]

submit_cases = run_cases + [
    ([], []),
    ([7], [7]),
    ([4, -7, 1, 0, 5], [-7, 0, 1, 4, 5]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expected: {expected_output}")
    start = time.time()
    result = merge_sort(input1)
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