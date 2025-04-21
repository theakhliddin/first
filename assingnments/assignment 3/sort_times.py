import time
import random
import matplotlib.pyplot as plt
from sorts import insertion_sort, merge_sort, quick_sort, quick_insertion_sort

SIZES = [200, 500, 800, 1100, 1400, 1700, 2000]

def sort_function_timer(sort_func, arr):
    arr_copy = arr.copy()
    start = time.time()
    sort_func(arr_copy)
    return time.time() - start

def plot_sort_time_using_random_arrays(sort_func):
    print("Timing", sort_func.__name__)
    x, y = [], []
    for size in SIZES:
        data = [random.randint(0, size) for _ in range(size)]
        y.append(sort_function_timer(sort_func, data))
        x.append(size)
    return x, y

def plot_sort_time_using_sorted_z(sort_func):
    print("Timing", sort_func.__name__)
    x, y = [], []
    for size in SIZES:
        data = list(range(size))  # Sorted array
        y.append(sort_function_timer(sort_func, data))
        x.append(size)
    return x, y

def main():
    # First plot: Random arrays
    plt.figure("Random Arrays")
    plt.title("Performance on Random Data")
    plt.xlabel("Array Size")
    plt.ylabel("Time (s)")
    plt.ylim(0, 0.1)
    
    for algo in [insertion_sort, merge_sort, quick_sort, quick_insertion_sort]:
        x, y = plot_sort_time_using_random_arrays(algo)
        plt.plot(x, y, marker='.', label=algo.__name__)
    
    plt.legend()
    plt.grid()
    
    # Second plot: Sorted arrays
    plt.figure("Sorted Arrays")
    plt.title("Performance on Sorted Data")
    plt.xlabel("Array Size")
    plt.ylabel("Time (s)")
    plt.ylim(0, 0.1)
    
    for algo in [insertion_sort, merge_sort, quick_sort, quick_insertion_sort]:
        x, y = plot_sort_time_using_sorted_z(algo)
        plt.plot(x, y, marker='.', label=algo.__name__)

    plt.legend()
    plt.grid()

    # New test for hybrid sort
    plt.figure("Hybrid Sort Test")
    plt.ylim(0, 0.1)
    
    # Test hybrid on random data
    x_rand, y_rand = plot_sort_time_using_random_arrays(quick_insertion_sort)
    plt.plot(x_rand, y_rand, 'g--', label="Hybrid (Random)")
    plt.ylim(0, 0.1)
    
    # Test hybrid on sorted data
    x_sorted, y_sorted = plot_sort_time_using_sorted_z(quick_insertion_sort)
    plt.plot(x_sorted, y_sorted, 'm--', label="Hybrid (Sorted)")
    plt.ylim(0, 0.1)
    
    plt.legend()
    plt.show()
    input("Done? Press Enter...")

if __name__ == "__main__":
    main()