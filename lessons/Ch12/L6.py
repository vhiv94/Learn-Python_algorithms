from lessons.Ch12.hashmap import HashMap
from lessons.Ch12.users import User


run_cases = [
    (
        512,
        [User(1, 30, "Engineer"), User(2, 25, "Designer")],
        [
            ("Ricky#1", User(1, 30, "Engineer")),
            ("Shelley#2", User(2, 25, "Designer")),
            ("FakeyFaker#2", None),
        ],
    ),
]

submit_cases = run_cases + [
    (
        1028,
        [User(4, 36, "Clerk"), User(5, 29, "Chef"), User(6, 55, "Pilot")],
        [
            ("George#4", User(4, 36, "Clerk")),
            ("John#5", User(5, 29, "Chef")),
            ("Blake#1", None),
        ],
    ),
]


def test(size, users, expected_hashmap):
    print("---------------------------------")
    print("Inputs:")
    print(f" * HashMap size: {size}")
    hm = HashMap(size)
    for user in users:
        hm.insert(user.user_name, user)
        print(f"   * Inserted ({user.user_name}, {user})")

    passes = True
    for user_name, expected in expected_hashmap:
        try:
            result = hm.get(user_name)
            if expected is None:
                print(f"Get {user_name}: Fail")
                print("   * Expect exception: sorry, key not found")
                print(f"   * Actual: {result}")
                passes = False
            elif result == expected:
                print(f"Get {user_name}: Pass")
            else:
                print(f"Get {user_name}: Fail")
                print(f"   * Expect: {expected}")
                print(f"   * Actual: {result}")
                passes = False
        except Exception as e:
            actualErr = str(e)
            expectedErr = "sorry, key not found"

            if expected is not None:
                print(f"Get {user_name}: Fail")
                print(f"   * Expect: {expected}")
                print(f"   * Actual: exception: {actualErr}")
                passes = False
            elif actualErr == expectedErr:
                print(f"Get {user_name}: Pass")
            else:
                print(f"Get {user_name}: Fail")
                print(f"   * Expect exception: {expectedErr}")
                print(f"   * Actual exception: {actualErr}")
                passes = False

    if passes:
        print("Pass")
        return True
    print("Fail")
    return False