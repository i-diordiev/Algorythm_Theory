import random


def Merge(array, left, right):
    n1, n2 = len(left), len(right)  # number of left and right elements
    i, j, k = 0, 0, 0  # indexes for left, right and main arrays
    global counter
    while i < n1 and j < n2:
        counter += 1
        if left[i] <= right[j]:  # if current element of left array < of right array, setting it to main array
            array[k] = left[i]
            i += 1
        else:                    # else setting current element of right array
            array[k] = right[j]
            j += 1
        k += 1
    while i < n1:  # adding remains element of left array to main
        array[k] = left[i]
        i += 1
        k += 1
    while j < n2:  # adding remains element of right array to main
        array[k] = right[j]
        j += 1
        k += 1


def MergeSort(array):
    if len(array) > 1:  # if length of array > 1, sorting
        q = len(array) // 2  # dividing array into 2 parts
        left = array[:q]
        right = array[q:]
        MergeSort(left)  # recursively sorting left part of array
        MergeSort(right)  # recursively sorting right part of array
        Merge(array, left, right)  # merging both parts


if __name__ == "__main__":
    array = [random.randint(0, 100) for i in range(10)]  # random generation of array
    print("Start array is:", array)

    counter = 0  # count of comparisons
    MergeSort(array)

    print("Final array is:", array)
    print("Number of operations:", counter)
