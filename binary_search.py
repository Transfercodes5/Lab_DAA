import time
import random

random.seed(42)

def binary_search(arr, value, first, last):
    
    if last < first:
        return -1
    
    pivot = (first + last) // 2
    
    if arr[pivot] == value:
        return pivot
    
    elif value > arr[pivot]:
        return binary_search(arr, value, pivot+1, last)
        
    elif value < arr[pivot]:
        return binary_search(arr, value, first, pivot-1)
        
    else:
        return -1

arr = [9, 4, 3, 8, 10, 2, 5]

arr = [random.randint(1, 100) for _ in range(1000)]

arr = sorted(arr)

# print(arr)

value = 8

start_time = time.perf_counter()

print(f"Location of {value} in {arr} is {binary_search(arr, value, 0, len(arr)- 1)}")

end_time = time.perf_counter()

print("Total time taken: ", end_time-start_time)
