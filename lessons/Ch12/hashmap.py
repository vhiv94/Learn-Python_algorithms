from lessons.Ch12.users import User
from functools import reduce

class HashMap:
    def __init__(self, size: int) -> None:
        self.hashmap = [None for _ in range(size)]

    def insert(self, key: str, val: User) -> None:
        self.resize()
        index = self.key_to_index(key)
        bucket = self.hashmap[index]
        original_index = index
        first_iteration = True
        while bucket is not None and bucket[0] is not key:
            if not first_iteration and index == original_index:
                raise Exception("hashmap is full")
            index += 1
            index %= len(self.hashmap)
            first_iteration = False
            bucket = self.hashmap[index]
        self.hashmap[index] = (key, val)

    def get(self, key: str) -> User:
        index = self.key_to_index(key)
        bucket = self.hashmap[index]
        original_index = index
        first_iteration = True
        while bucket is not None:
            if bucket[0] == key:    
                return bucket[1]    
            if not first_iteration and index == original_index:
                raise Exception("sorry, key not found")
            index += 1
            index %= len(self.hashmap)
            first_iteration = False
            bucket = self.hashmap[index]
        raise Exception("sorry, key not found")

        
    def resize(self) -> None:
        if len(self.hashmap) == 0:
            self.hashmap.append(None)
            return
        if self.current_load() < 0.05:
            return
        temp = self.hashmap
        self.hashmap = [None for _ in range(len(temp) * 10)]
        temp = list(filter(None, temp))
        for item in temp:
            self.insert(*item)

    def current_load(self) -> float:
        if len(self.hashmap) == 0:
            return 1
        return len(list(filter(None, self.hashmap))) / len(self.hashmap)

    def key_to_index(self, key: str) -> int:
        return reduce(lambda acc, char: acc + ord(char), key, 0) % len(self.hashmap)

    def __repr__(self):
        return str(filter(None, self.hashmap))