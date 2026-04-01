# import time
import time
from lessons.Ch16.L20 import submit_cases, test

def main():
    passed = 0
    failed = 0
    for test_case in submit_cases:
        start = time.time()
        correct = test(*test_case)
        end = time.time()
        print(f'executed in {round(1000 * (end - start), 3)}ms')
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")

if __name__ == "__main__":
    main()