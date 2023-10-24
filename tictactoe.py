# STUDENT NAME: POORVI MADNANI
# STUDENT NUMBER: 251178757
# COURSE NAME: COMPSCI 2120A
# DATE: 23-10-2022
# INSTRUCTOR NAME: CARO STRICKLAND
# DESCRIPTION OF CODE: THIS CODE IS A TIC TAC TOE GAME
# WHERE TWO PLAYERS CAN PLAY AGAINST EACH OTHER, AND THE FIRST PLAYER TO GET THREE IN A ROW WINS THE GAME.
# IF NO PLAYER GETS THREE IN A ROW, THE GAME IS A TIE. THIS CODE USES A 2D LIST TO STORE THE BOARD AND
# USES A FUNCTION TO CHECK IF THERE IS A WINNER OR NOT.
# THE CODE ALSO USES A WHILE LOOP TO KEEP THE GAME GOING UNTIL THERE IS A WINNER OR A TIE.
# ONCE THE GAME IS OVER, THE CODE PRINTS THE WINNER OR TIE.

board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

# THIS PART OF THE CODE PRINTS THE BOARD
def print_board():
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, "|", end=" ")
        print()

# THIS PART OF THE CODE CHECKS IF THERE IS A WINNER OR NOT
def check_for_win():
    for row in board:
        if row.count('X') == 3:
            return 'X'
        elif row.count('O') == 3:
            return 'O'
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] == 'X':
            return 'X'
        elif board[0][column] == board[1][column] == board[2][column] == 'O':
            return 'O'
    if board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'X':
        return 'X'
    elif board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'O':
        return 'O'

    # THIS PART OF THE CODE CHECKS IF THE GAME IS A TIE
    if all(cell != '_' for row in board for cell in row):
        return 'T'

    return '_'

# THIS PART OF THE CODE TAKES USER INPUT FOR THE NAMES OF THE PLAYERS
player_one_name = input('Please enter the name of Player One: ')
player_two_name = input('Please enter the name of Player Two: ')

# THIS PART OF THE CODE KEEPS TRACK OF THE CURRENT PLAYER
current_player_key = 'X'

# THIS PART OF THE CODE KEEPS THE GAME GOING UNTIL THERE IS A WINNER OR A TIE
while True:
    print_board()

    if current_player_key == 'X':
        print(f"{player_one_name} ({current_player_key}), it is your turn!")
    else:
        print(f"{player_two_name} ({current_player_key}), it is your turn!")

    # THIS PART OF THE CODE TAKES USER INPUT FOR THE ROW AND COLUMN
    turn_complete = False
    while not turn_complete:
        try:
            row = int(input('Row (1-3): '))
            column = int(input('Column (1-3): '))
        except ValueError:
            print('Invalid input. Please enter a valid number.')
            continue

        # THIS PART OF THE CODE CHECKS IF THE USER INPUT IS VALID OR NOT
        if 1 <= row <= 3 and 1 <= column <= 3:
            if board[row - 1][column - 1] == '_':
                board[row - 1][column - 1] = current_player_key
                turn_complete = True
            else:
                print('That cell is already taken, please try again!')
        else:
            print('Invalid entry, please try again!')

    # THIS PART OF THE CODE CHECKS IF THERE IS A WINNER OR NOT
    result = check_for_win()
    if result != '_':
        print_board()
        if result == 'T':
            print('Tie game!')
        else:
            print(f"{player_one_name} is the winner!" if result == 'X' else f"{player_two_name} is the winner!")
        break

    current_player_key = 'X' if current_player_key == 'O' else 'O'
