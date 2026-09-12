import time
import random

random.seed(42)

def linear_search(arr, value):
    
    for i in range(len(arr)):
        if arr[i] == value:
            return i
        
    return -1

arr = [9, 4, 3, 8, 10, 2, 5]

arr = [random.randint(1, 100) for _ in range(1000)]

value = 5

start_time = time.perf_counter()

print(f"Location of {value} in arr is {linear_search(arr, value)}")

end_time = time.perf_counter()

print("Total time taken: ", end_time-start_time)
