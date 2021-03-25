u_r1 = [8.9, 10.3, 12.1, 14.6, 15.6, 15.4, 13.4, 11.2, 9.2]
u_r2 = [10.2, 12.8, 17.2, 25.6, 33.5, 26.6, 18.2, 13.2, 9.8]
u_r3 = [10.3, 13, 18.7, 30, 46.9, 33.7, 21, 15.6, 11.4]

print("\n\nFOR R1:")
for el in u_r1:
    print(el/5)

print("\n\nFOR R2:")
for el in u_r2:
    print(el/5)

print("\n\nFOR R3:")
for el in u_r3:
    print(el/5)


name = input("Enter your file: ") # - rjvvtyn
file = open(name,'r')
matrix = [list(map(int, row.split())) for row in file.readlines()]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()
x = 6
file.close()
handle = open("is03_konyushenko_08_output.txt","w")
handle.write(str(x)+'\n')
for i in range(1,len(matrix)):
    counter=0
    for el_6 in range(1,len(matrix[i])-1):
        for j in range(1,len(matrix[i])-1):
            if(matrix[6][el_6]<matrix[i][j]):
                counter+=1
    handle.write(str(i)+' '+str(counter) + '\n')

handle = open("is03_konyushenko_08_output.txt","r")
data = handle.read()
print("is03_konyushenko_08_output.txt:")
print(data)
handle.close()