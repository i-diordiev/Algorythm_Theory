import random

array = [random.randint(0, 100) for i in range(10)]
print("Start array is:", array)

ops = 0
for i in array:
    isSorted = True
    for j in range(len(array) - 1):
        ops += 1
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp
            isSorted = False
    if isSorted:
        break

print("Final array is:", array)
print("Number of operations:", ops)
