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
    def add_to_head(self, val: any) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def add_to_tail(self, val: any) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def __init__(self, list: list[any] | None = None) -> None:
        if list is None:
            self.head: Node = None
            self.tail: Node = None
        elif len(list) == 1:
            self.head = Node(list[0])
            self.tail = self.head
        elif len(list) == 2:
            self.head = Node(list[0])
            self.tail = Node(list[1])
            self.head.next = self.tail
        else:
            self.head = Node(list[0])
            current = self.head
            for i in range(1, len(list)):
                current.next = Node(list[i])
                current = current.next
            self.tail = current

    def __iter__(self):
        current: Node = self.head
        while current is not None:
            yield current
            current = current.next
    
    def __repr__(self) -> str:
        nodes: list[Node] = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)