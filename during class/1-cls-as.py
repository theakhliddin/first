array1 = [6, 8, 2, 4, 5, 9, 7, 3]
array2 = [5, 12, 4, 1, 2, 8, 2, 6, 10]

# merge sort
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])
    return merge(left_half, right_half)
    
    # merge function to combine two sorted arrays
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def main():
    sorted_array1 = merge_sort(array1)
    sorted_array2 = merge_sort(array2)
    print("Sorted Array 1:", sorted_array1)
    print("Sorted Array 2:", sorted_array2)

if __name__ == "__main__":
    main()