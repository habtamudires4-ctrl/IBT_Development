"""
Day 8 Exercises: Basic Recursion, Searching & Sorting
"""

# ==========================================
# 1. Recursion Basics
# ==========================================
def factorial_recursive(n: int) -> int:
    """
    Calculates factorial recursively.
    Time Complexity: O(n) - Makes n recursive calls.
    Space Complexity: O(n) - Call stack depth of n.
    """
    # Base case: Factorial of 0 or 1 is 1
    if n <= 1:
        return 1
    # Recursive step: n * (n-1)!
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Calculates factorial iteratively using a loop.
    Time Complexity: O(n) - Loops n times.
    Space Complexity: O(1) - Uses constant space.
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# ==========================================
# 2. Recursion with Lists
# ==========================================
def sum_list(numbers: list) -> int:
    """
    Returns the sum of all numbers in a list recursively.
    Time Complexity: O(n) or O(n²) depending on slicing overhead.
    Space Complexity: O(n) call stack.
    """
    # Base case: Empty list sums to 0
    if not numbers:
        return 0
    # Recursive step: First element + sum of remaining elements
    return numbers[0] + sum_list(numbers[1:])


# ==========================================
# 3. Linear Search
# ==========================================
def linear_search(arr: list, target) -> int:
    """
    Searches for target linearly from start to end.
    Time Complexity: O(n) - May scan all elements in worst case.
    Space Complexity: O(1)
    """
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1


# ==========================================
# 4. Binary Search
# ==========================================
def binary_search(arr: list, target) -> int:
    """
    Searches for target using divide and conquer.
    
    Why does it need a sorted array?
    Binary Search compares the target with the middle element to eliminate half 
    of the remaining elements. This decision depends on the order guarantee:
    if target > mid, target MUST be on the right side. On an unsorted array, 
    we cannot make this assumption, which would break the algorithm.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return -1


# ==========================================
# 5. Bubble Sort
# ==========================================
def bubble_sort(arr: list) -> list:
    """
    Sorts array by repeatedly swapping adjacent elements out of order.
    Prints array state after each pass.
    
    Time Complexity: O(n²) worst/average case
    Space Complexity: O(1) in-place
    """
    n = len(arr)
    arr_copy = arr.copy()  # Avoid modifying original in place directly

    for i in range(n):
        swapped = False
        print(f"Pass {i + 1}:")
        
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                # Swap adjacent elements
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        
        print(f"  Result: {arr_copy}")
        
        # Optimization: If no elements were swapped, array is sorted
        if not swapped:
            break

    return arr_copy


if __name__ == "__main__":
    print("--- 1. Factorial ---")
    print(f"Recursive 5!: {factorial_recursive(5)}")
    print(f"Iterative 5!: {factorial_iterative(5)}\n")

    print("--- 2. Sum List ---")
    nums = [10, 20, 30, 40]
    print(f"Sum of {nums}: {sum_list(nums)}\n")

    print("--- 3 & 4. Searching ---")
    sample_list = [4, 2, 9, 1, 7, 5]
    sorted_list = sorted(sample_list)
    print(f"Linear Search for 7 in {sample_list}: Index {linear_search(sample_list, 7)}")
    print(f"Binary Search for 7 in {sorted_list}: Index {binary_search(sorted_list, 7)}\n")

    print("--- 5. Bubble Sort ---")
    bubble_sort([5, 1, 4, 2, 8])