from __future__ import annotations


class RBNode:
    def __init__(self, val: int, nil: RBNode) -> None:
        self.red: bool = False
        self.parent: RBNode = None
        self.val: int = val
        self.left: RBNode = nil
        self.right: RBNode = nil

class RBTree:
    def __init__(self) -> None:
        self.nil = RBNode(None, None)
        self.root = self.nil

    def insert(self, val: int) -> None:
        new_node = RBNode(val, self.nil)
        if self.root is self.nil:
            self.root = new_node
            return
        # new_node.red = True
        parent: RBNode = None
        current: RBNode = self.root
        while current is not self.nil:
            parent = current
            if new_node.val == current.val:
                return
            elif new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
        new_node.parent = parent
        new_node.red = not parent.red
        # if parent is None:
        #     self.root = new_node
        #     self.root.red = False
        # else:
        if new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

    def rotate_left(self, pivot_parent: RBNode) -> None:
        grandparent: RBNode | None = pivot_parent.parent
        if pivot_parent is self.nil or pivot_parent.right is self.nil:
            return
        pivot: RBNode = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left is not self.nil:
            pivot.left.parent = pivot_parent
        pivot.parent = grandparent
        if self.root == pivot_parent:
            self.root = pivot
        elif grandparent.left is pivot_parent: 
            grandparent.left = pivot
        elif grandparent.right is pivot_parent:
            grandparent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent: RBNode) -> None:
        grandparent: RBNode | None = pivot_parent.parent
        if pivot_parent is self.nil or pivot_parent.left is self.nil:
            return
        pivot: RBNode = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot.right is not self.nil:
            pivot.right.parent = pivot_parent
        pivot.parent = grandparent
        if self.root is pivot_parent:
            self.root = pivot
        elif grandparent.right is pivot_parent:
            grandparent.right = pivot
        elif grandparent.left is pivot_parent:
            grandparent.left = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot


def print_tree(node):
    lines = []
    format_tree_string(node.root, lines)
    print("\n".join(lines))


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