from lessons.Ch8.queue import Queue


def matchmake(queue: Queue, user: tuple[str, str]) -> str:
    match user[1]:
        case "join":
            queue.push(user[0])
        case "leave":
            queue.search_and_remove(user[0])

    return f"{queue.pop()} matched {queue.pop()}!" if queue.size() >= 4 else "No match found"


run_cases = [
    [("Ted", "join"), (["Ted"], "No match found")],
    [("Barney", "join"), (["Barney", "Ted"], "No match found")],
    [("Marshall", "join"), (["Marshall", "Barney", "Ted"], "No match found")],
    [("Lily", "join"), (["Lily", "Marshall"], "Ted matched Barney!")],
    [("Robin", "join"), (["Robin", "Lily", "Marshall"], "No match found")],
    [("Carl", "join"), (["Carl", "Robin"], "Marshall matched Lily!")],
    [("Carl", "leave"), (["Robin"], "No match found")],
    [("Robin", "leave"), ([], "No match found")],
]

submit_cases = run_cases + [
    [("Ranjit", "join"), (["Ranjit"], "No match found")],
    [("Ranjit", "leave"), ([], "No match found")],
    [("Victoria", "join"), (["Victoria"], "No match found")],
    [("Quinn", "join"), (["Quinn", "Victoria"], "No match found")],
    [("Zoey", "join"), (["Zoey", "Quinn", "Victoria"], "No match found")],
    [("Stella", "join"), (["Stella", "Zoey"], "Victoria matched Quinn!")],
]


def test(queue, user, expected_state):
    print("---------------------------------")
    print(f"Queue: {queue}")
    name = user[0]
    action = user[1]
    if action == "leave":
        print(f"{name} left the queue.")
    if action == "join":
        print(f"{name} joined the queue.")
    print(f"Expecting Queue: {expected_state[0]}")
    print(f"Expecting Return: {expected_state[1]}")
    try:
        result = matchmake(queue, user)
    except Exception as e:
        result = f"Error: {e}"
    print(f"Actual Queue: {queue}")
    print(f"Actual Return: {result}")
    if result == expected_state[1] and queue.items == expected_state[0]:
        print("Pass")
        return True
    print("Fail")
    return False