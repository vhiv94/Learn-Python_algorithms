# import time
import time
from lessons.Ch9.L4 import submit_cases, test
from lessons.Ch9.linked_list import Node, LinkedList

def main():
    passed = 0
    failed = 0
    linked_list = LinkedList(Node("Major Marquis Warren"))
    for test_case in submit_cases:
        start = time.time()
        correct = test(linked_list, *test_case)
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