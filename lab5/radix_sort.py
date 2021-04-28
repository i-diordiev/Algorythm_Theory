import random


def CountingSort(A, grade, k=10):
    TempArray = [0 for i in range(k)]  # array with quantity of digits
    OutputArray = [0 for i in range(len(A))]  # sorted array
    divider = 10 ** grade  # divider to get digit from number

    for i in range(0, len(A)):  # filling array with quantity of digits
        # on this stage array contains only quantity of digits that equal to current digit
        index = A[i] // divider % 10  # digit of number
        TempArray[index] += 1

    for i in range(1, k):  # completing filling array
        # on this stage array contains only quantity of digits that not less than current digit
        TempArray[i] += TempArray[i - 1]

    j = len(A) - 1  # iterating every number in array from the last element
    while j >= 0:
        index = A[j] // divider % 10  # digit of number
        OutputArray[TempArray[index] - 1] = A[j]  # setting current element to its position
        TempArray[index] -= 1  # decreasing remaining quantity of number with this digit
        j -= 1

    for i in range(len(A)):  # copying data from output to main array
        A[i] = OutputArray[i]


def RadixSort(A, d):
    for i in range(d):  # for every grade in number doing counting sort
        CountingSort(A, i)


if __name__ == "__main__":
    array = [random.randint(100, 1000) for i in range(10)]  # random generation of array
    print("Start array is:", array)

    RadixSort(array, 3)

    print("Final array is:", array)
