class BSTNode:
    def __init__(self, val: int | None = None) -> None:
        self.left: BSTNode = None
        self.right: BSTNode = None
        self.val: int = val

    def insert(self, val: int) -> None:
        if self.val is None:
            self.val = val
            return
        elif val == self.val:
            return
        elif val < self.val:
            if self.left is None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
                return
        elif val > self.val:
            if self.right is None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)
                return
        else:
            return