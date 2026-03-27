class Queue:
    def __init__(self, items: list[any] = []) -> None:
        self.items = items.copy()
        self.end = 0

    def push(self, item: any) -> None:
        self.items.append(item)

    def pop(self) -> any:
        if not self.items:
            return None
        item = self.items[self.end]
        self.items[self.end] = None
        self.end += 1
        return item 
       
    def peek(self) -> any:
        return self.items[self.end] if self.items else None
    
    def size(self) -> int:
        return len(self.items) - self.end
    
    def reset(self) -> None:
        self.items.clear()
    
    def search_and_remove(self, item):
        if item not in self.items:
            return None
        self.items.remove(item)
        return item

    def __repr__(self):
        return f"[{', '.join(list(filter(lambda item: item is not None, self.items)))}]"
