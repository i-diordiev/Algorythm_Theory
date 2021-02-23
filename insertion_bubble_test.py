import random
import numpy as np
from create_plot import plot_data


def generate_data(n, gen_type="random"):
    if gen_type == "best":
        a = [i+1 for i in range(n)]
    elif gen_type == "worst":
        a = [i+1 for i in reversed(range(n))]
    else:
        a = [i+1 for i in range(n)]
        random.shuffle(a)
    return a


def bubble_sort(array):
    op_count = 0
    for i in array:
        for j in range(len(array) - 1):
            op_count += 1
            if array[j] % 2:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    even_number = 0
    for num in array:
        if num % 2:
            even_number += 1

    for i in range(len(array) - even_number):
        for j in range(len(array) - even_number - 1):
            op_count += 1
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    for i in range(even_number - 1, len(array)):
        for j in range(even_number - 1, len(array) - 1):
            op_count += 1
            if array[j] < array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return op_count


def bubble_impr_sort(array):
    op_count = 0
    for i in array:
        isSorted = True
        for j in range(len(array) - 1):
            op_count += 1
            if array[j] % 2:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                isSorted = False
        if isSorted:
            break

    even_number = 0
    for num in array:
        if num % 2:
            even_number += 1

    for i in range(len(array) - even_number):
        isSorted = True
        for j in range(len(array) - even_number - 1):
            op_count += 1
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                isSorted = False
        if isSorted:
            break

    for i in range(even_number - 1, len(array)):
        isSorted = True
        for j in range(even_number - 1, len(array) - 1):
            op_count += 1
            if array[j] < array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                isSorted = False
        if isSorted:
            break
    return op_count


def insertion_sort(array):
    op_count = 0
    for i in range(1, len(array)):
        j = i - 1
        while j >= 0 and array[i] < array[j]:
            op_count += 1
            temp = array[j]
            array[j] = array[j - 1]
            array[j - 1] = temp
            j -= 1
    return op_count


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
plot_data(data_plot, logarithmic=True, oneplot=True)

