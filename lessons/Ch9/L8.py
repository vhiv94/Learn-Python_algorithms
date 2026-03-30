from lessons.Ch9.linked_list import LLQueue


run_cases = [
    (
        ["Rick", "Cliff", "Sharon", "Jay", "Roman", "Squeaky"],
        ["Cliff", "Sharon", "Jay", "Roman", "Squeaky"], "Rick", "Squeaky",
    ),
    (
        ["Cliff", "Sharon", "Jay", "Roman", "Squeaky"],
        ["Sharon", "Jay", "Roman", "Squeaky"], "Cliff", "Squeaky",
    ),
]

submit_cases = run_cases + [
    ([], [],),
    (["Jay"], [], "Jay"),
    (["Roman", "Squeaky"], ["Squeaky"], "Roman", "Squeaky"),
    (["Squeaky"], [], "Squeaky"),
]


def test(lst, expected_state, expected_head=None, expected_tail=None):
    queue = LLQueue()
    for item in lst:
        queue.push(item)

    print("---------------------------------")
    print(f"Linked List Queue: {queue}")
    print("Removing Head...\n")
    try:
        head = queue.pop()
        tail = queue.tail
        result = linked_list_to_list(queue)
        print(f"Expected List: {expected_state}")
        print(f"  Actual List: {result}\n")
        if result != expected_state:
            print("Fail")
            return False
        print(f"Expected Removed Head: {expected_head}")
        print(f"  Actual Removed Head: {head}\n")
        if not (head is None and expected_head is None) and (head.val != expected_head):
            print("Fail")
            return False
        print(f"Expected Tail: {expected_tail}")
        print(f"  Actual Tail: {tail}\n")
        if not (tail is None and expected_tail is None) and (tail.val != expected_tail):
            print("Fail")
            return False
        if head is not None:
            print("Expected Removed Head's Next Node: None")
            print(f"         Actual Removed Head Next: {head.next}\n")
            if head.next is not None:
                print("Fail")
                return False
        print("Pass")
        return True
    except Exception as e:
        print(f"Exception: {str(e)}")
        print("Fail")
        return False


def linked_list_to_list(linked_list):
    result = []
    for node in linked_list:
        result.append(node.val)

    return result