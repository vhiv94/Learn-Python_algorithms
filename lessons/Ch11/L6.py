from lessons.Ch11.rbtree import RBTree, print_tree
from lessons.Ch11.users import get_users

run_cases = [
    (4,),
]

submit_cases = run_cases + [
    (10,),
]


def test_rotate(tree, node, reference_tree, reference_node, direction):
    print(f"Rotating {direction} at {node.val}...")
    print("-------------------------------------")
    if direction == "left":
        tree.rotate_left(node)
        # ref_impl_left(reference_tree, reference_node)
    else:
        tree.rotate_right(node)
        # ref_impl_right(reference_tree, reference_node)
    # print("Expected Tree:")
    # print("-------------------------------------")
    # print_tree(reference_tree)
    print("-------------------------------------")
    print("Actual Tree:")
    print("-------------------------------------")
    print_tree(tree)
    print("-------------------------------------")
    # return ref_compare(tree.root, reference_tree.root)


def test_rotations(tree, reference_tree):
    return (
        test_rotate(tree, tree.root, reference_tree, reference_tree.root, "left")
        and test_rotate(tree, tree.root, reference_tree, reference_tree.root, "right")
        and test_rotate(
            tree, tree.root.right, reference_tree, reference_tree.root.right, "left"
        )
        and test_rotate(
            tree, tree.root.left, reference_tree, reference_tree.root.left, "right"
        )
    )


def test(num_users):
    users = get_users(num_users)
    tree = RBTree()
    reference_tree = RBTree()
    for user in users:
        tree.insert(user)
        reference_tree.insert(user)
    print("=====================================")
    print("Starting Tree:")
    print("-------------------------------------")
    print_tree(tree)
    print("-------------------------------------")

    if test_rotations(tree, reference_tree):
        print("Pass \n")
        return True
    print("Fail 1 \n")
    return False


def format_tree_string(node, lines, level=0):
    if node.val is not None:
        format_tree_string(node.right, lines, level + 1)
        lines.append(
            " " * 4 * level
            + "> "
            + str(node.val)
            + " "
            + ("[red]" if node.red else "[black]")
        )
        format_tree_string(node.left, lines, level + 1)