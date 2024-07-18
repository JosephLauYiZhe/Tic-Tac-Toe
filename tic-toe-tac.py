import random


def choose_first():
    player=random.randint(0,1)
    if player==0:
        return('player 1')
    else:
        return('player 2')

def space_check(board, position):
    return board[position] == " "

def full_board_check(board):
    for i in range(0,len(board)):
        if board[i]==' ':
            return False
    return True
        
    
def win_check(board, mark):
    
    pos = [str(i) for i,x in enumerate(board) if x==mark]
    win_conditions = ['123','456','789','147','258','369','357','159']
    
    s1 = set(pos)

    for win_con in win_conditions: 
        s2 = set(win_con)
        
        if s2.issubset(s1):
            return True
        
    return False


def place_marker(board, marker, position):
    board[position] = marker
    
def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    

def player_input():
    input_range = ['X', 'O']
    marker1 = ''
    
    while marker1 not in input_range:
        marker1 = input('Player 1, please choose your marker( X, O ): ')
        if marker1 not in input_range:
            print('Sorry, this marker is unavailable. \n')
    
    if marker1 ==  'X':
        marker2 = 'O'
    else:
        marker2 = 'X'
    
    return (marker1, marker2)

def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position
    
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

def end_game(board, player1_marker, player2_marker):
    #check if game ends
    n = 'no'
    if win_check(board, player1_marker):
        print('Player 1 wins!')
        n = 'yes'
    elif win_check(board,player2_marker):
        print('Player 2 wins!')
        n = 'yes'
    elif full_board_check(board):
        print('No one wins in this round!')
        n = 'yes'
    return n
    
# Main program
print('Welcome to Tic Tac Toe!')

while True:
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    first = choose_first()
    print(f'{first} goes first! ')
    print('------------------------------------------------\n')
    
    if first == 'player 1':
        #player 1 turn
        print('Player 1 turn:')
        place_marker(board, player1_marker, player_choice(board))
        display_board(board)
        print('\n')

    while not full_board_check(board):
            
        #player 2 turn
        print('Player 2 turn:')
        place_marker(board, player2_marker, player_choice(board))
        display_board(board)
        print('\n')
        
        if (end_game(board, player1_marker, player2_marker) == 'yes'):
            break
        
        #player 1 turn
        print('Player 1 turn:')
        place_marker(board, player1_marker, player_choice(board))
        display_board(board)
        print('\n')
        
        if (end_game(board, player1_marker, player2_marker) == 'yes'):
            break
            
            
    if not replay():
        break
