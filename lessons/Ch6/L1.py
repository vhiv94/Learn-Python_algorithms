from functools import reduce


def count_marketers(job_titles: list[str]) -> int:
    return reduce(lambda acc, title: acc + (title.lower() == "marketer"), job_titles, 0)

run_cases = [
    (["developer", "marketer", "designer"], 1),
    (["marketer", "marketer", "developer", "marketer"], 3),
]

submit_cases = run_cases + [
    ([], 0),
    (["developer", "designer", "product manager"], 0),
    (["marketer"], 1),
    (["MARKETER", "Marketer", "marketer"], 3),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input job titles: {input1}")
    print(f"Expected: {expected_output}")
    result = count_marketers(input1)
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False