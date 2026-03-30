from lessons.Ch9.linked_list import Node, LinkedList



run_cases = [
    (["Major Marquis Warren", "John Ruth"],),
    (["Major Marquis Warren", "John Ruth", "Daisy Domergue"],),
]

submit_cases = run_cases + [
    (["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix"],),
    (["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix", "Bob"],),
    (
        [
            "Major Marquis Warren",
            "John Ruth",
            "Daisy Domergue",
            "Chris Mannix",
            "Bob",
            "Oswaldo Mobray",
        ],
    ),
]


def test(inputs):
    print("---------------------------------")
    linked_list = LinkedList()
    for val in inputs:
        linked_list.add_to_tail(Node(val))
    actual = linked_list_to_list(linked_list)

    print(f"Expected: {inputs}")
    print(f"Actual  : {actual}")

    if actual == inputs:
        print("Pass")
        return True
    else:
        print("Fail")
        return False


def linked_list_to_list(linked_list):
    return [node.val for node in linked_list]