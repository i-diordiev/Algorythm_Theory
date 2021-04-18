import random

if __name__ == "__main__":
    array = [random.randint(0, 100) for i in range(10)]  # random generation of array
    print("Start array is:", array)

    counter = 0  # count of comparisons
    for i in range(1, len(array)):  # iterating every element except the first
        key = array[i]  # element to sort
        j = i - 1
        while j >= 0 and key < array[j]:                     # if previous element is bigger than key element
            array[j], array[j + 1] = array[j + 1], array[j]  # swap elements
            counter += 1
            j -= 1
        counter += 1  # counting the last, unsuccessful comparison

    print("Final array is:", array)
    print("Number of operations:", counter)
