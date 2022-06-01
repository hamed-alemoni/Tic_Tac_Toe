import random

def main():

    board = [' ' for x in range(10)]

    finish = False

    print('Welcome to tic tac to game :))')
    print_board(board)

    while not is_board_full(board):
        # if computer wasn't won, player should make a move
        if not is_winner(board, 'O'):
            player_move(board)
            print_board(board)
        else:
            print('Sorry computer won this time!!')
            finish = True
            break
        
        # if player wasn't won, computer should make a move
        if not is_winner(board, 'X'):
            move = computer_move(board)
            # board is full
            if move == 0:
                print('Tie game!!')
                break
            else:
                insert(board,move,'O')
                print(f'Computer placed an O in position {move} : ')
                print_board(board)
        else:
            print('Congratulation you won :))')
            finish = True
            break

    # if board is full and the game is not finished
    if is_board_full(board) and not finish:
        print('Tie game!!')

# check the board is full or not
def is_board_full(board):
    return ' ' not in board

# check the letter is winner or not
def is_winner(board, letter):
            # check rows (line 1 to 3) check column (lines 4 to 6) check diagonal (lines 7 and 8)
    return (board[1] == letter and board[2] == letter and board[3] == letter) or \
           (board[4] == letter and board[5] == letter and board[6] == letter) or \
           (board[7] == letter and board[8] == letter and board[9] == letter) or \
           (board[1] == letter and board[4] == letter and board[7] == letter) or \
           (board[2] == letter and board[5] == letter and board[8] == letter) or \
           (board[3] == letter and board[6] == letter and board[9] == letter) or \
           (board[1] == letter and board[5] == letter and board[9] == letter) or \
           (board[3] == letter and board[5] == letter and board[7] == letter)

def print_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def computer_move(board):
    move = 0
    # find index of empty space
    possible_moves = [index for index, letter in enumerate(board) if letter == ' ' and index != 0]

    move = win_or_blocked_player(possible_moves, board)

    if move != 0:
        return move

    # find center if it's exist
    move = find_specific_empty_space(possible_moves, [5])

    if move != 0:
        return move

    # find open corners
    move = find_specific_empty_space(possible_moves, [1, 3, 7, 9])
    
    if move != 0:
        return move
    

    # find open open edge
    move = find_specific_empty_space(possible_moves, [2, 4, 8, 6])
    
    
    return move


def find_specific_empty_space(possible_moves, specific_domain):
    open_space = []
    move = 0

    for i in possible_moves:
        if i in specific_domain:
            open_space.append(i)
    
    if len(open_space) > 0:
        move = select_random_move(open_space)
    
    return move

def select_random_move(a_list):
    move = random.choice(a_list)
    return move


def win_or_blocked_player(possible_moves, board):
    # if player has chance to win computer blocked him/her and if computer has chance to win use it
    for letter in ['O' , 'X']:
        for i in possible_moves:
            copy_board = board[:]
            insert(copy_board,i,letter)
            if is_winner(copy_board,letter):
                return i
    return 0

def player_move(board):
    run = True
    while run:
        move = input('Please determine the position of your X (1-9) : ')
        
        try:
            move = int(move)

            if 0 < move < 10:
                if is_space_free(board,move):
                    insert(board, move, 'X')
                    run = False
                else:
                    print('Sorry this position is already full!!')
            else:
                print(f'Please select the position from 1 to 9 not {move} !!')

        except:
            print('Please enter number!!')

# check the board with given index is free or not
def is_space_free(board, index):
    return board[index] == ' '

# insert given letter in given position
def insert(board, index, letter):
    board[index] = letter



if __name__ == '__main__':
    main()