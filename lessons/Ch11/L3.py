from lessons.Ch11.rbtree import RBTree, print_tree
from lessons.Ch11.users import get_users


run_cases = [
    (4,),
    (8,),
]

submit_cases = run_cases + [
    (10,),
]



def test(num_users):
    users = get_users(num_users)
    # ref_tree = RBTree()
    # for user in users:
    #     ref_implementation(ref_tree, user)
    print("============ NEW TEST ===============")
    actual_tree = RBTree()
    for user in users:
        print(f"Inserting {user} into tree...")
        actual_tree.insert(user)
    print("-------------------------------------")
    # print("Expecting Tree:")
    # print("-------------------------------------")
    # print_tree(ref_tree)
    print("-------------------------------------")
    print("Actual Tree:")
    print("-------------------------------------")
    print_tree(actual_tree)
    print("-------------------------------------")
    # if ref_inorder(actual_tree.root, []) == ref_inorder(ref_tree.root, []):
    #     print("Pass")
    #     return True
    print("Fail")
    return False
