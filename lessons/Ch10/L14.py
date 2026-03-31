from lessons.Ch10.bst import BSTNode
from lessons.Ch10.users import get_users, User


def populate_tree(nodes):
    if not nodes:
        return None
    tree = BSTNode(nodes[0])
    for node in nodes[1:]:
        tree.insert(node)
    return tree


run_cases = [
    (5, True),
    (3, False),
]

submit_cases = run_cases + [
    (1, True),
    (21, False),
    (17, True),
    (7, True),
]


def test(val_to_check, expected_output):
    print("---------------------------------")
    users = get_users(11)
    tree = populate_tree(users)
    user_to_find = User(val_to_check)
    print("Tree nodes:")
    for user in users:
        print(f" * {user}")
    print(f"Searching for: {user_to_find}")
    result = tree.exists(user_to_find)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False