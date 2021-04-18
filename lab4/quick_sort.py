import random


def Partition(array, left, right):
    pivot = array[right]  # pivot - last element of subarray
    global counter
    i = left - 1  # position of pivot after sorting
    for j in range(left, right):
        counter += 1
        if array[j] < pivot:  # if element < pivot - moving it before pivot
            i = i + 1  # moving pivot to the right
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]  # moving pivot on its position
    return i + 1


def QuickSort(array, left, right):
    if left < right:  # if length of subarray 2 or more - sorting
        q = Partition(array, left, right)  # q - position of current pivot
        QuickSort(array, left, q - 1)  # recursively sort left part of array
        QuickSort(array, q + 1, right)  # recursively sort right part of array


if __name__ == "__main__":
    array = [random.randint(0, 100) for i in range(10)]  # random generation of array
    print("Start array is:", array)

    counter = 0  # count of comparisons
    QuickSort(array, 0, len(array) - 1)

    print("Final array is:", array)
    print("Number of operations:", counter)
