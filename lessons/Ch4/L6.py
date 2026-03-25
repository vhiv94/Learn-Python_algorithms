import time


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums
    A: list[int] = nums[:len(nums)//2]
    B: list[int] = nums[len(nums)//2:]
    A = merge_sort(A)
    B = merge_sort(B)
    return merge(A, B)


def merge(first: list[int], second: list[int]) -> list[int]:
    final: list[int] = []
    i: int = 0
    j: int = 0
    while True:
        if first[i] < second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1

        if i == len(first):
            final.extend(second[j:])
            break
        elif j == len(second):
            final.extend(first[i:])
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