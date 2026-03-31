from lessons.Ch13.trie import Trie
import json


run_cases = [
    (["dev", "devops", "devs", "designer"], "devops", True),
    (["manager", "qa", "dev", "intern"], "ceo", False),
    (["engineer", "developer", "janitor"], "dev", False),
]

submit_cases = run_cases + [
    (
        ["dev", "developer", "devops", "manager"],
        "hr",
        False,
    ),
    (["qa", "qaops", "qam"], "qaops", True),
]


def test(words, word_to_check, expected_output):
    print("---------------------------------")
    trie = Trie()
    for word in words:
        trie.add(word)
    print("Trie:")
    print(json.dumps(trie.root, sort_keys=True, indent=2))
    print(f'Checking if "{word_to_check}" exists:')
    print(f"Expected: {expected_output}")
    try:
        actual = trie.exists(word_to_check)
        print(f"Actual:   {actual}")
        if actual == expected_output:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False