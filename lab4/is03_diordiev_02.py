def Partition(array, left, right):
    pivot = array[right]  # pivot - last element of subarray
    global comparisons1
    i = left - 1  # position of pivot after sorting
    for j in range(left, right):
        comparisons1 += 1
        if array[j] < pivot:  # if element < pivot - moving it before pivot
            i = i + 1  # moving pivot to the right
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]  # moving pivot on its position
    return i + 1


def PartitionThreeMedian(array, left, right):
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
    global comparisons2
    i = left - 1  # position of pivot after sorting
    for j in range(left, right):
        comparisons2 += 1
        if array[j] < pivot:  # if element < pivot - moving it before pivot
            i = i + 1  # moving pivot to the right
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]  # moving pivot on its position
    return i + 1


def PartitionThreePivot(array, left, right):
    global comparisons3
    a, b = left + 2, left + 2  # a, b, d - indexes of first, second and third pivot
    c, d = right - 1, right - 1

    temp_array = [array[left], array[left + 1], array[right]]  # array with 3 values of pivots
    for i in range(1, 3):                                      # sorting it, because q1 < q2 < q3 needed
        key = temp_array[i]
        j = i - 1
        while j >= 0 and key < temp_array[j]:
            temp_array[j + 1], temp_array[j] = temp_array[j], temp_array[j + 1]
            j -= 1
    array[left], array[left + 1], array[right] = temp_array[0], temp_array[1], temp_array[2]

    p, q, r = array[left], array[left + 1], array[right]  # 3 pivots
    while b <= c:
        while array[b] < q and b <= c:
            comparisons3 += 1
            comparisons3 += 1
            if array[b] < p:
                array[a], array[b] = array[b], array[a]
                a += 1
            b += 1
        comparisons3 += 1
        while array[c] > q and b <= c:
            comparisons3 += 1
            comparisons3 += 1
            if array[c] > r:
                array[c], array[d] = array[d], array[c]
                d -= 1
            c -= 1
        comparisons3 += 1
        if b <= c:
            comparisons3 += 1
            if array[b] > r:
                comparisons3 += 1
                if array[c] < p:
                    array[b], array[a] = array[a], array[b]
                    array[a], array[c] = array[c], array[a]
                    a += 1
                else:
                    array[b], array[c] = array[c], array[b]
                array[c], array[d] = array[d], array[c]
                b += 1
                c -= 1
                d -= 1
            else:
                comparisons3 += 1
                if array[c] < p:
                    array[b], array[a] = array[a], array[b]
                    array[a], array[c] = array[c], array[a]
                    a += 1
                else:
                    array[b], array[c] = array[c], array[b]
                b += 1
                c -= 1
    a -= 1
    b -= 1
    c += 1
    d += 1
    array[left + 1], array[a] = array[a], array[left + 1]
    array[a], array[b] = array[b], array[a]
    a -= 1
    array[left], array[a] = array[a], array[left]
    array[right], array[d] = array[d], array[right]
    return a, b, d


def QuickSort(array, left, right):
    if left < right:  # if length of subarray 2 or more - sorting
        q = Partition(array, left, right)  # q - position of current pivot
        QuickSort(array, left, q - 1)  # recursively sort left part of array
        QuickSort(array, q + 1, right)  # recursively sort right part of array


def QuickSortThreeMedian(array, left, right):
    if left < right:  # if length of subarray 2 or more - sorting
        if right - left > 3:  # if length of subarray > 3, doing quick sort, else insertion sort
            q = PartitionThreeMedian(array, left, right)  # q - position of current pivot
            QuickSortThreeMedian(array, left, q - 1)  # recursively sort left part of array
            QuickSortThreeMedian(array, q + 1, right)  # recursively sort right part of array
        else:
            global comparisons2
            for i in range(left + 1, right + 1):  # insertion sort
                key = array[i]
                j = i - 1
                while j >= 0 and key < array[j]:
                    comparisons2 += 1
                    array[j + 1], array[j] = array[j], array[j + 1]
                    j -= 1
                comparisons2 += 1


def QuickSortThreePivot(array, left, right):
    if left < right:  # if length of subarray 2 or more - sorting
        if right - left > 3:  # if length of subarray > 3, doing quick sort, else insertion sort
            q1, q2, q3 = PartitionThreePivot(array, left, right)  # q1, q2, q3 - 3 indexes of pivots
            QuickSortThreePivot(array, left, q1 - 1)  # recursively sort array from left to q1
            QuickSortThreePivot(array, q1 + 1, q2 - 1)  # recursively sort array from q1 to q2
            QuickSortThreePivot(array, q2 + 1, q3 - 1)  # recursively sort array from q2 to q3
            QuickSortThreePivot(array, q3 + 1, right)  # recursively sort array from q3 to right
        else:
            global comparisons3
            for i in range(left + 1, right + 1):  # insertion sort
                key = array[i]
                j = i - 1
                while j >= 0 and key < array[j]:
                    comparisons3 += 1
                    array[j + 1], array[j] = array[j], array[j + 1]
                    j -= 1
                comparisons3 += 1


if __name__ == "__main__":
    file_name = input("Type file name: ")
    with open(file_name, "r") as file:
        source = file.readlines()

    data1, data2, data3 = [0 for i in range(1, len(source))], [0 for i in range(1, len(source))], [0 for i in range(1, len(source))]
    for i in range(len(data1)):
        data1[i], data2[i], data3[i] = int(source[i + 1].strip()), int(source[i + 1].strip()), int(source[i + 1].strip())
    comparisons1 = 0
    comparisons2 = 0
    comparisons3 = 0
    QuickSort(data1, 0, len(data1) - 1)
    QuickSortThreeMedian(data2, 0, len(data2) - 1)
    QuickSortThreePivot(data3, 0, len(data3) - 1)

    with open("is03_diordiev_02_output.txt", "w") as file:
        file.write(str(comparisons1) + " " + str(comparisons2) + " " + str(comparisons3))
