# Input handler for Study Group 5


# import libraries

from datetime import datetime


# input validation

def get_user_date(prompt):
    while True:
        date = input(prompt).strip().replace("/", "-")
        try:
            return datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("   Data Entry Error - Date is not in a valid format (YYYY-MM-DD).")



def secure_get_date(prompt):
    #It allows the user a reasonable number of attempts to enter the date correctly before the program exits.
    attempt = 0
    while attempt < 3:
        try:
            date = input(prompt).replace("/", "-")
            date = datetime.strptime(date, "%Y-%m-%d")
        except:
            print("   Data Entry Error - Date is not in a valid format (YYYY-MM-DD).")
            attempt += 1
        else:
            return date
    print("   Too many invalid attempts. Exiting...")
    exit()





def get_user_info(prompt):  
# input validation to ensure string isn't blank 
    while True:
        info = input(prompt).title().strip()
        if info != "":
            return info
        else: 
            print("   Data Entry Error - Field must not be blank. Please re-enter. ")

def get_user_text(prompt):
# input validation to ensure string isn't blank and contains only alpha characters, apostrophe, or hyphen
    while True:
        text = input(prompt).title().strip()
        if text == "":
            print("   Data Entry Error - Field cannot be blank.")
        elif not text.isalpha():
            print("   Data Entry Error - Field cannot contain numbers or special characters.")
        else:
            return text


def get_user_phone(prompt):
    while True:
        PhoneNum = input(prompt).replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
        if PhoneNum == "":
            print("   Data Entry Error - Phone number cannot be blank.")
        elif len(PhoneNum) != 10:
            print("   Data Entry Error - Phone number must be 10 digits.")
        elif not PhoneNum.isdigit():
            print("   Data Entry Error - Phone Number contains invalid characters.")
        else:
            return PhoneNum


def get_year(prompt): 
# input validation for year (YYYY); should be updated if want year to be a current-ish year
    while True:
        year = input(prompt).strip()
        if year.isdigit() is False:
            print("   Data Entry Error - Year must be written as digits.")
        elif len(year) != 4:
            print("    Data Entry Error - Please enter a valid year (YYYY).")
        else:
            return year


def get_user_float(prompt):
# input validation for floats
    while True:
        try:
            digits = float(input(prompt))
            return digits
        except:
            print("   Data Entry Error - Please enter a valid number for cost.")


def get_user_yesno(prompt):   
# retrives extra options in required 'Y' or 'N' format
    while True:
        option = input(prompt).upper().strip() 
        if option in ["Y", "N"]:
            return option 
        else:
            print("   Data Entry Error - please enter 'Y' for Yes or 'N' for No.")



def get_user_option(prompt, option_set):   
# retrives extra options in required format set (shown in a list)
    while True:
        option = input(prompt).upper().strip() 
        if option in option_set:
            return option 
        else:
            print("   Data Entry Error - please enter and option from the list.")
