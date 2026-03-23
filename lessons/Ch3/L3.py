def does_name_exist(first_names: list[str], last_names: list[str], full_name: str)  -> bool:
    for first in first_names:
        for last in last_names:
            if f"{first} {last}" == full_name:
                return True
    return False


run_cases = [
    (100, 100, "bob0 gonzalez0", True),
    (500, 500, "maria1 smith1", True),
]

submit_cases = run_cases + [
    (1000, 1000, "bob500 smith1", False),
    (2000, 2000, "bob1999 wagner1998", False),
    (3000, 3000, "sally2999 smith2998", True),
]


def test(num_fnames, num_lnames, check_name, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * num first_names: {num_fnames}")
    print(f" * num last_names: {num_lnames}")
    print(f" * looking for name: {check_name}")
    print(f"Expected: {expected_output}")
    fnames = get_first_names(num_fnames)
    lnames = get_last_names(num_lnames)
    result = does_name_exist(fnames, lnames, check_name)
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def get_first_names(num):
    names = []
    for i in range(num):
        m = i % 3
        if m == 0:
            names.append(f"bob{i}")
        elif m == 1:
            names.append(f"maria{i}")
        elif m == 2:
            names.append(f"sally{i}")
    return names


def get_last_names(num):
    names = []
    for i in range(num):
        m = i % 3
        if m == 0:
            names.append(f"gonzalez{i}")
        elif m == 1:
            names.append(f"smith{i}")
        elif m == 2:
            names.append(f"wagner{i}")
    return names