from lessons.Ch13.trie import Trie
import json


run_cases = [
    (
        ["dev", "devops", "devs"],
        {
            "d": {
                "e": {
                    "v": {"*": True, "o": {"p": {"s": {"*": True}}}, "s": {"*": True}}
                }
            }
        },
    ),
    (
        ["qa", "qaops", "qam"],
        {
            "q": {
                "a": {"*": True, "o": {"p": {"s": {"*": True}}}, "m": {"*": True}},
            }
        },
    ),
]

submit_cases = run_cases + [
    (
        ["pm", "po", "pojo", "pope", "cs", "ce", "ceo", "cfo"],
        {
            "p": {
                "m": {"*": True},
                "o": {"*": True, "j": {"o": {"*": True}}, "p": {"e": {"*": True}}},
            },
            "c": {
                "s": {"*": True},
                "e": {"*": True, "o": {"*": True}},
                "f": {"o": {"*": True}},
            },
        },
    ),
]


def test(words, expected_trie):
    print("---------------------------------")
    print("Inputs:")
    print(f" * Words: {words}")
    print(" * Expected trie:")
    print(f"{json.dumps(expected_trie, sort_keys=True, indent=2)}")
    try:
        trie = Trie()
        for word in words:
            trie.add(word)
            print(f"Adding {word}...")
        print("Actual Trie:")
        print(json.dumps(trie.root, sort_keys=True, indent=2))
        if trie.root == expected_trie:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False