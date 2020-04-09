board = ["-","-","-",
         "-","-","-",
         "-","-","-"] 

#In case the game continues
game_playing = True

#We start with no winner
winner = None

#Whos turn is it 
current_player = "X"

#The playing board
def display_board():
    print(board[0] + " | " + board[1] +" | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] +" | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] +" | " + board[8] + "     7 | 8 | 9")


def GAME():

    #Display the initial board 
    display_board()

    while game_playing:

        handle_turn(current_player)

        check_if_game_over()

        change_player()

    #If the game ended
    if winner == "X" or winner == "O":
        print(winner + " is the winner!! Congrats!!")
    elif winner == None:
        print("Tie Game.")



def handle_turn(player):

    print(player + "...Is your turn.Be careful")
    position = input("Pick a position from 1 to 9: ")

    valid = False
    while not valid:
        #Make sure the position is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Pick a position from 1 to 9: ")

        position = int(position) -1  # "-1" is because we want number 1 for position 0 , 2 for 1 and so on

        #Make sure the spot is available on the board 
        if board[position] == "-":
            valid = True
        else:
            print("That space is already taken.Try again!")

    #Put the game piece on the board
    board[position] = player

    #Show the game board
    display_board()


def check_if_game_over():

    check_for_winner()
    check_if_tie()


def check_for_winner():

    #For global variables
    global winner

    #check rows
    row_winner = check_rows()

    #check columns
    column_winner = check_columns()

    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diagonal_winner:
        winner = diagonal_winner

    else:
        winner = None
    return


def check_rows():
    global game_playing

    #Check if any of the rows have the same value
    row_1 = board[0] == board[1] == board[2] != "-" 
    row_2 = board[3] == board[4] == board[5] != "-" 
    row_3 = board[6] == board[7] == board[8] != "-" 
    
    #If any row has a match, mark the win
    if row_1 or row_2 or row_3:
        game_playing = False 

    #Return the winner (X or O)
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return


def check_columns():
    global game_playing

    #Check if any of the rows have the same value
    column_1 = board[0] == board[3] == board[6] != "-" 
    column_2 = board[1] == board[4] == board[7] != "-" 
    column_3 = board[2] == board[5] == board[8] != "-" 
    
    #If any column has a match, mark the win
    if column_1 or column_2 or column_3:
        game_playing = False 

    #Return the winner
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return


def check_diagonals():
    global game_playing

    #Check if any of the rows have the same value
    diagonal_1 = board[0] == board[4] == board[8] != "-" 
    diagonal_2 = board[2] == board[4] == board[6] != "-" 
    
    #If any diagonal has a match, mark the win
    if diagonal_1 or diagonal_2:
        game_playing = False 

    #Return the winner (X or O)
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]
    return

def check_if_tie():
    global game_playing
    if "-" not in board:
        game_playing = False
    return


def change_player():
    global  current_player
    #If the current player was X, then change it to O 
    if current_player == "X":
        current_player = "O"
    #If the current player was O, then change it to X
    elif current_player == "O":
        current_player = "X"
    return




#This is where the game starts
GAME()