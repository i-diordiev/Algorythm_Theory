import random

if __name__ == "__main__":
    array = [random.randint(0, 100) for i in range(10)]  # random generation of array
    print("Start array is:", array)

    '''
    moving even numbers to left part of array, odd numbers - to right part
    '''

    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] % 2:
                array[j], array[j + 1] = array[j + 1], array[j]

    '''
    counting odd numbers
    '''

    odd_number = 0
    for n in array:
        if n % 2:
            odd_number += 1

    '''
    sorting left part of array using bubble sort
    '''

    for i in range(len(array) - odd_number):
        for j in range(len(array) - odd_number - 1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    '''
    sorting right part of array using bubble sort
    '''

    for i in range(len(array) - odd_number, len(array)):
        for j in range(len(array) - odd_number, len(array) - 1):
            if array[j] < array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    print("Final array is:", array)
