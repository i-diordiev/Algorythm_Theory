import random

array = [random.randint(0, 100) for i in range(10)]
print("Start array is:", array)

for i in array:
    for j in range(len(array) - 1):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp

print("Final array is:", array)
