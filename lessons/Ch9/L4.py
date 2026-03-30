from lessons.Ch9.linked_list import Node, LinkedList


# Updated test cases with character names from "The Hateful Eight"
run_cases = [
    ("John Ruth", ["Major Marquis Warren", "John Ruth"]),
    ("Daisy Domergue", ["Major Marquis Warren", "John Ruth", "Daisy Domergue"]),
    (
        "Chris Mannix",
        ["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix"],
    ),
]

submit_cases = run_cases + [
    (
        "Bob",
        ["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix", "Bob"],
    ),
    (
        "Oswaldo Mobray",
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


def test(linked_list, input, expected_state):
    print("---------------------------------")
    print(f"Linked List: {linked_list}")
    print(f"Set Next: {input}")
    print(f"Expected: {expected_state}")
    node = Node(input)
    last_node: Node = get_last_node(linked_list)
    last_node.set_next(node)
    try:
        result = linked_list_to_list(linked_list)
    except Exception as e:
        result = f"Error: {e}"
    print(f"Actual: {result}")
    if result == expected_state:
        print("Pass")
        return True
    print("Fail")
    return False


def linked_list_to_list(linked_list: LinkedList) -> list[Node]:
    result: list[Node] = []
    for node in linked_list:
        result.append(node.val)

    return result


def get_last_node(linked_list: LinkedList) -> Node:
    current: Node = linked_list.head
    while hasattr(current, "next") and current.next:
        current = current.next
    return current