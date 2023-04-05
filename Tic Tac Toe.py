import random
def display_board(board):
    """Display the Tic Tac Toe Board
            board(list): Range of 10, index 0 not used
    """
    print(board[7] + " | " + board[8] +  " | " + board[9])
    print(board[4] + " | " + board[5] +  " | " + board[6])
    print(board[1] + " | " + board[2] +  " | " + board[3])

def player_input():
    """Assign the player marker, either X or O. Player 1 to choose.
            return(tuple): (player1 marker, player2 marker)
    """
    marker = ""
    while not (marker == "X" or marker == "O"):
        marker = input("Player 1 - Please pick a marker 'X' or 'O': ")

    if marker == "X":
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    """Place the marker of the player in the corresponding position on the board
            board(list)
            marker(string): Either 'X' or 'O'
            position(integer): Between 1 and 9
    """
    board[position] = marker

def win_check(board, mark):
    """Check if either of the players have won. Need to check if a marker is the same
        across any rows, columns or diagonals
            return(bool): True if match
    """
#Re-write as for loop
    return ((board[7] == board[8] == board[9] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[1] == board[2] == board[3] == mark) or

            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or

            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))

def choose_first():
    """Randomly choose which player will go first"""
    if random.randint(0,1) == 0:
        return "Player 2"
    else:
        return "Player 1"

def space_check(board, position):
    """Check if a space is empty
            board(list)
            position(int): Between 1 and 9
    """
    return board[position] == " "

def full_board_check(board):
    """Check if the board is full
            return(bool): True if all spaces are empty
    """
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    """Player to choose position. Must be in range of 1-9 where a space is empty
            return(int): Valid position number
    """
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position (1-9): '))
    return position

def replay():
    """When the game is over, ask the play if they want to play again"""
    choice = input("Do you want to play again? Enter Yes or No: ")
    return choice == 'Yes'


def main():
    print("Welcome to Tic Tac Toe!")

    while True:
        # Set up the board
        the_board = [" "] * 10
        player1_marker, player2_marker = player_input()

        # Determine who will go first
        turn = choose_first()
        print(turn + " will go first")

        #start the game
        game_on = True
        while game_on:
            if turn == "Player 1":
                print(turn + " your turn")
                #Show the board, choose position, place marker
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, player1_marker, position)

                #Check if they won
                if win_check(the_board,player1_marker):
                    display_board(the_board)
                    print("Player 1 has won!")
                    game_on = False
                #Check if there is a tie
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("The game is a tie")
                        break
                    # Not win or draw - Player 2 turn
                    else:
                        turn = "Player 2"

            else:
                # Player 2 turn - same
                print(turn + " your turn")
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, player2_marker, position)

                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print("Player 2 has won!")
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("The game is a tie")
                        break
                    else:
                        turn = "Player 1"

        if not replay():
                break

main()
Footer