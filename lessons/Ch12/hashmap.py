from lessons.Ch12.users import User
from functools import reduce

class HashMap:
    def __init__(self, size: int) -> None:
        self.hashmap = [None for _ in range(size)]

    def insert(self, key: str, val: User) -> None:
        self.hashmap[self.key_to_index(key)] = (key, val)

    def get(self, key: str) -> User:
        val = self.hashmap[self.key_to_index(key)]
        if val is None:
            raise Exception("sorry, key not found") 
        else:
            return val[1]

    def key_to_index(self, key: str) -> int:
        uni_sum = reduce(lambda acc, char: acc + ord(char), key, 0)
        return uni_sum % len(self.hashmap)

    def __repr__(self):
        return str(filter(None, self.hashmap))