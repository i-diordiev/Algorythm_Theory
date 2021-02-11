import random

array = [random.randint(0, 100) for i in range(10)]
print("Start array is:", array)

for i in array:
    for j in range(len(array) - 1):
        if array[j] % 2:
            temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp

even_number = 0
for n in array:
    if n % 2:
        even_number += 1

for i in range(len(array) - even_number):
    for j in range(len(array) - even_number - 1):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp

for i in range(even_number - 1, len(array)):
    for j in range(even_number - 1, len(array) - 1):
        if array[j] < array[j+1]:
            temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp

print("Final array is:", array)
