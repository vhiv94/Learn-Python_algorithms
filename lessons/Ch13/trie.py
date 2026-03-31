from __future__ import annotations
import json


class Trie:
    def __init__(self, init_list: list[str] | None = None) -> None:
        self.root = {}
        self.end_symbol = "*"

        if not init_list:
            return
        
        sorted_list = sorted(init_list, key=lambda elem: len(elem))
        for elem in sorted_list:
            self.add(elem)

    def add(self, word: str) -> Trie:
        word.lower()
        next = self.root
        for char in word:
            if char not in next:
                next.setdefault(char, {})
            next = next.get(char)
        next.setdefault(self.end_symbol, True)
        return self
    
    def __repr__(self) -> str:
        return json.dumps(trie.root, sort_keys=True, indent=2)

trie = Trie(["hi", "hello", "help"])
print(trie)