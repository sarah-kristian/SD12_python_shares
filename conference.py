# Program: Conference bookings manager
# Author: Phredd
# Date(s): Jul 11, 2024
 

# Define required libraries

import time
from constants_conference import HST_RATE, SMALL_VENUE, MED_VENUE, LARGE_VENUE, BREAKFAST, LUNCH, SUPPER, COFFEE_BREAK
    # I'm importing the constants from a separate file to keep the main program file clean and easy to read;
    # for the homework, this should be a .dat file, I focused on the main program file for this exercise



# Define program constants and global variables
ID_START = 999


# Define program functions

def progress_dots():
    # instead of a progress bar, I used dots to show progress
    total_iterations = 10 # The more iterations, the more time is takes.
    print("\nSaving information...", end="")
    for _ in range(total_iterations):  # '_' used instead of 'i' because the the variable is not used inside the loop
        time.sleep(0.3)  # Simulate a delay
        print(".", end="", flush=True)  # Print a dot and flush the output buffer
    print("\n")
    print()    
    print("Information saved!")

def get_last_id(file_path):
# This function reads the last line of the file and returns the first item in the line (the ID)
    try:
        with open(file_path, "r") as file:   # Use 'a' for append, 'w' for overwrite, 'r' to read
            lines = file.readlines()         # Read all lines in the file
            if lines:                        # Check if there are any lines in the file
                last_line = lines[-1]        # Get the last line in the file (it's a list so use -1 to get the last element)
                last_id = int(last_line.split(",")[0].strip())  # Split the line by comma and get the first element, then remove any leading or trailing spaces
                return last_id       # Return the first item of the last line (last_line[0])
            else:
                return ID_START      # Return the default value if the file is empty     
    except FileNotFoundError:
        return ID_START
    except Exception as e:  # Catch any other exceptions that may occur
        print(f"An error occurred while reading the file: {e}")     
        return ID_START     # Return the default value if an error occurs
    

def get_user_yesno(prompt):   
# retrives extra options in required 'Y' or 'N' format
    while True:
        option = input(prompt).upper().strip() 
        if option in ["Y", "N", "YES", "NO"]:
            return option 
        else:
            print("    ** Invalid input, please enter 'Y' for Yes or 'N' for No. **")

# Main program starts here

conference_num = get_last_id("Conference.dat")
conference_list = []

print()
print("Welcome to the Conference Bookings Manager!")
print()

while True:
    conference_num = conference_num + 1

    # Gather User Inputs
    # I didn't use validations here to keep things simpler. But I'm sad about it. 

    client_name = input("Enter the client name: ")
    if client_name == "END" or client_name == "end":
        print("Thank you for using the program. Have a good day!")
        break

    conference_title = input("Enter the conference title: ")
    start_date = input("Enter the start date of the conference (YYYY-MM-DD): ")
    num_days = int(input("Enter the number of days for the conference: "))
    max_attendees = int(input("Enter the maximum number of attendees: "))
    num_breakfasts = int(input("Enter the number of breakfasts: "))
    num_lunches = int(input("Enter the number of lunches: "))
    num_suppers = int(input("Enter the number of suppers: "))


    # Calculations

    if max_attendees <= 50:
        venue_cost = SMALL_VENUE
    elif max_attendees <= 100:
        venue_cost = MED_VENUE
    else:
        venue_cost = LARGE_VENUE

    meal_cost = (num_breakfasts * BREAKFAST) + (num_lunches * LUNCH) + (num_suppers * SUPPER) + (num_days * COFFEE_BREAK)
    conference_cost = num_days * (venue_cost + meal_cost)
    hst = conference_cost * HST_RATE

    conference_total = conference_cost + hst
    cost_per_attendee = conference_total / max_attendees


    # Store conference data in dictionary and add to conference_list
    conference_data = {
        "Conference Number": conference_num,
        "Client Name": client_name,
        "Conference Title": conference_title,
        "Start Date": start_date,
        "Number of Days": num_days,
        "Max Attendees": max_attendees,
        "Number of Breakfasts": num_breakfasts,
        "Number of Lunches": num_lunches,
        "Number of Suppers": num_suppers,
        "Venue Cost": venue_cost,
        "Meal Cost": meal_cost,
        "Conference Cost": conference_cost,
        "HST": hst,
        "Conference Total": conference_total,
        "Cost per Attendee": cost_per_attendee
    }
 
    
    conference_list.append(conference_data) # adds current conference data to the conference_list (initially empty list)


    # Display information for user to review. If they made a mistke, they can update the details (but they have to update all of them)
    print()
    print("Generating details for review...")
    time.sleep(1)
    for key, value in conference_data.items(): # Loop through the dictionary and print the key and value (the key is the label and the value is the data entered by the user)
        print(f"{key}: {value}")
    print()


    update = get_user_yesno("Do you want to update the details for this conference (Y / N)?: ")

    if update == "Y":
        print("Updating details...")
        print()
        del conference_list[-1]     # Delete the last item in the conference_list (the one that was just added)
        time.sleep(1)
        continue

    go_on = get_user_yesno("\nDo you want to continue for another conference (Y / N)?: ")

    if go_on == "N" or go_on == "NO":
        break

# Write processed data to a file for future use.
with open("Conference.dat", "a") as file:  # Use 'a' for append, 'w' for overwrite, 'r' to read
    for conference in conference_list:      # Loop through the conference_list and write each conference to the file (the dictionary keys won't be written, but the dictionary values will be written in the order they were added to the dictionary)
        file.write(f"{conference['Conference Number']}, {conference['Client Name']}, {conference['Conference Title']}, {conference['Start Date']}, {conference['Number of Days']}, {conference['Max Attendees']}, {conference['Number of Breakfasts']}, {conference['Number of Lunches']}, {conference['Number of Suppers']}, {conference['Venue Cost']}, {conference['Meal Cost']}, {conference['Conference Cost']}, {conference['HST']}, {conference['Conference Total']}, {conference['Cost per Attendee']}\n")


# housekeeping
progress_dots()
print()
print("Thanks for using this program! Have a great day.")
print()


