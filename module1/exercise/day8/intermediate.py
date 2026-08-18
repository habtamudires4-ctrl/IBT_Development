"""
Day 8 Exercises: Intermediate Recursion, Sorting & Algorithms
"""

# ==========================================
# 6. Recursive Problems
# ==========================================
def reverse_string_recursive(s: str) -> str:
    """
    Reverses a string recursively.
    Time Complexity: O(n²) due to string slicing/concatenation.
    Space Complexity: O(n) call stack.
    """
    if len(s) <= 1:
        return s
    return reverse_string_recursive(s[1:]) + s[0]


def count_occurrences_recursive(arr: list, target) -> int:
    """
    Counts occurrences of a target in a list recursively.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not arr:
        return 0
    count = 1 if arr[0] == target else 0
    return count + count_occurrences_recursive(arr[1:], target)


# ==========================================
# 7. Sorting Comparison
# ==========================================
def selection_sort(arr: list) -> tuple:
    """
    Selection Sort: Finds minimum element and moves it to the front.
    Returns sorted list, comparison count, swap count.
    """
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1

    return arr, comparisons, swaps


def insertion_sort(arr: list) -> tuple:
    """
    Insertion Sort: Builds sorted array one item at a time by shifting elements.
    Returns sorted list, comparison count, swap count.
    """
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
        arr[j + 1] = key

    return arr, comparisons, swaps


# ==========================================
# 8. Two Pointer Technique
# ==========================================
def two_sum_sorted(arr: list, target: int) -> tuple:
    """
    Finds two numbers in a sorted array that add up to target using two pointers.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return arr[left], arr[right]
        elif current_sum < target:
            left += 1  # Need a larger sum, move left pointer right
        else:
            right -= 1  # Need a smaller sum, move right pointer left

    return None


if __name__ == "__main__":
    print("--- Recursive String Reversal ---")
    orig = "Addis Ababa"
    print(f"Original: {orig}")
    print(f"Reversed: {reverse_string_recursive(orig)}\n")

    print("--- Recursive Occurrences Count ---")
    test_list = [1, 3, 7, 3, 2, 3, 9]
    print(f"Occurrences of 3 in {test_list}: {count_occurrences_recursive(test_list, 3)}\n")

    print("--- Sorting Comparison ---")
    data = [29, 10, 14, 37, 13]
    sel_res, sel_comp, sel_swaps = selection_sort(data)
    ins_res, ins_comp, ins_swaps = insertion_sort(data)

    print(f"Original Array: {data}")
    print(f"Selection Sort: {sel_res} | Comparisons: {sel_comp}, Swaps: {sel_swaps}")
    print(f"Insertion Sort: {ins_res} | Comparisons: {ins_comp}, Swaps: {ins_swaps}\n")

    print("--- Two Pointer Technique ---")
    sorted_nums = [2, 7, 11, 15, 20]
    target_sum = 18
    pair = two_sum_sorted(sorted_nums, target_sum)
    print(f"Pair in {sorted_nums} summing to {target_sum}: {pair}")