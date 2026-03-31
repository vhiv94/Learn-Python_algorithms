from lessons.Ch12.hashmap import HashMap
from lessons.Ch12.users import get_users


run_cases = [
    (
        8,
        get_users(2),
        [3, 6],
    ),
]

submit_cases = run_cases + [
    (
        512,
        get_users(6),
        [360, 487, 150, 458, 112, 50],
    ),
]


def test(size, users, expected_indexes):
    print("---------------------------------")
    print(f" * HashMap size: {size}")
    hm = HashMap(size)
    try:
        actual = []
        for i, user in enumerate(users):
            index = hm.key_to_index(user.user_name)
            print(f"  Expect  {user.user_name} -> {expected_indexes[i]}")
            print(f"  Actual  {user.user_name} -> {index}")
            actual.append(index)
        if actual == expected_indexes:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False