from __future__ import annotations


class Node:
    def __init__(self, val: any) -> None:
        self.val: any | None = val
        self.next: Node | None = None

    def set_next(self, node: Node) -> None:
        self.next = node

    def __repr__(self) -> any:
        return self.val
    

class LinkedList:
    def __init__(self, node: Node | None = None) -> None:
        self.head: Node | None = node

    def add_to_head(self, node: Node) -> None:
        node.next = self.head
        self.head = node

    def add_to_tail(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            return
        for current in self:
            if current.next is None:
                current.next = node
                return

    def __iter__(self):
        current: Node = self.head
        while True:
            yield current
            if current.next is not None:
               current = current.next
            else:
                break
    
    def __repr__(self) -> str:
        nodes: list[Node] = []
        current: Node = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)
