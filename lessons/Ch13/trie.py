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
    
    def find_matches(self, doc: str) -> set[str]:
        result = set()
        for i in range(len(doc)):
            level = self.root
            for j in range(i, len(doc)):
                level = level.get(doc[j])
                if not level:
                    break
                if self.end_symbol in level:
                    result.add(doc[i:j+1])
        return result
    
    def exists(self, word: str) -> bool:
        word.lower()
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current.get(char)
        return current.get(self.end_symbol, False)

    def words_with_prefix(self, prefix: str) -> list[str]:
        result = []
        level = self.root
        for char in prefix:
            level = level.get(char)  
            if level is None:
                return result
        self.search_level(level, prefix, result)
        return result

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

trie = Trie(["hi", "hello", "help"])
trie.exists("hello")
words = trie.find_matches("hello, world, help me help you")
print(words)