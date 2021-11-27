#!/usr/bin/env python3

turn = 4
Counter1 = 0
col = [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 1, 1],
       [1, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
col2 = [[1, 2, 3, 4, 5, 6, 7], [11, 12, 13, 14, 15, 16, 17],
        [21, 22, 23, 24, 25, 26, 27], [31, 32, 33, 34, 35, 36, 37],
        [41, 42, 43, 44, 45, 46, 47], [51, 52, 53, 54, 55, 56, 57]]
play = (3, 4)


def FourinRow(arr):
    b = 0
    for i in range(len(arr)):
        print(b)
        if arr[i] == 0:
            b = 0
        else:
            b += arr[i]
            if b == 4:
                print("Four in a row")


''' 
def modifyRow(play, row):
    newplay = (play[1], play[0])
    row[newplay[0]][newplay[1]] = 1
 '''


def CheckDiag(col):
    print("Checking Diagonal", "\n", col)
    for j in range(6):
        if (col[1][j] == 1 and col[0][j + 1] == 1):
            print("Diagonal Detected")
        if (col[0][j] == 1 and col[1][j + 1] == 1):
            print("Diagonal Detected")
    print("Diagonal Check Complete")


def Digonal(matrix):
    a = 0
    for j in range(2):
        arr = []
        for i in range(6):
            arr.append(matrix[i][i + j])
            print(matrix[i][i + j])
            print(arr)
        print("\n")
        print(arr)
        FourinRow(arr)


Digonal(col)

zero = [1, 0, 1, 0, 1, 0, 1]
four = [0, 0, 0, 1, 1, 1, 1]
