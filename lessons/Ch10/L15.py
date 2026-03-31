from lessons.Ch10.bst import BSTNode, print_tree
from lessons.Ch10.users import get_users


run_cases = [
    (2, 2),
    (6, 3),
]

submit_cases = run_cases + [
    (0, 0),
    (1, 1),
    (16, 7),
]


def test(num_users, expected_output):
    users = get_users(num_users)
    if not users:
        root = BSTNode()
    else:
        root = BSTNode(users[0])
        for user in users[1:]:
            root.insert(user)

    print("---------------------------------")
    print(f"Users: {[str(user) for user in users]}")
    print_tree(root)
    print(f"Expecting height: {expected_output}")
    result = root.height()
    print(f"Actual height: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False