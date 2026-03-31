from lessons.Ch13.trie import Trie
import json


run_cases = [
    (
        ["synergy", "alignment", "leverage", "bandwidth"],
        "Let's leverage our synergy to realign our bandwidth",
        ["synergy", "leverage", "bandwidth"],
    ),
    (
        ["circle", "back", "touch", "base"],
        "Let's circle back to touch base",
        ["circle", "back", "touch", "base"],
    ),
]

submit_cases = run_cases + [
    (
        ["pivot", "innovate", "scalable", "proactive"],
        "We need to pivot and innovate for truly scalable solutions",
        ["pivot", "innovate", "scalable"],
    ),
]


def test(words, document, expected_matches):
    print("---------------------------------")
    print("Trie:")
    trie = Trie()
    for word in words:
        trie.add(word)
    print(json.dumps(trie.root, sort_keys=True, indent=2))
    print(f"Expected matches: {sorted(expected_matches)}")
    try:
        actual = sorted(trie.find_matches(document))
        print(f"Actual matches: {actual}")
        if actual == sorted(expected_matches):
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False