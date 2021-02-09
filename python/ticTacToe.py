#!/usr/bin/env python
from random import randint

def connected(letter,board):
    for i in range(3):
        #horizontal  
        if ( board[i][0] == letter )  and ( board[i][1] == letter ) and ( board[i][2] == letter ):
            return True
        #vertical
        elif ( board[0][i] == letter ) and ( board[1][i] == letter ) and ( board[2][i] == letter ):
            return True

    # bottom left corner to up right corner
    if ( board[2][0] == letter ) and ( board[1][1] == letter ) and ( board[0][2] == letter ):
        return True

    #top left corner to down right corner
    elif ( board[0][0] == letter ) and ( board[1][1] == letter ) and ( board[2][2] == letter ):
        return True

def showBoard(board):
    print("\n"," "," -"*9)
    for i in range(3):
        print(chr(99-i), " | ", board[i][0], " | ", board[i][1], " | ", board[i][2], " | ")
        print("  "," -"*9)
    print(" "*5, "1", " "*3, "2", " "*3, "3","\n")

def twoPlayers(board):
    moves = 0
    while moves < 9:
        showBoard(board)
        if moves % 2 == 0:
            player1 = input("Player 1's turn \n> ")
            if player1 == "q" or player1 == "quit":
                print("good bye (: ")
                break
            column = player1[0].lower()
            row = int(player1[1])
            case = board[-(ord(column)-95-1)][row-1] 
            if case!=' ':
                print("please play in an empty square.")
                moves-=1
            else:
                board[-(ord(column)-96)][row-1] = "x"
    
        else:
            player2 = input("Player 2's turn \n> ")
            if player2 == "q" or player2 == "quit":
                print("good bye (:")
                break
            column = player2[0].lower()
            row = int(player2[1])
            case = board[-(ord(column)-95-1)][row-1]
            if case!= ' ':
                print("please play in an empty square.")
                moves-=1
            else:
                board[-(ord(column)-96)][row-1] = "o"

        #verifying if anyone won
        if connected("x",board):
            showBoard(board)
            print("Player 1 won")
            break 
        elif connected("o", board):
            showBoard(board)
            print("Player 2 won")
            break
        moves += 1

# fake IA, just ranodm moves 
def singlePlayer(board):
    moves = 0
    while moves < 5:
        showBoard(board)
        #player turn 
        player1 = input("Player 1's turn \n> ")
        if player1 == "q" or player1 == "quit":
            print("good bye (: ")
            break
        column = player1[0].lower()
        row = int(player1[1])
        case = board[-(ord(column)-95-1)][row-1] 
        if case!=' ':
            print("please play in an empty square.")
            moves-=1
            continue
        else:
            board[-(ord(column)-96)][row-1] = "x"

        if connected("x",board):
            showBoard(board)
            print("You won ;)")
            break 

        #random oppenent moves
        x,y = randint(0,2), randint(0,2)
        while board[x][y] in ("o", "x"):
            x,y = randint(0,2), randint(0,2)
        board[x][y] = "o"

        if connected("o",board):
            showBoard(board)
            print("The fake IA won :(")
            break 

        moves +=1 

def main():
    board = [[" "," "," "],
            [" "," "," "],
            [" "," "," "]]
    
    print("\nWelcome to another random tic tac toe. \nPlease use the following syntax to play \"LetterNumber\", example: b2\nEnjoy! (:")
    
    mode = input("What mode do you want to play? Single (s) or two players? (t) : ")
    while mode != "s" and mode != "t":
        mode = input("What mode do you want to play? Single (s) or two players? (t) : ")
        if mode != 's' and mode != 't':
            print('please insert either "s" or "t"')
    if mode == "s":
        singlePlayer(board)
    else:
        twoPlayers(board)
    
main()
    
    


