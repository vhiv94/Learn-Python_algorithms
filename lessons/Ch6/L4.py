def last_work_experience(work_experiences: list[str]) -> str:
    return work_experiences[-1] if work_experiences else None


run_cases = [
    (["Software Engineer", "Data Analyst", "Project Manager"], "Project Manager"),
    (["Intern", "Junior Developer"], "Junior Developer"),
]

submit_cases = run_cases + [
    ([], None),
    (["CEO"], "CEO"),
    (["Cashier", "Supervisor", "Manager", "Director"], "Director"),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input work experiences: {input1}")
    print(f"Expected output: {expected_output}")
    original = list(input1)
    result = last_work_experience(input1)
    print(f"Actual output: {result}")
    if result == expected_output and input1 == original:
        print("Pass")
        return True
    print("Fail")
    return False