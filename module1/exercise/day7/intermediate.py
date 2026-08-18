"""
Day 7 Exercises: Intermediate Linear Data Structures
"""

from collections import deque

# ==========================================
# 5. Big-O Analysis
# ==========================================
def find_max(numbers: list) -> int:
    """
    Time Complexity: O(n) - Linear Time.
    It inspects each of the 'n' elements in the list exactly once.
    """
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def print_pairs(numbers: list) -> None:
    """
    Time Complexity: O(n²) - Quadratic Time.
    For an input size of n, the outer loop runs n times and the inner loop
    runs n times for each outer iteration (n * n = n² steps).
    """
    for i in numbers:
        for j in numbers:
            print(f"({i}, {j})", end=" ")
    print()


# ==========================================
# 6. Linked List Basics
# ==========================================
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Append value to the end of the list. Time Complexity: O(n)."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Print all node values. Time Complexity: O(n)."""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements) + " -> None")


# ==========================================
# 7. Stack (LIFO)
# ==========================================
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Time Complexity: O(1) amortized"""
        self.items.append(item)

    def pop(self):
        """Time Complexity: O(1)"""
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        """Time Complexity: O(1)"""
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0


def reverse_string(text: str) -> str:
    stack = Stack()
    for char in text:
        stack.push(char)
    
    reversed_text = ""
    while not stack.is_empty():
        reversed_text += stack.pop()
    return reversed_text


# ==========================================
# 8. Queue (FIFO)
# ==========================================
class Queue:
    def __init__(self):
        # Using deque for efficient O(1) pops from the left side
        self.items = deque()

    def enqueue(self, item):
        """Time Complexity: O(1)"""
        self.items.append(item)

    def dequeue(self):
        """Time Complexity: O(1)"""
        return self.items.popleft() if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0


def simulate_bank_queue():
    bank_queue = Queue()
    
    # Customers arrive
    print("--- Bank Queue Simulation ---")
    bank_queue.enqueue("Customer 1: Abebe")
    bank_queue.enqueue("Customer 2: Almaz")
    bank_queue.enqueue("Customer 3: Bekele")

    # Serving customers in order
    while not bank_queue.is_empty():
        served_customer = bank_queue.dequeue()
        print(f"Serving {served_customer}")


if __name__ == "__main__":
    # Test Stack String Reversal
    original = "Addis Ababa"
    print(f"Original String: {original}")
    print(f"Reversed String: {reverse_string(original)}\n")

    # Test Queue Simulation
    simulate_bank_queue()