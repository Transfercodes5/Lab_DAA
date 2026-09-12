import time
import random

random.seed(42)

def partition(arr, low, high):

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[high], arr[i+1] = arr[i+1], arr[high]
    return i+1

def quick_sort(arr, low, high):

    if low < high:

        mid = partition(arr, low, high)

        quick_sort(arr, low, mid-1)
        quick_sort(arr, mid+1, high)

def is_sorted(iterable, reverse=False):
    return iterable == sorted(iterable, reverse=reverse)

arr = [7, 5, 2, 4, 7, 1, 3]

arr = [random.randint(1, 100) for _ in range(1000)]

start_time = time.perf_counter()

quick_sort(arr, 0, len(arr) - 1)

end_time = time.perf_counter()

print("Total time taken: ", end_time-start_time)

print(f"Is sorted : {is_sorted(arr)}")