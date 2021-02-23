array = [56, 64, 12, 5, 7, 89, 24, 16, 0, 45]

for i in range(1, len(array)):
    j = i - 1
    while j >= 0 and array[i] < array[j]:
        temp = array[j]
        array[j] = array[j - 1]
        array[j - 1] = temp
        j -= 1
