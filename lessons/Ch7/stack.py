class Stack:
    def __init__(self, items: list[any] = []) -> None:
        self.items = items.copy()

    def push(self, item: any) -> None:
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)
    
    def peek(self) -> any:
        return self.items[-1] if self.items else None
    
    def pop(self) -> any:
        # return self.items.pop() if self.items else None
        if not self.items:
            return None
        top = self.items[-1]
        del self.items[-1]
        return top

    def reset(self) -> None:
        self.items.clear()