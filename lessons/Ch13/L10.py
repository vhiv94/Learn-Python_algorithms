from lessons.Ch13.trie import Trie


run_cases = [
    (
        [
            "darnit",
            "nope",
            "bad",
        ],
        "This is a d@rn1t test with b@d words!",
        {
            "@": "a",
            "1": "i",
            "4": "a",
            "!": "i",
        },
        [
            "b@d",
            "d@rn1t",
        ],
    ),
    (
        [
            "darn",
            "shoot",
            "gosh",
        ],
        "h3ck this fudg!ng thing",
        {
            "@": "a",
            "3": "e",
        },
        [],
    ),
    (
        [
            "dang",
            "darn",
            "heck",
            "gosh",
        ],
        "d@ng it to h3ck",
        {
            "@": "a",
            "3": "e",
        },
        ["d@ng", "h3ck"],
    ),
]
submit_cases = run_cases + [
    (
        [
            "darn",
            "shoot",
            "fudging",
        ],
        "sh00t, I hate this fudg!ng assignment",
        {
            "@": "a",
            "3": "e",
            "0": "o",
            "!": "i",
        },
        ["sh00t", "fudg!ng"],
    ),
]


def test(words, document, variations, expected_matches):
    print("---------------------------------")
    print("Document:")
    print(document)
    print(f"Variations: {variations}")
    print(f"Expected matches: {sorted(expected_matches)}")
    try:
        trie = Trie(words)
        actual = sorted(trie.advanced_find_matches(document, variations))
        print(f"Actual matches: {actual}")
        if actual == sorted(expected_matches):
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False