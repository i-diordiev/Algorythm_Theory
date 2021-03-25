array = [56, 64, 12, 5, 7, 89, 24, 16, 8, 45]

for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and key < array[j]:
        temp = array[j + 1]
        array[j + 1] = array[j]
        array[j] = temp
        j -= 1

print(array)
