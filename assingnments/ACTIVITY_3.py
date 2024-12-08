'''Activity 3 - Group 8
This activity requires us to understand the various algorithms for searching and sorting a dataset by 
comparing and contrasting the different algorithms.'''

# This is the link to Mohammed Eshaans's github repository : https://github.com/me3574/NoTrofy2.0
# This is the link to Mohammad Saad's github repository : https://github.com/ms5810/GCIS-Group-9.git
# This is the link to Akhliddin Koziboev's github repository : https://github.com/theakhliddin/first/tree/master
# This is the link to Danay Sultanov's github repository : https://github.com/ds4449/swag.inc.git

#Importing required modules
import array as arr
import time
import random as ran



#Phase 1 : Akhliddin
'''Phase 1 objective is to create a function which takes a size as input in order to create an Array of
said size filled with random numbers ranging from 1-100 and then sort the array using the insertion sort algorithm'''


'''function that takes array as argument and sorts it using an insertion sort algorithm'''
def insertion_sort(ar):
    for i in range(1,len(ar)):
        j=i                                  
        while j>0:
            if ar[j]<ar[j-1]:
                ar[j],ar[j-1]=ar[j-1],ar[j]
            j-=1
    return ar
 
'''function to generate the random array of fixed size and fill it with random numbers.
Then use the previous function to sort it.'''
def generate_data_sort(size):
    ar=[]
    for i in range(size):                
        ar.append(ran.randint(1,100))        
    result=insertion_sort(ar)
    return result



#Phase 2 : Danay
'''Phase 2 objective is to create a code that runs the binary search algorithm so that it can be used on the previously
sorted array to return the index of the required target.'''

'''Function that runs the binary search algorithm'''
def binary_algorithm(array,start,end,target):
    mid=(start+end)//2
    if start>end:
        return -1
    elif target==array[mid]:
        return mid
    elif target>array[mid]:
        return binary_algorithm(array,mid+1,end,target)
    elif target<array[mid]:
        return binary_algorithm(array,start,mid-1,target)
    
'''Function that takes sorted array as argument and searched for required target using binary algorithm'''
def binary_search(array,target):
    start=0
    end=len(array)-1
    result=binary_algorithm(array,start,end,target)
    print("The index value for the searched target is:",result)
    return result


#Phase 3 : Eshaan
'''Phase 3 objective is to create a code that runs a merge sort algorithm that can sort arrays of much larger sizes'''

'''Function that sorts and merges the 2 halves of the array'''
def merge_algorithm(ar,start,end):
    mid=(start+end)//2
    left=ar[start:mid+1]
    right=ar[mid+1:end+1]
    i,j,next=0,0,start
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            ar[next]=left[i]
            i+=1
        else:
            ar[next]=right[j]
            j+=1
        next+=1
    while i<len(left):
        ar[next]=left[i]
        i+=1
        next+=1
    while j<len(right):
        ar[next]=right[j]
        j+=1
        next+=1
    return ar

'''Function that splits array to 2 halves in order for each half to be sorted in divide and conquer method'''
def merge_sort_algorithm(ar,start,end):
    if start==end:
        return ar
    else:
        mid=(start+end)//2
        merge_sort_algorithm(ar,start,mid)
        merge_sort_algorithm(ar,mid+1,end)
        merge_algorithm(ar,start,end)
        return ar
            
    
'''seperate function for generating and sorting larger arrays'''
def generate_large_data_sort(size):
    ar=[]
    for i in range(size):                
        ar.append(ran.randint(1,100))      
    result=merge_sort_algorithm(ar,0,(len(ar)-1))
    return result


#Phase 4 : Saad
'''Phase 4 objective is to define a function that runs linear search algorithm to find and
return index value of the target.
we also have to use binary search and linear search on the same array and compare their times.'''

'''Function that runs linear search algorithm'''
def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

'''Function that searches array using linear and binary methods and prints time taken for both'''
def compare_search_times(array, target):
    '''Linear search and time'''
    start_time = time.perf_counter()
    linear_search_result = linear_search(array, target)
    linear_search_time = time.perf_counter() - start_time
    print(f"Linear Search Result: ", (linear_search_result))
    print(f"Time: {linear_search_time:.10f} seconds")
    '''Binary search and time'''
    start_time2 = time.perf_counter()
    binary_search_result = binary_search(array, target)
    binary_search_time = time.perf_counter() - start_time2
    print(f"Binary Search Result: ", (binary_search_result)) 
    print(f"Time: {binary_search_time:.10f} seconds")


        
'''Main function definition'''
def main():
    target=int(input("Enter target to be searched in random sorted array to compare search times:"))
    array1=generate_large_data_sort(20)
    compare_search_times(array1,target)
    
if __name__=="__main__":
    main()