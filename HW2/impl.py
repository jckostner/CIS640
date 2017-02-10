def tic_tac_toe_check(board):
    if type(board) == list:
        for item in board:
            if type(item) != str:
                raise TypeError('List does not contain all strings')
    else:
        raise TypeError('Method not passed a valid list')

    empty = 0
    if len(board) != 9:
        raise ValueError('List is not correct size')
    else:
        for item in board:
            if not (item == "x" or item == "o" or item == ""):
                print(item)
                raise ValueError('Board contains invalid characters')
            elif item == "":
                empty + 1;
    if empty == 9:
        return None


    boardArray = []
    for index in range(3):
        i = index * 3
        boardArray.append([board[i], board[i + 1], board[i + 2]])

    wins = 0
    symbol = ""
    for num in range(3):
        if boardArray[num][0] == boardArray[num][1] == boardArray[num][2] != "":
            wins += 1
            symbol = boardArray[num][0]
        elif boardArray[0][num] == boardArray[1][num] == boardArray[2][num] != "":
            wins += 1
            symbol = boardArray[0][num]
    if boardArray[0][0] == boardArray[1][1] == boardArray[2][2] != "":
        wins += 1
        symbol = boardArray[1][1]
    elif boardArray[2][0] == boardArray[1][1] == boardArray[0][2] != "":
        wins += 1
        symbol = boardArray[1][1]

    if wins == 1:
        return symbol
    elif wins == 0:
        return None
    else:
        raise ValueError('Board has multiple winners')
    return


