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
    
    def search_and_remove(self, item):
        if item not in self.items:
            return None
        self.items.remove(item)
        return item

    def __repr__(self):
        return f"[{', '.join(self.items)}]"
