def count_names(list_of_lists: list[list[str]], target_name: str) -> int:
    count: int = 0
    for lst in list_of_lists:
        for name in lst:
            if target_name == name:
                count += 1

    return count

run_cases = [
    ([["George", "Eva", "George"], ["Diane", "George", "Eva", "Frank"]], "George", 3),
    (
        [
            ["Amy", "Bob", "Candy"],
            ["Diane", "George", "Eva", "Frank"],
            ["Diane", "George"],
            ["George", "name", "George"],
        ],
        "George",
        4,
    ),
]

submit_cases = run_cases + [
    (
        [
            ["Alex", "name", "Chloe"],
            ["Eric", "name", "Fred"],
            ["Hector", "name"],
            ["Hector", "name"],
            ["Hector", "name"],
            ["George"],
        ],
        "Hector",
        3,
    ),
    (
        [
            ["Alex", "name", "Chloe"],
            ["Eric", "name", "Fred"],
            ["Hector", "name"],
            ["Hector", "name"],
            ["Hector", "name"],
            ["George"],
        ],
        "George",
        1,
    ),
    (
        [["Alex", "name", "Chloe"], ["Eric", "name", "Fred"], ["Hector", "name"]],
        "Alex",
        1,
    ),
    ([], "George", 0),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * list of lists: {input1}")
    print(f" * target name: {input2}")
    result = count_names(input1, input2)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False