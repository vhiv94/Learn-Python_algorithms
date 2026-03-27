from lessons.Ch8.queue import Queue

run_cases = [
    (
        [("push", "Rand"), ("push", "Mat"), ("peek", None), ("pop", None)],
        ["Rand", "Rand"],
    ),
    (
        [
            ("push", "Egwene"),
            ("push", "Nynaeve"),
            ("size", None),
            ("pop", None),
            ("size", None),
        ],
        [2, "Egwene", 1],
    ),
]

submit_cases = run_cases + [
    ([("pop", None), ("peek", None), ("size", None)], [None, None, 0]),
    (
        [
            ("push", "Perrin"),
            ("push", "Moiraine"),
            ("push", "Lan"),
            ("pop", None),
            ("pop", None),
            ("peek", None),
        ],
        ["Perrin", "Moiraine", "Lan"],
    ),
    (
        [("push", "Thom"), ("pop", None), ("push", "Loial"), ("peek", None)],
        ["Thom", "Loial"],
    ),
]


def visualize_queue(queue):
    if not queue.items:
        return "Queue is empty"
    return "\n".join([f"- {item}" for item in reversed(queue.items)])


def test(operations, expected_outputs):
    print("---------------------------------")
    queue = Queue()
    outputs = []
    for op, value in operations:
        if op == "push":
            queue.push(value)
            print(f"Push: {value}")
        elif op == "pop":
            result = queue.pop()
            outputs.append(result)
            print(f"Pop: {result}")
        elif op == "peek":
            result = queue.peek()
            outputs.append(result)
            print(f"Peek: {result}")
        elif op == "size":
            result = queue.size()
            outputs.append(result)
            print(f"Size: {result}")

        print("\nQueue state:")
        print(visualize_queue(queue))
        print()

    print(f"Expected: {expected_outputs}")
    print(f"Actual: {outputs}")
    if outputs == expected_outputs:
        print("Pass")
        return True
    print("Fail")
    return False