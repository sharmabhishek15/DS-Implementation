def solve(lst, row, rookcol, count):
    print(row, rookcol, count)
    for i in range(0, rookcol):
        if lst[row][i] == "P":
            count += 1
            break
        if lst[row][i] == "B":
            break

    for i in range(rookcol + 1, 8):
        if lst[row][i] == "P":
            count += 1
            break
        if lst[row][i] == "B":
            break

    for i in range(0, rookcol):
        if lst[i][rookcol] == "P":
            count += 1
            break
        if lst[i][rookcol] == "B":
            break

    for i in range(rookcol + 1, 8):
        if lst[i][rookcol] == "P":
            count += 1
            break
        if lst[i][rookcol] == "B":
            break
    return count


def captureThePawns(board):
    # Write your code here.
    count = 0
    for listIndex in board:
        # print(listIndex)
        rIndex = board.index(listIndex)
        if 'R' in listIndex:
            cIndex = listIndex.index('R')
            count =  solve(board, rIndex, cIndex, count)
            break

    return count
# board = [
#             ['*','*','*','*','*','*','*','*'],
#             ['*','*','*','*','*','*','*','*'],
#             ['*','*','*','R','*','*','*','P'],
#             ['*','*','*','*','*','*','*','*'],
#             ['*','*','*','P','*','*','*','*'],
#             ['*','*','*','*','*','*','*','*'],
#             ['*','*','*','P','*','*','*','*'],
#             ['*','*','*','*','*','*','*','*']
#          ]

board = [
            ['B','*','*','*','*','P','*','R'],
            ['*','*','*','*','*','*','*','*'],
            ['P','*','*','*','*','*','*','*'],
            ['*','*','*','*','*','P','*','*'],
            ['*','*','*','*','*','*','*','*'],
            ['*','*','*','*','*','*','*','*'],
            ['*','*','B','P','*','*','*','*'],
            ['*','*','P','*','B','*','*','*']
         ]

#B****P*R ******** P******* *****P** ******** ******** **BP**** **P*B***
print(captureThePawns(board))