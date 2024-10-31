import time

def binary_search(array_a, start, stop, target_value):
    mid = (start + stop)//2
    print("printing mid-point", mid)
    if start>stop:
        return -1
    if array_a[mid] < target_value:
        return binary_search(array_a, start, stop, target_value)
    
    elif array_a[mid] > target_value:
        return binary_search(array_a, start, mid-1, target_value)
    elif array_a[mid] == target_value:
        return mid
def main():
    array_a = [20, 30, 40 ,50, 60, 80, 90]
    target_value = int(input("Enter the value you want to search: "))
    begin = time.perf.counter()
    result = binary_search(array_a, 0, len(array_a) - 1, target_value)

    if result == -1:
        print("target value not found")
    else:
        print("target value found")

main()