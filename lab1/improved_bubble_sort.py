import random

if __name__ == "__main__":
    array = [random.randint(0, 100) for i in range(10)]  # random generation of array
    print("Start array is:", array)

    counter = 0  # count of comparisons
    for i in range(len(array)):  # iterating every element
        isSorted = True  # flag
        for j in range(len(array) - 1):  # iterating every element except the last
            counter += 1
            if array[j] > array[j+1]:                            # if next element bigger than current element
                array[j], array[j + 1] = array[j + 1], array[j]  # swap elements
                isSorted = False  # changing flag
        if isSorted:  # if no changes during current iteration - end sort
            break

    print("Final array is:", array)
    print("Number of operations:", counter)
