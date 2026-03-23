import math


def get_influencer_score(num_followers: int, average_engagement_percentage: float) -> float:
    return average_engagement_percentage * math.log(num_followers, 2)


run_cases = [(40000, 0.3, 5), (43000, 0.1, 2), (100000, 0.6, 10)]

submit_cases = run_cases + [
    (1, 1, 0),
    (200, 0.8, 6),
    (300000, 0.5, 9),
    (500000, 0.2, 4),
    (750000, 0.7, 14),
]


def test(input1, input2, expected_output):
    try:
        print("---------------------------------")
        print(f"Inputs:")
        print(f" * num_followers: {input1}")
        print(f" * average_engagement_percentage: {input2}")
        result = round(get_influencer_score(input1, input2))
        print(f"Expected: {expected_output}")
        print(f"Actual:   {result}")
        if result == expected_output:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print("Fail")
        print(e)
        return False