from lessons.Ch12.hashmap import HashMap


run_cases = [
    (
        2,
        [
            ("Billy Beane", "General Manager"),
            ("Peter Brand", "Assistant GM"),
        ],
        [(False, None), (False, None)],
    ),
    (
        3,
        [
            ("Art Howe", "Manager"),
            ("Ron Washington", "Coach"),
            ("David Justice", "Designated Hitter"),
        ],
        [(False, None), (False, None), (False, None)],
    ),
]

submit_cases = run_cases + [
    (
        2,
        [
            ("Paul DePodesta", "Analyst"),
            ("Ron Washington", "Coach"),
            ("Chad Bradford", "Pitcher"),
        ],
        [
            (False, None),
            (False, None),
            (True, "hashmap is full"),
        ],
    )
]


def test(size, items, errors):
    hm = HashMap(size)
    print("=====================================")
    inserted_items = {}
    for (key, val), (error_expected, expected_error_message) in zip(items, errors):
        print(f"Inserting ({key}, {val})...")
        try:
            hm.insert(key, val)
            if error_expected:
                print(
                    f"Expected error '{expected_error_message}' but insertion succeeded."
                )
                print("Fail")
                return False
            else:
                inserted_items[key] = val
        except Exception as e:
            if error_expected:
                if str(e) == expected_error_message:
                    print(f"Expected error occurred: {e}")
                else:
                    print(
                        f"Error occurred, but message '{e}' does not match expected '{expected_error_message}'."
                    )
                    print("Fail")
                    return False
            else:
                print(f"Unexpected error occurred during insertion: {e}")
                print("Fail")
                return False
    for key, expected_val in inserted_items.items():
        print(f"Getting {key}...")
        try:
            actual_val = hm.get(key)
            print(f"Expected: {expected_val}, Actual: {actual_val}")
            if actual_val != expected_val:
                print("Fail")
                return False
        except Exception as e:
            print(f"Error getting {key}: {e}")
            print("Fail")
            return False
    print("Pass")
    return True