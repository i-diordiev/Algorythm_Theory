import random


def Partition(array, left, right):
    global counter
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
            counter += 1
            counter += 1
            if array[b] < p:
                array[a], array[b] = array[b], array[a]
                a += 1
            b += 1
        counter += 1
        while array[c] > q and b <= c:
            counter += 1
            counter += 1
            if array[c] > r:
                array[c], array[d] = array[d], array[c]
                d -= 1
            c -= 1
        counter += 1
        if b <= c:
            counter += 1
            if array[b] > r:
                counter += 1
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
                counter += 1
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
        if right - left > 3:  # if length of subarray > 3, doing quick sort, else insertion sort
            q1, q2, q3 = Partition(array, left, right)  # q1, q2, q3 - 3 indexes of pivots
            QuickSort(array, left, q1 - 1)  # recursively sort array from left to q1
            QuickSort(array, q1 + 1, q2 - 1)  # recursively sort array from q1 to q2
            QuickSort(array, q2 + 1, q3 - 1)  # recursively sort array from q2 to q3
            QuickSort(array, q3 + 1, right)  # recursively sort array from q3 to right
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
