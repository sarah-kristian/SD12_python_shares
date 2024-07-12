# Description: Menu options for sprint programs
# Author Study Group 5
# Date: 2024-Jun-14 to 


# import libraries

from sprintQ1 import make_claim
from sprintQ2 import FizzBizzMenu
from sprintQ3 import CreateProfile
from sprintQ4 import MaintenanceScheduler
from sprintQ5 import AgeFacts

#define constants:
MENU = """
     .✧･ﾟ: *,｡✧･ﾟ:* ｡･:*:･ﾟ★,｡･:･ﾟ*:･ﾟ☆
     *           MAIN MENU          *
     .✧･ﾟ: *,｡✧･ﾟ:* ｡･:*:･ﾟ★,｡･:･ﾟ*:･ﾟ☆

        
       1. Complete Travel Claim
       2. Play Fizz Bizz 
       3. Create Employee Profile
       4. Marine Maintenance Scheduler
       5. Age Facts
       6. Exit

        
    ☆･ﾟ.✧･ﾟ: *,｡✧･ﾟ:* ｡･:*:･ﾟ★,｡･:･ﾟ*:･ﾟ
    """


# Main Program
def menu():

    play_again = True
    print()
    print("Study Group 5's Collection of Programs")
    print()

    
    while play_again == True:

        print(MENU)

    # User inputs        
        choice = input("\nEnter the number of the program would you like to run: ")

    # Calculations (function selector)    
        if choice == '1':
            make_claim()
        elif choice == '2':
            FizzBizzMenu()
        elif choice == '3':
            CreateProfile()
        elif choice == '4':
            MaintenanceScheduler()
        elif choice == '5':
            AgeFacts()
        elif choice == '6':
            print()
            print("Thanks for playing!")
            print()
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5 or 6.")
        

    # Housekeeping
        print()
        print()
        print("✧･ﾟ: *✧･ﾟ:* ｡･:*:･ﾟ★,｡･:*:･ﾟ☆.")
        print()
        continue_game = input("\nThanks for playing! Would you like to choose another program (Y/N)  ").lower().strip()
        if continue_game == "n" or continue_game == "no":
            play_again = False
            print()
            print("Have a great day!")
            print()
            print("✧･ﾟ: *✧･ﾟ:* ｡･:*:･ﾟ★,｡･:*:･ﾟ☆.")
            print()


if __name__ == "__main__":
    menu()