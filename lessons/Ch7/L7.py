from lessons.Ch7.stack import Stack


def is_balanced(input: str) -> bool:
    stack = Stack()
    for paren in input:
        if paren == "(":
            stack.push(paren)
        if paren == ")":
            if not stack.peek():
                return False
            stack.pop()

    return False if stack.pop() else True


run_cases = [
    ("(", False),
    ("()", True),
    ("(())", True),
]

submit_cases = run_cases + [
    ("()()", True),
    ("(()))", False),
    ("((())())", True),
    ("(()(()", False),
    (")(", False),
    (")()(()", False),
    ("())(()", False),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expected: {expected_output}")
    result = is_balanced(input1)
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False