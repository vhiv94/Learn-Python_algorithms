def get_follower_prediction(follower_count: int, influencer_type: str, num_months: int) -> int:
    match influencer_type:
        case "fitness":
            return follower_count * 4 ** num_months
        case "cosmetic":
            return follower_count * 3 ** num_months
        case _:
            return follower_count * 2 ** num_months
        
TestCase = tuple[int, str, int, int]

run_cases: list[TestCase] = [
    (10, "fitness", 1, 40),
    (10, "fitness", 2, 160),
    (12, "cosmetic", 4, 972),
]

submit_cases: list[TestCase] = run_cases + [
    (15, "business", 4, 240),
    (10, "fitness", 5, 10240),
    (10, "fitness", 6, 40960),
    (10, "fitness", 7, 163840),
    (10, "fitness", 8, 655360),
    (10, "tech", 9, 5120),
]


def test(
    follower_count: int, influencer_type: str, num_months: int, expected: int
) -> bool:
    print("---------------------------------")
    print("Inputs:")
    print(f" * Follower count: {follower_count}")
    print(f" * Influencer type: {influencer_type}")
    print(f" * Number of months: {num_months}")
    print(f"Expected: {expected}")
    result = get_follower_prediction(follower_count, influencer_type, num_months)
    print(f"Actual:   {result}")
    if result == expected:
        print("Pass")
        return True
    print("Fail")
    return False