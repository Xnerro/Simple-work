import os
from time import sleep


class matrix:
    def add(matrik1, matrik2, total=[]):
        for i in range(len(matrik1)):
            for j in range(len(matrik2)):
                total[i][j] = matrik1[i][j] + matrik2[i][j]
        return total

    def subtrac(matrik1, matrik2, total=[]):
        for i in range(len(matrik1)):
            for j in range(len(matrik2)):
                total[i][j] = matrik1[i][j] - matrik2[i][j]
        return total

    def multiply(matrik1, matrik2, total=[]):
        for i in range(len(matrik1)):
            for j in range(len(matrik1[0])):
                for k in range(len(matrik2)):
                    total[i][k] += matrik1[i][j] * matrik2[j][k]
        return total

    def determinan(board1, de1t=0):
        if len(board1) == 2 and len(board1[0]) == 2:
            det1 = (board1[0][0] * board1[1][1]) - (board1[0][1] * board1[1][0])
            return det1
        elif len(board1) == 3 and len(board1[0]) == 3:
            det1 = (
                (board1[0][0] * board1[1][1] * board1[2][2])
                + (board1[0][1] * board1[1][2] * board1[2][0])
                + (board1[0][2] * board1[1][0] * board1[2][1])
            ) - (
                (board1[2][0] * board1[1][1] * board1[0][2])
                + (board1[2][1] * board1[1][2] * board1[0][0])
                + (board1[2][2] * board1[1][0] * board1[0][1])
            )
            return det1

    def invers(adj1, board1, det1=0):
        if len(board1) == 2 and len(board1[0]) == 2:
            adj1[0][0] = board1[1][1]
            adj1[0][1] = -board1[0][1]
            adj1[1][0] = -board1[1][0]
            adj1[1][1] = board1[0][0]
            det1 = (board1[0][0] * board1[1][1]) - (board1[0][1] * board1[1][0])
            for i in range(2):
                for j in range(2):
                    board1[i][j] = (1 / det1) * adj1[i][j]
            return board1
        elif len(board1) == 3 and len(board1[0]) == 3:
            det1 = (
                (board1[0][0] * board1[1][1] * board1[2][2])
                + (board1[0][1] * board1[1][2] * board1[2][0])
                + (board1[0][2] * board1[1][0] * board1[2][1])
            ) - (
                (board1[2][0] * board1[1][1] * board1[0][2])
                + (board1[2][1] * board1[1][2] * board1[0][0])
                + (board1[2][2] * board1[1][0] * board1[0][1])
            )

            a11 = (board1[1][1] * board1[2][2]) - (board1[2][1] * board1[1][2])
            a12 = (board1[1][0] * board1[2][2]) - (board1[2][0] * board1[1][2])
            a13 = (board1[1][0] * board1[2][1]) - (board1[2][0] * board1[1][1])
            a21 = (board1[0][1] * board1[2][2]) - (board1[2][1] * board1[0][2])
            a22 = (board1[0][0] * board1[2][2]) - (board1[2][0] * board1[0][2])
            a23 = (board1[0][0] * board1[2][1]) - (board1[2][0] * board1[0][1])
            a31 = (board1[0][1] * board1[1][2]) - (board1[1][1] * board1[0][2])
            a32 = (board1[0][0] * board1[1][2]) - (board1[1][0] * board1[0][2])
            a33 = (board1[0][0] * board1[1][1]) - (board1[1][0] * board1[0][1])

            adj1[0][0] = a11
            adj1[0][1] = -a21
            adj1[0][2] = a31
            adj1[1][0] = -a12
            adj1[1][1] = a22
            adj1[1][2] = -a32
            adj1[2][0] = a13
            adj1[2][1] = -a23
            adj1[2][2] = a33

            for i in range(3):
                for j in range(3):
                    board1[i][j] = (1 / det1) * adj1[i][j]

            return board1


d = []
matrik1 = []
matrik2 = []
total = []

a = int(input("lenght kolom:"))
b = int(input("lenght baris:"))


print("=================")
for i in range(a):
    d.append(0)
for i in range(b):
    matrik1.append(list(d))
    matrik2.append(list(d))
    total.append(list(d))


"""for i in matrik1:
    print(i)"""

for i in range(len(matrik1)):
    for j in range(len(matrik1[0])):
        x = int(input(f"matrix 1 ke-[{i}][{j}] :"))
        matrik1[i][j] = x
print("=================")
print("matrix 1=")
for i in matrik1:
    print(i)

print("=================")
for j in range(len(matrik2)):
    for k in range(len(matrik2[0])):
        y = int(input(f"Data matrix 2 ke-[{j}][{k}] :"))
        matrik2[j][k] = y
print("=================")
print("matrik 2=")
for i in matrik2:
    print(i)


os.system("clear")
print("=================")
print("matrik 1=")
for i in matrik1:
    print(i)
print("=================")

print("matrik 2=")
for i in matrik2:
    print(i)
print("=================")
print("Operator")
print("=================")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Determinan")
print("5. Invers")
print("=================")
choice = int(input("Choose Operasi :"))
print("=================")

while choice != 1 or choice != 2 or choice != 3:
    if choice == 1:
        print("Add")
        for i in matrix.add(matrik1, matrik2, total):
            print(i)
        break
    elif choice == 2:
        print("Subtract")
        for i in matrix.subtrac(matrik1, matrik2, total):
            print(i)
        break
    elif choice == 3:
        print("Multioply")
        for i in matrix.multiply(matrik1, matrik2, total):
            print(i)
        break
    elif choice == 4:
        print("Determinan matrix 1=")
        for i in matrix.determinan(matrik1):
            print(i)
        print("\nDeterminan matrix 2=")
        for i in matrix.determinan(matrik2):
            print(i)
        break
    elif choice == 5:
        print("Invers matrix 1=")
        for i in matrix.invers(total, matrik1):
            print(i)
        print("\nInvers matrix 2=")
        for i in matrix.invers(total, matrik2):
            print(i)
        break
    else:
        print("Operation Not Available")
        sleep(1)
        os.system("clear")
        print("=================")
        print("Operator")
        print("=================")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Determinan")
        print("5. Invers")
        print("=================")
        choice = int(input("choose Operasi :"))
        print("=================")
        pass
