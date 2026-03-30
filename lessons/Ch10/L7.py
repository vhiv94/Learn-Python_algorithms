from lessons.Ch10.bst import BSTNode, print_tree
from lessons.Ch10.users import get_users

run_cases = [
    (5, "Blake#0", "Carrell#14"),
    (10, "Ricky#1", "Vennett#29"),
]

submit_cases = run_cases + [
    (15, "Shelley#2", "George#42"),
]


def test(num_users, min_user, max_user):
    users = get_users(num_users)
    bst = BSTNode()
    for user in users:
        bst.insert(user)
    print("=====================================")
    print("Tree:")
    print("-------------------------------------")
    print_tree(bst)
    print("-------------------------------------\n")
    print(f"Expected min: {min_user}, max: {max_user}")
    try:
        actual_min = bst.get_min()
        actual_max = bst.get_max()
        print(f"Actual min: {actual_min.user_name}, max: {actual_max.user_name}")
        if actual_max.user_name == max_user and actual_min.user_name == min_user:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False