#1
list_b = [n for n in range(2,15,3)]
print(list_b) #2,5,8,11,14

#2
a_list2 = ["Hat", "water", "Pen", "is", "Good"]
a_list2.sort(key=str.lower)
print(a_list2) #['Good', 'Hat', 'is', 'Pen', 'water']

#3
setE = {5, 6, 7, 8}
setF = {6, 7, 8, 9, 10}
print(setE.issubset(setF)) #False

#4

def computer_value(x):
    cube = x ** 3
    reminder = cube % 5
    print(reminder)
computer_value(7) #3

#5
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

array = [7, 3, 5, 1, 8, 6, 2, 4]
sorted_array = insertion_sort(array)
print(sorted_array) #[1, 2, 3, 4, 5, 6, 7, 8]

#6
    """
    push(10) [10]
    push(4) [10, 4]
    pop() [10]
    push(7) [10, 7]
    push(2) [10, 7, 2]
    pop() [10, 7]
    """

#7

    """
    enqueue(11) [11]
    enqueue(22) [11, 22]
    dequeue() [22]
    enqueue(44) [22, 44]
    dequeue() [44]
    enqueue(77) [44, 77]    
    """

#8
"""
    "Bubble Sort": {"Best": "O(n)", "Average": "O(n^2)", "Worst": "O(n^2)"},
    "Selection Sort": {"Best": "O(n^2)", "Average": "O(n^2)", "Worst": "O(n^2)"},
    "Insertion Sort": {"Best": "O(n)", "Average": "O(n^2)", "Worst": "O(n^2)"},
    "Merge Sort": {"Best": "O(n log n)", "Average": "O(n log n)", "Worst": "O(n log n)"},
    "Quick Sort": {"Best": "O(n log n)", "Average": "O(n log n)", "Worst": "O(n^2)"},
    "Heap Sort": {"Best": "O(n log n)", "Average": "O(n log n)", "Worst": "O(n log n)"},
    "Radix Sort": {"Best": "O(nk)", "Average": "O(nk)", "Worst": "O(nk)"},
"""
#9c
class Book:
    __slots__ = ['__title', '__isbn']

    def __init__(self, title: str, isbn: int):
        self.__title = title
        self.__isbn = isbn

    def get_isbn(self) -> int:
        return self.__isbn
    

def function(num):
    result = num % 2 == 0 and not num % 4 == 0
    return result

def main():
    print(function(6))  # True
    print(function(8))  # False

if __name__ == "__main__":
    main()
    