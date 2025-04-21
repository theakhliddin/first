array1 = [6, 8, 2, 4, 5, 9, 7, 3]
array2 = [5, 12, 4, 1, 2, 8, 2, 6, 10]

# quick sort
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def main():
    sorted_array1 = quick_sort(array1)
    sorted_array2 = quick_sort(array2)
    print("Sorted Array 1:", sorted_array1)
    print("Sorted Array 2:", sorted_array2)

if __name__ == "__main__":
    main()



s = "Datascience"
print(s[4:])
print(s[::3])
print(s[1:8:2])
print(s[3:3])

