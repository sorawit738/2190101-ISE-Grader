import module
import time
import random

# Generate an array of 200 unordered integers

array_size = 40000000
min_value = 0
max_value = 10000
#unordered_array = [random.randint(min_value, max_value) for _ in range(array_size)]

#print(unordered_array)
#print("\n")

arr = [0, -1, -2, 2, 1]

start = time.time()

#module.quickSort(unordered_array, 0, len(arr) - 1)
#print(unordered_array)
#print(module.insertionSort(unordered_array))
#print(module.selectionSort(unordered_array))
#module.mergeSort(unordered_array, 0, len(unordered_array) - 1)
#print(unordered_array)
print(module.binarySearch(arr, -2))

end = time.time()
print("\n")
print("--- %s miliseconds ---" % ((end - start) * 1000))