#Tic-Tac-Toe

import random

def draw_board(board):
    """This function prints out the board it was passed.
    'board' is a list of 10 strings representing the board
    (ignore index 0.)"""
    print(board[7] + '|'  + board [8] + '|' + board [9])
    print('-+-+-')
    print(board[4] + '|'  + board [5] + '|' + board [6])
    print('-+-+-')
    print(board[1] + '|'  + board [2] + '|' + board [3])

def input_player_letter():
    """Lets the player enter which letter they want 
    to be. Returns a list with the player's letter 
    as the first item  and the computer's letter as 
    the second."""
    letter = ''
    while not (letter == "X" or letter == "O"):
        print("Do you want to be X or O?")
        letter = input().upper()
    
    """The first element in the list is the player's 
    letter; the second is the computer's letter."""
    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]
    
print (input_player_letter())