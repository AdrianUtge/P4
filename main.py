turn = 4
""" col = [[0 for x in range(7)] for y in range(6)]
 """
col = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 1],
       [1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

row = [[0 for i in range(6)] for j in range(7)]
play = (3, 4)


def modifyRow(play, row):
    newplay = (play[1], play[0])
    row[newplay[0]][newplay[1]] = 1


modifyRow(play, row)

if turn > 3:
    for i in row:
        RowTotal = sum(i)
        if RowTotal > 4:
            print("You win!")
            break
    for j in col:
        ColTotal = sum(j)
        if ColTotal > 4:
            print("You win!")
            break
        sum(j)


def CheckDiag(col):
    print("Checking Diagonal", col)
    for j in range(6):
        if (col[1][j] == 1 and col[0][j + 1] == 1):
            print("Diagonal Detected")
        if (col[0][j] == 1 and col[1][j + 1] == 1):
            print("Diagonal Detected")
    print("Diagonal Check Complete")


CheckDiag(col[2:4])