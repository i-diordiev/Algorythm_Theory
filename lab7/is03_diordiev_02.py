from chained_hash_division import *  # importing hash tables
from chained_hash_multiplication import *
from open_address_hash_linear import *
from open_address_hash_quad import *
from open_address_hash_double import *

if __name__ == "__main__":
    table_types = {
        1: ChainedHashDivision,
        2: ChainedHashMultiplication,
        3: OpenAddressHashLinear,
        4: OpenAddressHashQuad,
        5: OpenAddressHashDouble
        }

    file_name = input("Type file name: ")  # reading data from file
    with open("input_10.txt", "r") as file:
        source = file.readlines()

    n, m = source[0].strip().split()
    n, m = int(n), int(m)

    elementArray = []  # writing elements to arrays
    sumArray = []
    for i in range(1, len(source)):
        element = int(source[i].strip())
        if i > n:
            sumArray.append(element)
        else:
            elementArray.append(element)

    print("Choose type of hash-table:\n"  # choosing type of table
          "1. Chained hash table with division hash function\n"
          "2. Chained hash table with multiplication hash function\n"
          "3. Open address hash table with linear hashing\n"
          "4. Open address hash table with quadratic hashing\n"
          "5. Open address hash table with double hashing")
    option = int(input())

    Table = table_types[option](n)  # creating hash table and filling it
    for el in elementArray:
        Table.Insert(el)

    with open("is03_diordiev_02_output.txt", "w") as file:
        file.write(str(Table.collision_counter) + "\n")  # writing number of collisions
        for summa in sumArray:  # searching for elements to get sum
            elementFound = False
            for element in elementArray:
                response = Table.Search(summa - element)
                if response is not None:
                    elementFound = True
                    file.write(str(element) + " " + str(summa - element) + "\n")
                    break
            if not elementFound:
                file.write("0 0\n")
