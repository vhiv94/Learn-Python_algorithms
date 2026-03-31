from __future__ import annotations


class BSTNode:
    def __init__(self, val: int | None = None) -> None:
        self.left: BSTNode = None
        self.right: BSTNode = None
        self.val: int = val

    def get_max(self) -> int:
        if self.right:
            return self.right.get_max()
        return self.val
    
    def get_min(self) -> int:
        if self.left:
            return self.left.get_min()
        return self.val

    def insert(self, val: int) -> None:
        if self.val is None:
            self.val = val
        elif val == self.val:
            pass
        elif val < self.val:
            if self.left is None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)

    def delete(self, val: int) -> BSTNode:
        if self.val is None:
            return None
        elif val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        elif val == self.val:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                successor = self.left.get_max()
                self.val = successor
                self.left = self.left.delete(successor)
                return self
            
    def preorder(self, order: list[int]) -> list[int]:
        if self.val is not None:
            order.append(self.val)
        if self.left:
            self.left.preorder(order)
        if self.right:
            self.right.preorder(order)
        return order
    
    def postorder(self, order: list) -> list:
        if self.left:
            self.left.postorder(order)
        if self.right:
            self.right.postorder(order)
        if self.val:
            order.append(self.val)
        return order
        
    def inorder(self, order: list) -> list:
        if self.left:
            self.left.inorder(order)
        if self.val:
            order.append(self.val)
        if self.right:
            self.right.inorder(order)
        return order

def print_tree(bst_node):
    lines = []
    format_tree_string(bst_node, lines)
    print("\n".join(lines))


def format_tree_string(bst_node, lines, level=0):
    if bst_node is not None:
        format_tree_string(bst_node.right, lines, level + 1)
        lines.append(" " * 4 * level + "> " + str(bst_node.val))
        format_tree_string(bst_node.left, lines, level + 1)