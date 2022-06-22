import os


def game(x, y):
    if x == 1:
        board[0][0] = y

    elif x == 2:
        board[0][2] = y

    elif x == 3:
        board[0][4] = y

    elif x == 4:
        board[1][0] = y

    elif x == 5:
        board[1][2] = y

    elif x == 6:
        board[1][4] = y

    elif x == 7:
        board[2][0] = y

    elif x == 8:
        board[2][2] = y

    elif x == 9:
        board[2][4] = y

    else:
        "Tempat tidak tersedia"


def checker(board):
    if (board[0][0] == "o" and board[0][2] == "o" and board[0][4] == "o") or (
        board[0][0] == "x" and board[0][2] == "x" and board[0][4] == "x"
    ):
        return 1
    elif (board[0][0] == "o" and board[1][2] == "o" and board[2][4] == "o") or (
        board[0][0] == "x" and board[1][2] == "x" and board[2][4] == "x"
    ):
        return 1
    elif (board[1][0] == "o" and board[1][2] == "o" and board[1][4] == "o") or (
        board[1][0] == "x" and board[1][2] == "x" and board[1][4] == "x"
    ):
        return 1
    elif (board[2][0] == "o" and board[2][2] == "o" and board[2][4] == "o") or (
        board[2][0] == "x" and board[2][2] == "x" and board[2][4] == "x"
    ):
        return 1
    elif (board[2][0] == "o" and board[1][2] == "o" and board[0][4] == "o") or (
        board[2][0] == "x" and board[1][2] == "x" and board[0][4] == "x"
    ):
        return 1
    elif (board[0][0] == "o" and board[1][0] == "o" and board[2][0] == "o") or (
        board[0][0] == "x" and board[1][0] == "x" and board[2][0] == "x"
    ):
        return 1
    elif (board[0][2] == "o" and board[1][2] == "o" and board[2][2] == "o") or (
        board[0][2] == "x" and board[1][2] == "x" and board[2][2] == "x"
    ):
        return 1
    elif (board[0][4] == "o" and board[1][4] == "o" and board[2][4] == "o") or (
        board[0][4] == "x" and board[1][4] == "x" and board[2][4] == "x"
    ):
        return 1
    else:
        return 0


board = (["1", "|", "2", "|", "3"], ["4", "|", "5", "|", "6"], ["7", "|", "8", "|", "9"])
a = 0

for i in range(9):
    os.system("clear")
    print(i)
    for i in range(len(board)):
        print(board[i])
    p1 = int(input(" p1: "))
    x = "o"
    game(p1, x)
    a = checker(board)
    if a == 2:
        pass
    elif a == 0:
        os.system("clear")
        if i == 2:
            print("Game draw")
            break
        for i in range(len(board)):
            print(board[i])

        p2 = int(input(" p2: "))
        x = "x"
        game(p2, x)
        a = checker(board)
        if a == 1:
            os.system("clear")
            for i in board:
                print(i)
            print("p2 win")
            break
    elif a == 1:
        os.system("clear")
        for i in board:
            print(i)
        print("p1 win")
        break
