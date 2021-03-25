def get_source_from_file(source_name):  # чтение и анализ исходного файла
    source_name = source_name + ".txt"
    with open(source_name, "r") as file:
        source = file.readlines()
    users, films = source[0].split()  # количество пользователей и фильмов
    users = int(users)
    films = int(films)
    matrix = [[j for j in range(films)] for i in range(users)]
    for i in range(1, len(source)):  #
       arr = source[i].split()
       for j in range(1, len(arr)):
            matrix[i - 1][j - 1] = int(arr[j])
    return users, films, matrix


def convert_array(array, key):  # трансформация массива для поиска количества инверсий
    result = [0 for i in range(len(array))]
    i = 0
    for index in key:  #
        result[index - 1] = array[i]
        i += 1
    return result


def merge_and_count_split_inv(left, right):
    array = []  # результирующий массив
    i = 0  # индекс левой части
    j = 0  # индекс правой части
    cnt = 0  # счетчик инверсий
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # если левый елемент меньше правого, добавляю его
            array.append(left[i])
            i += 1
        else:   # иначе добавляю правый элемент и увеличиваю счетчик инверсий
            array.append(right[j])
            j += 1
            cnt += len(left) - i
    array += right[j:]  # дополняю получившийся массив остальными значениями из правой и левой части
    array += left[i:]
    return array, cnt


def sort_and_count_inv(array):
    n = len(array)  # длина массива
    k = n // 2  # разделитель массива
    if n == 1:
        return array, 0
    else:
        left, x = sort_and_count_inv(array[:k])  # разделяю массив
        right, y = sort_and_count_inv(array[k:])
        array, z = merge_and_count_split_inv(left, right)
        return array, x+y+z


def save_result_to_file(file_name, results, s_user):  # записываю результат в файл
    file_name = file_name + ".txt"
    with open(file_name, "w") as file:
        file.write(str(s_user) + "\n")
        for i in range(len(results)):
            if results[i][0] != s_user:
                file.write(str(results[i][0]) + " " + str(results[i][1]) + "\n")
        file.write(str(s_user) + "\n")


name = input("Type name of input file WITHOUT \".txt\": ")
usr, film, matrix = get_source_from_file(name)  # читаю исходный файл, записываю количество пользователей, фильмов и матрицу предпочтений
result_matrix = [[i + 1, 0] for i in range(usr)]

start_user = int(input("Type number of start user: "))  # ввожу номер пользователя, с которым буду сравнивать
key_array = matrix[start_user - 1]

for i in range(usr):  # заполняю матрицу результатов, где 1 елемент - номер пользователя, 2 елемент - кол-во инверсий
    if i != start_user - 1:
        not_sorted_array = convert_array(matrix[i], key_array)
        sorted_array, counter = sort_and_count_inv(not_sorted_array)
        result_matrix[i][1] = counter

for i in range(len(result_matrix)):  # сортирую матрицу результатов по возрастанию 2 елемента
    for j in range(len(result_matrix) - 1):
        if result_matrix[j][1] > result_matrix[j + 1][1]:
            temp = result_matrix[j]
            result_matrix[j] = result_matrix[j + 1]
            result_matrix[j+1] = temp

save_result_to_file("is03_diordiev_01_output", result_matrix, start_user)
