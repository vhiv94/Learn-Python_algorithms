class Queue:
    def __init__(self, items: list[any] = []) -> None:
        self.items = items.copy()

    def push(self, item: any) -> None:
        self.items.insert(0, item)

    def pop(self) -> any:
        if not self.items:
            return None
        item = self.items[-1]
        del self.items[-1]
        return item 
       
    def peek(self) -> any:
        return self.items[-1] if self.items else None
    
    def size(self) -> int:
        return len(self.items)
    
    def reset(self) -> None:
        self.items.clear()