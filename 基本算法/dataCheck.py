import random
from time import time
from .quicksort import quick_sort

arr1 = []
for i in range(random.randint(0, 10000)):
    arr1.append(random.randint(0, 10000))

start_time1 = time()
arr2 = sorted(arr1.copy())
end_time1 = time()

start_time2 = time()
arr3 = quick_sort(arr1.copy())
end_time2 = time()

if arr2 == arr3:
    print("Time 1: ", end_time1 - start_time1)
    print("Time 2: ", end_time2 - start_time2)
else:
    print("error: ", arr1)
