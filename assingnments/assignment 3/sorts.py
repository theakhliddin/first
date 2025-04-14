"""
This script contains sorting algorithms used for testing and comparison.
These functions follow the basic logic taught in class and are written
in a simple, clear manner without optimization or helper functions.

Functions:
insertion_sort() - Sorts using insertion sort (good for small or sorted data)
merge_sort() - Sorts using merge sort (split and merge method)
quick_sort() - Sorts using quick sort with last-element pivot
quick_insertion_sort() - Hybrid that uses quick sort but switches to insertion sort when depth is too deep
"""

# Insertion Sort
def insertion_sort(array):
    """
    Sorts an array using insertion sort.
    Starts from the second element and compares backward,
    placing it in the correct position in the sorted portion.
    """
    for index in range(1, len(array)):
        current_value = array[index]
        compare_index = index - 1
        while compare_index >= 0 and array[compare_index] > current_value:
            array[compare_index + 1] = array[compare_index]
            compare_index -= 1
        array[compare_index + 1] = current_value
    return array

# Merge Sort
def merge_sort(array):
    """
    Sorts an array using merge sort.
    Splits array into halves, sorts each, and merges them back together.
    """
    if len(array) <= 1:
        return array

    middle_index = len(array) // 2
    left_half = merge_sort(array[:middle_index])
    right_half = merge_sort(array[middle_index:])

    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(right_half[right_index])
            right_index += 1
    while left_index < len(left_half):
        merged.append(left_half[left_index])
        left_index += 1
    while right_index < len(right_half):
        merged.append(right_half[right_index])
        right_index += 1

    return merged

# Quick Sort
def quick_sort(array):
    """
    Sorts an array using quick sort.
    Uses the middle element as pivot to avoid worst-case recursion on sorted arrays.
    """
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Hybrid Quick-Insertion Sort
def quick_insertion_sort(an_array, depth=0, max_depth=None):
    """
    Sorts using quick sort, but switches to insertion sort
    if recursion gets too deep. Useful when input is sorted.
    """
    if len(an_array) < 2:
        return an_array

    if max_depth is None:
        max_depth = 2 * (len(an_array).bit_length())

    if depth >= max_depth:
        return insertion_sort(an_array[:])

    pivot = an_array[-1]
    lower_values = [element for element in an_array[:-1] if element <= pivot]
    higher_values = [element for element in an_array[:-1] if element > pivot]

    sorted_lower = quick_insertion_sort(lower_values, depth + 1, max_depth)
    sorted_higher = quick_insertion_sort(higher_values, depth + 1, max_depth)

    return sorted_lower + [pivot]+sorted_higher