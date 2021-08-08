#!/usr/bin/env python
# coding: utf-8

#author: mohammad ghavi

'''
7|8|9
-----
4|5|6
----- 
1|2|3
'''

# Import the modules
from IPython.display import clear_output
from random import choice
from time import sleep


def display_board(board: list)->str:
    '''
    display the boardgame according the below map:
    
                        7|8|9
                        -----
                        4|5|6
                        ----- 
                        1|2|3
    '''
    clear_output()
    reshape = [[i for i in board[j:j+3]] for j in range(1, 10, 3)][::-1]
    
    for i, data in enumerate(reshape):
        print(' | '.join(data))
        if i != len(reshape)-1:
            print('------------')
        


def player_input()->tuple:
    '''
    select the shape of list for each player 
        
    return: 
        a tuple which the first element display the shape of player one piece 
        and the second element display the shape of the player two piece
        player 2 is computer.
    '''
    
    while True:   
        piece1 = input('player1 choose X or o: ')
        if piece1 in ['X', 'o']:
            break
        print('Dear player, just small "o" or capital "X", try again:')  
        
    piece2 = 'X' if piece1 != 'X' else 'o'
    return (piece1, piece2)




def place_marker(board: list, marker: str,position: int)->None:
    '''
    put down the marker on the position in the board.
    '''
    board[position] = marker
    




def win_check(board: list, marker: str)->bool:
    '''
    Check the victor
    '''
    for i in [[i for i in board[j:j+3]] for j in range(1, 10, 3)]:
        if all(v==marker for v in i):
            return True
    
    for i in [[i for i in board[j+1:j+8:3]] for j in range(0, 3)]:
        if all(v==marker for v in i):
            return True
        
    for i in [[board[i] for i in [7, 5, 3]], [board[i] for i in [9, 5, 1]]] :
        if all(v==marker for v in i):
            return True
    return False





def choose_first()->str:
    '''
    Choose a random player between pleyer1 and player2.
    '''
    return choice(['player1', 'player2(computer)'])
    





def space_check(board: list,position: list)->bool:
    '''
    check being empty blocks.
    '''
    if board[position] != ' ': 
        return False
    return True   




def full_board_check(board: list)->bool:
    '''
    check board black, if all black filled, the function will return "True", otherwise "False".
    '''
    if board.count(' ') == 0:
        return True
    else:
        return False
    



def player_choice(board: list)->int:
    '''
    check going authority 
    '''
    
    while True:
        position = input('choose a position (1-9): ')
         
        if position.isdecimal() :
            if 0<int(position)<10:
                if space_check(board, int(position)) :
                    break
    return int(position)
            

def computer(board)->int:
    empty = [i for i in range(len(board)) if board[i]==' ']
    sleep(1.5)
    return choice(empty)


def replay()->bool:
    while True:
        repeat = input('playe again? Enter yes or no:')
        if repeat == 'yes': 
            return True
        elif repeat == 'no':
            return False
        else:
            print("What?!, be sure, you enter exactly \"yes\" or \"no\" not something else.")
            print("Please try again.") 



print('welcome to tic tac toe')

while True:
    board = ['s'] + [' ']*9
    start_with = choose_first()
    turn = start_with
    print(f"start wirh {start_with}")
    markers = player_input()
    while True: 
        marker = markers[0] if turn=='player1' else markers[1]
        if turn == 'player1':
            position = player_choice(board)
        else:
            position = computer(board)
        place_marker(board, marker, position)

        display_board(board)
        if win_check(board, marker):
            print(f'\n{turn} has won!')
            break
        elif full_board_check(board):
            print("\nDraw the game")
            break

        else:
            turn = 'player2(computer)' if turn=='player1' else 'player1'
            marker = 'o' if marker=='X' else 'X'
            print(f"\nnobat {turn}, {marker}")
    
    if not replay():
        break




