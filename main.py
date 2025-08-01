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
    
def who_goes_first():
    """Randomly choose which player goes first."""
    if random.randint(0, 1) == 0:
        return 'computer'
    else: 
        return 'player'

def makeMove(board, letter, move):
  board[move] = letter

def get_computer_move(board, computer_letter):
    """Given a boar and computer's letter, determine where to move
    and return that move."""
    if computer_letter == 'X':
        player_letter == 'O':
    else: 
        return None

    """Here is the algorithm for our Tic-Tac-Toe AI:"""
    """First, check if we can win in next move."""
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, computer_letter, i):
            if is_winner (board_copy, computer_letter):
                return i

    """Check if player could win on next move and block them"""
    for i in range (1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, computer_letter, i)
            if is_winner(board_copy, player_letter)
                return i

    """Try to take one of the corners, if they are free"""
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move
    """Try to take center, if it is free"""
    if is_space_free(board, i):
        return False
    return True

print('Welcome to Tic-Tac-Toe!')