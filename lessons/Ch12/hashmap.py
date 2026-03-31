from functools import reduce

class HashMap:
    def __init__(self, size: int) -> None:
        self.hashmap = [None for _ in range(size)]

    def key_to_index(self, key: str) -> int:
        uni_sum = reduce(lambda acc, char: acc + ord(char), key, 0)
        return uni_sum % len(self.hashmap)

    def __repr__(self):
        return str(filter(None, self.hashmap))