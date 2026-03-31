from __future__ import annotations
import json


class Trie:
    def __init__(self, init_list: list[str] | None = None) -> None:
        self.root: dict = {}
        self.end_symbol: str = "*"

        if init_list:
            # init_list = sorted(init_list, key=lambda elem: len(elem))
            for elem in init_list:
                self.add(elem)

    def add(self, word: str) -> Trie:
        word.lower()
        current = self.root
        for char in word:
            if char not in current:
                current.setdefault(char, {})
            current = current.get(char)
        current.setdefault(self.end_symbol, True)
        return self
    
    def exists(self, word: str) -> bool:
        word.lower()
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current.get(char)
        return current.get(self.end_symbol, False)
    
    def __repr__(self) -> str:
        return json.dumps(trie.root, sort_keys=True, indent=2)

trie = Trie(["hi", "hello", "help"])
trie.exists("hello")
print(trie)