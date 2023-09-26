# TICTACTOE
# -Print a board


# Default board
board = {'topL': " ", 'topM': " ", 'topR': " ",
         'midL': " ", 'midM': " ", 'midR': " ",
         'botL': " ", 'botM': " ", 'botR': " ",}

# Printboard function
def printBoard(board):
    row = []
    column = []
    for k, v in board.items():
        row.append("|" + v + "|")

    r = []
    for i in range(len(row)):
        r.append(row[i])

        if(len(r) == 3):
            column.append(r)
            r = []

    for c in range(len(column)):
        print_board = ""
        for cc in range(len(column[c])):
            print_board += column[c][cc]

        print(print_board)
    

move = 'X'

for i in range(9):
    printBoard(board)
    print('Enter your move: ')
    turn = input()

    board[turn] = move

    if move == 'X':
        move = "O"
    elif move =='O':
        move = "X"
    if(board["topL"] == 'X' and board['topM'] == 'X' and board['topR'] == 'X'):
        print('You win')
        printBoard(board)
        break
