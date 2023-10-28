"""
I approached the project using 4 functions:
- display_board: to display the board
- check_victory: checks for victory of the user
- enter_move: forces the user to enter a valid input and returns it
- play: initialize the game and defines all the game logic
"""

def display_board(board):
    """Displays Tic-Tac-Toe board"""
    print(board[0][0],'|',board[0][1],'|',board[0][2])
    print('--*---*--')
    print(board[1][0],'|',board[1][1],'|',board[1][2])
    print('--*---*--')
    print(board[2][0],'|',board[2][1],'|',board[2][2])

def check_victory(board, sign):
    """Returns True if winning condition is met, else False"""
    # Check rows
    for row in board:
        if all(cell == sign for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False

def enter_move(free_fields):
    """Returns user valid input"""
    field = int(input('Enter position: '))
    while field not in free_fields:
        print('Not a valid position')
        field = int(input('Enter position: '))
    return field

def play():
    """Defines all the game logic, and initialize the game"""
    board = [[" " for _ in range(3)] for _ in range(3)]
    user_move = {i: (i // 3, i % 3) for i in range(10)}
    free_fields = {*range(9)}
    display_board(board)
    while free_fields:
        print('Turn user 1')
        user1_input = enter_move(free_fields)
        x, y = user_move[user1_input]
        free_fields.remove(user1_input)
        board[x][y] = 'X'
        display_board(board)
        if check_victory(board, 'X'):
            print("The winner is player 1")
            return
        if not free_fields:
            print("Tie")
            return
        print('Turn user 2')
        user2_input = enter_move(free_fields)
        x, y = user_move[user2_input]
        free_fields.remove(user2_input)
        board[x][y] = 'O'
        display_board(board)
        if check_victory(board, 'O'):
            print("The winner is player 2")
            return
    print("Tie")
    return

play()
