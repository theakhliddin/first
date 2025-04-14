import math

# Insertion Sort (as provided)
def insertion_sort(array):
    for index in range(1, len(array)):
        current_value = array[index]
        compare_index = index - 1
        while compare_index >= 0 and array[compare_index] > current_value:
            array[compare_index + 1] = array[compare_index]
            compare_index -= 1
        array[compare_index + 1] = current_value
    return array

# Merge Sort implementation
def merge_sort(array):
    if len(array) <= 1:
        return array.copy()
    
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    merged += left[i:]
    merged += right[j:]
    return merged

# Fixed Quick Sort with better pivot selection
def quick_sort(array):
    if len(array) <= 1:
        return array.copy()
    
    # Median-of-three pivot selection
    first = array[0]
    mid = array[len(array)//2]
    last = array[-1]
    pivot = sorted([first, mid, last])[1]
    
    lower = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    higher = [x for x in array if x > pivot]
    
    return quick_sort(lower) + equal + quick_sort(higher)

# Fixed Hybrid Sort with recursion depth control
def quick_insertion_sort(array, depth=0):
    if len(array) <= 15:
        arr_copy = array.copy()
        insertion_sort(arr_copy)
        return arr_copy
    
    # Prevent excessive recursion
    max_depth = 2 * math.floor(math.log2(len(array)))
    if depth > max_depth:
        arr_copy = array.copy()
        insertion_sort(arr_copy)
        return arr_copy
    
    # Improved pivot selection
    first = array[0]
    mid = array[len(array)//2]
    last = array[-1]
    pivot = sorted([first, mid, last])[1]
    
    lower = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    higher = [x for x in array if x > pivot]
    
    return (quick_insertion_sort(lower, depth+1) +
            equal +
            quick_insertion_sort(higher, depth+1))