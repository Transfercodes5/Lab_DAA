import time

def heapify(arr, n, i):

    largest = i

    l = 2 * i + 1

    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):

        arr[0], arr[i] = arr[i], arr[0]

        heapify(arr, i, 0)

arr = [9, 4, 3, 8, 10, 2, 5]

start_time = time.perf_counter()

heapSort(arr)

end_time = time.perf_counter()

print("Total time taken: ", end_time-start_time)

for i in range(len(arr)):
    print(arr[i], end=" ")

print()