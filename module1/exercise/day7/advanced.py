"""
Day 7 Exercises: Advanced Data Structure Analysis & Trade-offs
"""

import time
from collections import deque

# ==========================================
# 9. Performance Comparison
# ==========================================
def compare_search_performance():
    size = 1_000_000
    test_list = list(range(size))
    test_dict = {i: True for i in range(size)}
    target = 999_999  # Worst-case item

    # Search in List - O(n)
    start_time = time.perf_counter()
    _ = target in test_list
    list_time = time.perf_counter() - start_time

    # Search in Dict - O(1)
    start_time = time.perf_counter()
    _ = target in test_dict
    dict_time = time.perf_counter() - start_time

    print("--- 1. Search Performance ---")
    print(f"List search O(n): {list_time:.6f} seconds")
    print(f"Dict search O(1): {dict_time:.6f} seconds\n")


def compare_insertion_performance():
    elements_count = 10_000

    # Insert at index 0 in Python List - O(n)
    py_list = []
    start_time = time.perf_counter()
    for i in range(elements_count):
        py_list.insert(0, i)
    list_time = time.perf_counter() - start_time

    # Insert at head using collections.deque - O(1)
    dq = deque()
    start_time = time.perf_counter()
    for i in range(elements_count):
        dq.appendleft(i)
    deque_time = time.perf_counter() - start_time

    print("--- 2. Prepend Performance ---")
    print(f"List insert(0) O(n): {list_time:.6f} seconds")
    print(f"Deque appendleft O(1): {deque_time:.6f} seconds\n")


# ==========================================
# 10. Choose the Right Structure
# ==========================================
"""
Scenario Recommendations:

1. Checking if a username is already taken:
   - Recommended: Hash Set or Hash Map (Dictionary)
   - Big-O: O(1) average lookup time.

2. Processing tasks in the order they arrive (customer support):
   - Recommended: Queue (`collections.deque`)
   - Big-O: O(1) for enqueue and dequeue (FIFO logic).

3. Implementing "Undo" feature in a text editor:
   - Recommended: Stack (List or custom Stack)
   - Big-O: O(1) for push and pop operations (LIFO logic).

4. Storing student IDs for fast lookup:
   - Recommended: Hash Map (Dictionary) where Key=ID, Value=Student details
   - Big-O: O(1) average for key lookup.
"""


# ==========================================
# 11. Linked List vs Array (Remove Middle)
# ==========================================
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_middle_list(py_list: list) -> list:
    """
    Remove middle from Python List.
    Finding index: O(1)
    Removal: O(n) shift required.
    Overall: O(n)
    """
    if not py_list:
        return py_list
    mid_idx = len(py_list) // 2
    py_list.pop(mid_idx)
    return py_list


def remove_middle_linked_list(head: Node) -> Node:
    """
    Remove middle using Fast & Slow Pointer strategy.
    Finding middle: O(n) traversal.
    Removal: O(1) pointer adjustment.
    Overall: O(n)
    """
    if not head or not head.next:
        return None

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    # Unlink middle node (slow)
    prev.next = slow.next
    return head


"""
Trade-offs Discussion:
- Python List: Finding the middle index is direct O(1) because elements are contiguous,
  but removing it is O(n) because remaining elements must shift left.
- Linked List: Finding the middle node requires traversing the list O(n), but deleting 
  it requires a simple pointer re-assignment O(1).
"""

if __name__ == "__main__":
    compare_search_performance()
    compare_insertion_performance()