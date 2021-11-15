turn = 4
col = [[0 for x in range(7)] for y in range(6)]
row = [[0 for i in range(6)] for j in range(7)]

play = (3, 4)


def modifyRow(play, row):
    newplay = (play[1], play[0])
    row[newplay[0]][newplay[1]] = 1
    print(row)


modifyRow(play, row)
col[play[0]][play[1]] = 1

print(col[play[0]][play[1]])
print(col)

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