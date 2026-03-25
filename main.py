# import time
import random
from lessons.Ch4.L15 import submit_cases, test


def main():
    random.seed(1)
    passed = 0
    failed = 0
    test1_speeds = []
    test2_speeds = []
    for test_case in submit_cases:
        # start = time.time()
        correct = test(test1_speeds, test2_speeds, *test_case)
        # end = time.time()
        # print(f'executed in {round(1000 * (end - start), 3)}ms')
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")
    print(f"test 1 speeds: {test1_speeds}")
    print(f"test 2 speeds: {test2_speeds}")

if __name__ == "__main__":
    main()