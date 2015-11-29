the_board = {'top-L': 'X', 'top-M': 'X', 'top-R': 'X',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}



def print_board(board):
    print(board['top-L'] + '|'+ board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|'+ board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|'+ board['low-M'] + '|' + board['low-R'])

turn = 'X'

for i in range(9):
    print_board(the_board)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    the_board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    if (the_board['top-L'] + the_board['top-M'] + the_board['top-R']) or (the_board['mid-L'] + the_board['mid-M'] + the_board['mid-R']) or (the_board['low-L'] + the_board['low-M'] + the_board['low-R']) or (the_board['top-L'] + the_board['mid-M'] + the_board['low-R'])== 'XXX':
        print('Congratulations! Player X has won the game!')
        break
    elif 



print_board(the_board)

print(the_board['top-L'] + the_board['top-M'] + the_board['top-R'])

