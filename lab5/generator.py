import random

with open("input_sample.txt", "w") as file:
    grade = int(input("Type number of digits in every number: "))
    array = [random.randint(10 ** (grade - 1), 10 ** grade) for i in range(10)]
    file.write(str(grade) + "\n")
    for el in array:
        file.write(str(el) + "\n")
