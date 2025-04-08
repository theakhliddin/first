def swap_halves(lst):
    mid = len(lst) // 2

    if len(lst) % 2 != 0:
        mid += 1
    return lst[mid:] + lst[:mid]

original_list = [1, 2, 3, 4, 5, 6]
swapped_list = swap_halves(original_list)
print("Original list:", original_list)
print("Swapped list:", swapped_list)