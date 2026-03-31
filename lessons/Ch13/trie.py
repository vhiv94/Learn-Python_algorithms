from __future__ import annotations
import json


class Trie:
    def __init__(self, init_list: list[str] | None = None) -> None:
        self.root: dict[str, dict] = {}
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

    def words_with_prefix(self, prefix: str) -> list[str]:
        words = []
        current_level = self.root
        for char in prefix:
            current_level = current_level.get(char)  
            if current_level is None:
                return words
        self.search_level(current_level, prefix, words)
        return words

    def search_level(self, current_level: dict[str, dict], current_prefix: str, words: list[str]) -> None:
        if current_level.get(self.end_symbol, False):
            words.append(current_prefix)
        for char, sub_trie in sorted(current_level.items(), key=lambda item: item[0]):
            if char is self.end_symbol:
                continue
            sub_trie_prefix = current_prefix + char
            self.search_level(sub_trie, sub_trie_prefix, words)
    
    def __repr__(self) -> str:
        return json.dumps(self.root, sort_keys=True, indent=2)

# trie = Trie(["hi", "hello", "help"])
# trie.exists("hello")
# words = trie.words_with_prefix("hel")
# print(words)