import random


def Partition(array, left, right):
    '''
    choosing an average element of A[left], A[right], A[mid]
    and moving it to the right position
    '''
    low, mid, high = left, (left + right) // 2, right
    if array[low] <= array[mid] <= array[high] or array[high] <= array[mid] <= array[low]:
        array[mid], array[right] = array[right], array[mid]
    elif array[mid] <= array[low] <= array[high] or array[high] <= array[low] <= array[mid]:
        array[low], array[right] = array[right], array[low]
    pivot = array[right]  # pivot - last element of subarray
    global counter
    i = left - 1  # position of pivot after sorting
    for j in range(left, right):  # iterating every element
        counter += 1
        if array[j] < pivot:  # if element < pivot - moving it before pivot
            i = i + 1  # moving pivot to the right
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]  # moving pivot on its position
    return i + 1


def QuickSort(array, left, right):
    if left < right:  # if length of subarray 2 or more - sorting
        if right - left > 3:  # if length of subarray > 3, doing quick sort, else insertion sort
            q = Partition(array, left, right)  # q - position of current pivot
            QuickSort(array, left, q - 1)  # recursively sort left part of array
            QuickSort(array, q + 1, right)  # recursively sort right part of array
        else:
            global counter
            for i in range(left + 1, right + 1):  # insertion sort
                key = array[i]
                j = i - 1
                while j >= 0 and key < array[j]:
                    counter += 1
                    array[j + 1], array[j] = array[j], array[j + 1]
                    j -= 1
                counter += 1


if __name__ == "__main__":
    array = [random.randint(0, 100) for i in range(10)]  # random generation of array
    print("Start array is:", array)

    counter = 0  # count of comparisons
    QuickSort(array, 0, len(array) - 1)

    print("Final array is:", array)
    print("Number of operations:", counter)
