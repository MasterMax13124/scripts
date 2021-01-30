#!/usr/bin/env python
def horizontalWin(board):
    for i in range(3):
        if ( board[i][0] == "x" and board[i][1] == "x" and board[i][2] == "x") or ( board[i][0] == "o" and board[i][1] == "o" and board[i][2] == "o" ):
            return True

def verticalWin(board):
    for i in range(3):
        if ( board[0][i] == "x" and board[1][i] == "x" and board[2][i] == "x") or ( board[0][i] == "o" and board[1][i] == "o" and board[2][i] == "o" ):
            return True

def diagonal(board):
    #bottom left corner to up right corner
    if ( board[2][0] == "x" and board[1][1] == "x" and board[0][2] == "x") or ( board[2][0] == "o" and board[1][1] == "o" and board[0][2] == "o" ):
        return True
    #top left corner to down right corner
    elif ( board[0][0] == "x" and board[1][1] == "x" and board[2][2] == "x") or ( board[0][0] == "o" and board[1][1] == "o" and board[2][2] == "o" ):
        return True

def connected(board):
    if horizontalWin(board) or verticalWin(board) or diagonal(board):
        return True

def showBoard(board):
    print("\n"," "," -"*9)
    for i in range(3):
        print(chr(99-i), " | ", board[i][0], " | ", board[i][1], " | ", board[i][2], " | ")
        print("  "," -"*9)
    print(" "*5, "1", " "*3, "2", " "*3, "3","\n")

print("\nWelcome to another random tic tac toe. \nPlease use the following syntax to play \"LetterNumber\", example: b2\nEnjoy! (:")

board = [[" "," "," "],
        [" "," "," "],
        [" "," "," "]]

for moves in range(9):
    showBoard(board)
    if moves % 2 == 0:
        print("Player 1's turn.")
        player1 = input("> ")
        if player1 == "quit":
            print("good bye.")
            break
        column = player1[0].lower()
        row = int(player1[1])
        case = board[-(ord(column)-96)][row-1] 
        if case!=' ':
            print("please play in an empty square.")
            moves-=1
        else:
            board[-(ord(column)-96)][row-1] = "x"
            if connected(board):
                showBoard(board)
                print("Player 1 won.")
                break

    else:
        print("Player 2's turn.")
        player2 = input("> ")
        if player2 == "quit":
            print("good bye.")
            break
        column = player2[0].lower()
        row = int(player2[1])
        case = board[-(ord(column)-96)][row-1]
        if case!= ' ':
            print("please play in an empty square.")
            moves-=1
        else:
            board[-(ord(column)-96)][row-1] = "o"
            if connected(board):
                showBoard(board)
                print("Player 2 won.")
                break
