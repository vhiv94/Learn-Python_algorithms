from lessons.Ch10.users import get_users
from lessons.Ch10.bst import BSTNode



run_cases = [
    (3),
    (5),
]

submit_cases = run_cases + [
    (10),
]


def test(num_users):
    users = get_users(num_users)
    expected_bst = BSTNode()
    # for user in users:
    #     ref_implementation(expected_bst, user)
    print("=====================================")
    print("Expecting Tree:")
    print("-------------------------------------")
    print_tree(expected_bst)
    print("-------------------------------------\n")
    actual_bst = BSTNode()
    for user in users:
        print(f"Inserting {user} into tree...")
        actual_bst.insert(user)
    print("\n")
    print("Actual Tree:")
    print("-------------------------------------")
    print_tree(actual_bst)
    print("-------------------------------------")
    # if ref_inorder(actual_bst, []) == ref_inorder(expected_bst, []):
    #     print("Pass \n")
        # return True
    print("Fail \n")
    return False


def print_tree(bst_node):
    lines = []
    format_tree_string(bst_node, lines)
    print("\n".join(lines))


def format_tree_string(bst_node, lines, level=0):
    if bst_node is not None:
        format_tree_string(bst_node.right, lines, level + 1)
        lines.append(" " * 4 * level + "> " + str(bst_node.val))
        format_tree_string(bst_node.left, lines, level + 1)