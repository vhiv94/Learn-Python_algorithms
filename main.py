import time
import random
from lessons.Ch3.L11 import submit_cases, test

def main():
    random.seed(1)
    passed = 0
    failed = 0
    for test_case in submit_cases:
        start = time.time()
        correct = test(*test_case)
        execution_time_ms = round(1000 * (time.time() - start), 3)
        if correct:
            passed += 1
        else:
            failed += 1
        print(f'executed in {execution_time_ms}ms')
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")

if __name__ == "__main__":
    main()