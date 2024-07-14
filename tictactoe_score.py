# Tic Tac Toe with score
# Phredd
# Date: 2024-June-12


# Game Set up

import os

def clear_screen():
    os.system('clear')  # For Unix/Linux/MacOS

board_spaces = {
    "A1": "     ",
    "B1": "     ",
    "C1": "     ",
    "A2": "     ",
    "B2": "     ",
    "C2": "     ",
    "A3": "     ",
    "B3": "     ",
    "C3": "     ",
}

players = ["X","O"]

def create_board():
    return(f"""
    {"        "}{"  1   "}{"  2   "}{"  3  "}
 
    {"        "}{"     "}|{"     "}|{"     "}
    {"   A    "}{board_spaces["A1"]}|{board_spaces["A2"]}|{board_spaces["A3"]}
    {"        "}{"_____"}|{"_____"}|{"_____"}
    {"        "}{"     "}|{"     "}|{"     "}
    {"   B    "}{board_spaces["B1"]}|{board_spaces["B2"]}|{board_spaces["B3"]}
    {"        "}{"_____"}|{"_____"}|{"_____"}
    {"        "}{"     "}|{"     "}|{"     "}
    {"   C    "}{board_spaces["C1"]}|{board_spaces["C2"]}|{board_spaces["C3"]}
    {"        "}{"     "}|{"     "}|{"     "}
    """)


def mark_board(board_spaces, player):
    while True:
        cell = input(f"\n{player}'s turn. Please choose a space on the board: ").strip().upper()
        if cell in board_spaces and board_spaces[cell] != f"  X  " and board_spaces[cell] != "  O  ":
            board_spaces[cell] = f"  {player}  "  # Update the cell with 'X' or 'O'
            newboard = create_board()
            return newboard
        else:
            print("That space is already taken. Please pick an empty space on the board.")



def check_winner(board_spaces, player):
    winning_combinations = [
        ["A1", "A2", "A3"],  # column 1
        ["B1", "B2", "B3"],  # column 2
        ["C1", "C2", "C3"],  # column 3
        ["A1", "B1", "C1"],  # row 1
        ["A2", "B2", "C2"],  # row 2
        ["A3", "B3", "C3"],  # row 3
        ["A1", "B2", "C3"],  # Diagnol 1
        ["C1", "B2", "A3"],  # Diagnol 2
    ]
    
    for combination in winning_combinations:
        if all(board_spaces[cell] == f"  {player}  " for cell in combination):
            return True
    return False

def player_move(player):
    mark = mark_board(board_spaces, player)
    clear_screen()
    print()
    print()
    print(mark)
    


# Game instructions

def print_instructions():
    print(f"""
        
        {"Example Game Board:"}

        {"        "}{"  1   "}{"  2   "}{"  3  "}
                        
        {"        "}{"     "}|{"     "}|{"     "}                                   
        {"  A     "}{"  X  "}|{board_spaces["A2"]}|{board_spaces["A3"]}               X is in A1.
        {"        "}{"_____"}|{"_____"}|{"_____"}                                    
        {"        "}{"     "}|{"     "}|{"     "}
        {"  B     "}{board_spaces["B1"]}|{"  O  "}|{board_spaces["B3"]}               O is in B2.
        {"        "}{"_____"}|{"_____"}|{"_____"}
        {"        "}{"     "}|{"     "}|{"     "}
        {"  C     "}{board_spaces["C1"]}|{board_spaces["C2"]}|{board_spaces["C3"]}
        {"        "}{"     "}|{"     "}|{"     "}
            
        {"To play the game, players take turns to mark a space on the board with their symbol ('X' or 'O')."}
        {"The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins the game."}
        {"If all spaces on the board are filled and no player has three in a row, the game is a draw."}
        {"The game board is represented as a grid with rows labeled A, B, C and columns labeled 1, 2, 3."}
        {"Players choose a space by typing the row and column labels (e.g. 'A1' or 'B3')."}
        {"The game continues until a player wins or there is a draw."}
""")

# Game Set up

#starting board

def tictactoe():
    print("Welcome to Tic Tac Toe!")
    print()
    start_board = create_board()
    print(start_board)
    print()
    see_instructions = input("Would you like an explanation of the game board?  ").lower().strip()
    if see_instructions in ["yes", "y"]:
        print_instructions()

    print(input("Press Enter to continue.  "))

# Game play
    while True:

        board_spaces = {
            "A1": "     ",
            "B1": "     ",
            "C1": "     ",
            "A2": "     ",
            "B2": "     ",
            "C2": "     ",
            "A3": "     ",
            "B3": "     ",
            "C3": "     ",
        }

        o_win_count = 0
        x_win_count = 0
        draw_count = 0


        clear_screen()
        print("\nLet's start!\n")
        print(start_board)
        
        count = 0
        while True:
            move = player_move("X")

            count += 1

            if check_winner(board_spaces, "X") == True:
                x_win_count += 1
                print("X wins!")
                break

            if count < 9:
                move = player_move("O")
            else: 
                draw_count += 1
                print("It's a draw!")
                break

            if check_winner(board_spaces, "O") == True:
                o_win_count += 1
                print("O wins!")
                break

            count += 1

        print("\nGood game\n")

        print(f"""  Score:    X   |   O   |  draw
            ---------------------
            {x_win_count}   |   {o_win_count}   |   {draw_count}""")

        while True:
            play_again = input("\nWould you like to play again?:  ").upper().strip()
            if play_again not in ["YES", "Y", "NO", "N"]:
                print(input("please type 'yes' or 'no'"))
            elif play_again == "YES" or play_again == "Y":
                clear_screen()
                break
            else:
                break

        if play_again == "NO" or play_again == "N":
            print("Goodbye!")
            break



# housekeeping

if __name__ == "__main__":
    tictactoe()

