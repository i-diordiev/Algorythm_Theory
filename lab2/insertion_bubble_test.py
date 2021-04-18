import random
import numpy as np
from create_plot import plot_data


def generate_data(n, gen_type="random"):
    if gen_type == "best":
        a = [i + 1 for i in range(n)]
    elif gen_type == "worst":
        a = [i + 1 for i in reversed(range(n))]
    else:
        a = [i + 1 for i in range(n)]
        random.shuffle(a)
    return a


def bubble_sort(array):
    counter = 0  # count of comparisons
    for i in range(len(array)):  # iterating every element
        for j in range(len(array) - 1):  # iterating every element except the last
            counter += 1
            if array[j] > array[j + 1]:  # if next element bigger than current element
                array[j], array[j + 1] = array[j + 1], array[j]  # swap elements
    return counter


def bubble_impr_sort(array):
    counter = 0  # count of comparisons
    for i in range(len(array)):  # iterating every element
        isSorted = True  # flag
        for j in range(len(array) - 1):  # iterating every element except the last
            counter += 1
            if array[j] > array[j + 1]:  # if next element bigger than current element
                array[j], array[j + 1] = array[j + 1], array[j]  # swap elements
                isSorted = False  # changing flag
        if isSorted:  # if no changes during current iteration - end sort
            break
    return counter


def insertion_sort(array):
    counter = 0  # count of comparisons
    for i in range(1, len(array)):  # iterating every element except the first
        key = array[i]  # element to sort
        j = i - 1
        while j >= 0 and key < array[j]:  # if previous element is bigger than key element
            array[j], array[j + 1] = array[j + 1], array[j]  # swap elements
            counter += 1
            j -= 1
        counter += 1  # counting the last, unsuccessful comparison
    return counter


if __name__ == "__main__":
    sizes = [10, 100, 1000]
    types = ["random", "best", "worst"]
    data_plot = {'random': {'bubble': {}, 'insertion': {}, 'bubble_impr': {}},
                 'best': {'bubble': {}, 'insertion': {}, 'bubble_impr': {}},
                 'worst': {'bubble': {}, 'insertion': {}, 'bubble_impr': {}}}
    for n in sizes:
        print("\nDATA SIZE:", n)
        for gen_type in types:
            print("\n\nDATA TYPE: ", gen_type)
            source = generate_data(n, gen_type)

            data_bubble = np.copy(source)
            bubble_op_count = bubble_sort(data_bubble)
            print("\tBubble sort operation count:", int(bubble_op_count))
            data_plot[gen_type]['bubble'][n] = bubble_op_count

            data_bubble_impr = np.copy(source)
            bubble_impr_op_count = bubble_impr_sort(data_bubble_impr)
            print("\tImproved bubble sort operation count:", int(bubble_impr_op_count))
            data_plot[gen_type]['bubble_impr'][n] = bubble_impr_op_count

            data_insertion = np.copy(source)
            insertion_op_count = insertion_sort(data_insertion)
            print("\tInsertion sort operation count:", int(insertion_op_count))
            data_plot[gen_type]['insertion'][n] = insertion_op_count

    plot_data(data_plot, logarithmic=True, oneplot=False)


