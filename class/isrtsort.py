def insertion_sort(arr):
    for i in range(1, len(arr)):
          j = 1
          while arr[j - 1] > arr[j] and j > 0:
               arr[j - 1], arr[j] = arr[j], arr[j - 1]
               j -= 1

arr = [2, 6, 4, 5, 7, 1, 3,]
insertion_sort(arr)
print(arr)
