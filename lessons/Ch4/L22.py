def selection_sort(arr: list[int]) -> None:
    for i in range(len(arr)):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]

run_cases = [
    ([5, 3, 8, 6, 1, 9], [1, 3, 5, 6, 8, 9]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
]

submit_cases = run_cases + [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([15, 12, 8, 7, 5, 3, 1], [1, 3, 5, 7, 8, 12, 15]),
    ([10, 5, 3, 7, 2, 8, 1], [1, 2, 3, 5, 7, 8, 10]),
    ([], []),
    ([1], [1]),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input}")
    print(f"Expected: {expected_output}")
    selection_sort(input)
    print(f"Actual:   {input}")
    if input == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False