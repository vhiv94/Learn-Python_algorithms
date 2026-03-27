class Stack:
    def __init__(self, items: list[any] = []) -> None:
        self.items = items

    def push(self, item: any) -> None:
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)
    
    def clear(self) -> None:
        self.items.clear()
