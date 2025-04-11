# -------------------- Sorting Algorithms --------------------

def insertion_sort(an_array):
    """
    Sorts an array using the insertion sort algorithm.
    
    Args:
        an_array: The array to be sorted
        
    Returns:
        The sorted array
    """
    result = an_array.copy()
    
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        
        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1
            
        result[j + 1] = current
        
    return result

def merge_sort(an_array):
    """
    Sorts an array using the merge sort algorithm.
    
    Args:
        an_array: The array to be sorted
        
    Returns:
        The sorted array
    """
    # Base case
    if len(an_array) < 2:
        return an_array
    
    # Split the array into two halves
    mid = len(an_array) // 2
    left = merge_sort(an_array[:mid])
    right = merge_sort(an_array[mid:])
    
    # Merge the two sorted halves
    return merge(left, right)

def merge(left, right):
    """
    Merges two sorted arrays into a single sorted array.
    Helper function for merge_sort.
    
    Args:
        left: First sorted array
        right: Second sorted array
        
    Returns:
        A merged sorted array
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    # Add any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def quick_sort(an_array):
    """
    Sorts an array using the quick sort algorithm (iterative implementation).
    
    Args:
        an_array: The array to be sorted
        
    Returns:
        The sorted array
    """
    # Make a copy to avoid modifying the original
    array = an_array.copy()
    
    # Use an iterative approach with a stack
    def _quick_sort_iterative(arr, low, high):
        # Create an auxiliary stack
        stack = []
        
        # Push initial values to stack
        stack.append(low)
        stack.append(high)
        
        # Keep popping from stack while it's not empty
        while stack:
            # Pop high and low
            high = stack.pop()
            low = stack.pop()
            
            # Set pivot element at its correct position
            # Improved pivot selection using median-of-three
            if high - low > 1:
                mid = (low + high) // 2
                if arr[low] > arr[mid]:
                    arr[low], arr[mid] = arr[mid], arr[low]
                if arr[low] > arr[high]:
                    arr[low], arr[high] = arr[high], arr[low]
                if arr[mid] > arr[high]:
                    arr[mid], arr[high] = arr[high], arr[mid]
                
                pivot = arr[mid]
                
                # Partition using the pivot
                i = low
                j = high
                
                while i <= j:
                    while arr[i] < pivot:
                        i += 1
                    while arr[j] > pivot:
                        j -= 1
                    
                    if i <= j:
                        arr[i], arr[j] = arr[j], arr[i]
                        i += 1
                        j -= 1
                
                # If there are elements on the left side of pivot,
                # push left side to stack
                if low < j:
                    stack.append(low)
                    stack.append(j)
                    
                # If there are elements on the right side of pivot,
                # push right side to stack
                if i < high:
                    stack.append(i)
                    stack.append(high)
    
    if len(array) > 1:
        _quick_sort_iterative(array, 0, len(array) - 1)
    
    return array

def quick_insertion_sort(an_array):
    """
    A hybrid sorting algorithm that combines quicksort and insertion sort.
    Uses quicksort for initial partitioning but switches to insertion sort
    when the array size becomes small or when quicksort is detected to be
    inefficient (such as with nearly sorted arrays).
    
    Args:
        an_array: The array to be sorted
        
    Returns:
        The sorted array
    """
    # Make a copy to avoid modifying the original
    array = an_array.copy()
    
    # Insertion sort for small arrays
    def _insertion_sort(arr, low, high):
        for i in range(low + 1, high + 1):
            key = arr[i]
            j = i - 1
            while j >= low and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
    
    # Iterative quicksort with cutoff to insertion sort
    def _hybrid_sort(arr, low, high):
        # Create an auxiliary stack
        stack = []
        
        # Push initial values to stack
        stack.append(low)
        stack.append(high)
        
        # Keep popping from stack while it's not empty
        while stack:
            # Pop high and low
            high = stack.pop()
            low = stack.pop()
            
            # Use insertion sort for small subarrays
            if high - low + 1 <= 20:
                _insertion_sort(arr, low, high)
                continue
            
            # Set pivot element at its correct position
            # Improved pivot selection using median-of-three
            mid = (low + high) // 2
            if arr[low] > arr[mid]:
                arr[low], arr[mid] = arr[mid], arr[low]
            if arr[low] > arr[high]:
                arr[low], arr[high] = arr[high], arr[low]
            if arr[mid] > arr[high]:
                arr[mid], arr[high] = arr[high], arr[mid]
            
            pivot = arr[mid]
            
            # Partition using the pivot
            i = low
            j = high
            
            while i <= j:
                while arr[i] < pivot:
                    i += 1
                while arr[j] > pivot:
                    j -= 1
                
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
            
            # Check for unbalanced partitions
            left_size = j - low + 1
            right_size = high - i + 1
            total_size = high - low + 1
            
            # If partitioning is poor, use insertion sort
            if (left_size > 0 and left_size > 0.9 * total_size) or (right_size > 0 and right_size > 0.9 * total_size):
                _insertion_sort(arr, low, high)
                continue
            
            # Push subarrays to stack
            if low < j:
                stack.append(low)
                stack.append(j)
                
            if i < high:
                stack.append(i)
                stack.append(high)
    
    if len(array) > 1:
        _hybrid_sort(array, 0, len(array) - 1)
    
    return array
    