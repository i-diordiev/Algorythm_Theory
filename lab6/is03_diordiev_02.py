def Parent(i):  # returning index of parent element
    return i // 2


def Left(i):  # returning index of left element
    return 2 * i


def Right(i):  # returning index of right element
    return 2 * i + 1


def MaxHeapify(A, i):  # procedure to restore property of max heap
    p = Left(i)
    q = Right(i)
    if p < len(A) and A[p] > A[i]:  # choosing element to swap with node
        largest = p
    else:
        largest = i
    if q < len(A) and A[q] > A[largest]:
        largest = q
    if largest != i:
        A[i], A[largest] = A[largest], A[i]  # swapping elements
        MaxHeapify(A, largest)  # recursively run


def MinHeapify(A, i):  # procedure to restore property of min heap
    p = Left(i)
    q = Right(i)
    if p < len(A) and A[p] < A[i]:  # choosing element to swap with node
        smallest = p
    else:
        smallest = i
    if q < len(A) and A[q] < A[smallest]:
        smallest = q
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]  # swapping elements
        MinHeapify(A, smallest)  # recursively run


def MaxHeapIncreaseKey(A, i, key):  # procedure to move key element A[i] to his position in max heap
    A[i] = key
    while i > 0 and A[Parent(i)] < A[i]:  # while element < his parent, moving it up
        A[i], A[Parent(i)] = A[Parent(i)], A[i]
        i = Parent(i)


def MinHeapDecreaseKey(A, i, key):  # procedure to move key element A[i] to his position in min heap
    A[i] = key
    while i > 0 and A[Parent(i)] > A[i]:  # while element > his parent, moving it up
        A[i], A[Parent(i)] = A[Parent(i)], A[i]
        i = Parent(i)


def MaxHeapInsert(A, key):  # procedure to insert element into max heap
    heap_size = len(A)
    A.append(key)
    MaxHeapIncreaseKey(A, heap_size, key)


def MinHeapInsert(A, key):  # procedure to insert element into min heap
    heap_size = len(A)
    A.append(key)
    MinHeapDecreaseKey(A, heap_size, key)


def HeapExtractMax(A):  # procedure to return max element from max heap without property violation
    max = A.pop(0)  # getting element
    MaxHeapify(A, 0)  # restoring structure of heap
    return max


def HeapExtractMin(A):  # procedure to return min element from min heap without property violation
    min = A.pop(0)  # getting element
    MinHeapify(A, 0)  # restoring structure of heap
    return min


if __name__ == "__main__":
    file_name = input("Type file name: ")  # reading data from file
    with open(file_name, "r") as file:
        source = file.readlines()

    n = int(source[0].strip())
    array = [int(source[i + 1].strip()) for i in range(n)]

    Hhigh = []  # min heap
    Hlow = []  # max heap

    f = open("is03_diordiev_02_output.txt", "w")
    for i in range(n):
        element = array[i]

        # deciding where to add element
        if len(Hlow) == 0:  # if Hlow heap is empty, write
            Hlow.append(element)
        elif len(Hhigh) == 0:  # if Hhigh heap is empty, write
            Hhigh.append(element)
        elif element < Hlow[0]:  # if element less that the largest element of Hlow, write
            MaxHeapInsert(Hlow, element)
        else:  # else write to Hhigh
            MinHeapInsert(Hhigh, element)

        # checking difference between size of both heaps
        if abs(len(Hlow) - len(Hhigh)) > 1:  # if it's 2 or more, extracting element from 1 heap and insert it to 2
            if len(Hhigh) > len(Hlow):
                temp = HeapExtractMin(Hhigh)
                MaxHeapInsert(Hlow, temp)
            else:
                temp = HeapExtractMax(Hlow)
                MinHeapInsert(Hhigh, temp)

        # if total size of both heaps is odd, there is 1 median
        if (i + 1) % 2:
            if len(Hlow) > len(Hhigh):  # if size of Hlow > size of Hhigh, median is in Hlow
                f.write(str(Hlow[0]) + "\n")
            else:  # else median is in Hhigh
                f.write(str(Hhigh[0]) + "\n")
        else:  # else there is 2 median, they are in both heaps
            m1 = Hlow[0]
            m2 = Hhigh[0]
            f.write(str(Hlow[0]) + " " + str(Hhigh[0]) + "\n")
    f.close()
