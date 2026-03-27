from __future__ import annotations


class Node:
    def __init__(self, val: any) -> None:
        self.val = val
        self.next = None

    def set_next(self, node: Node) -> None:
        self.next = node

    def __repr__(self):
        return self.val