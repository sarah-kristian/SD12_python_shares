# Description: Create Employee Profile
# Author:      Study Group 5
# Date:        2024-06-17


from datetime import datetime, timedelta
import time
import random

from input_handler_g5 import get_user_date, get_user_text, get_user_phone, get_user_yesno
from display_handler_g5 import FPhone, date_str, dsp_date


# Define program constants and global variables
RETIRMENT_AGE = 65
SPECIAL_CHARACTERS = ["!", "@", "#", "$", "%", "&"]
CurDate = datetime.now() 

# Main program

def CreateProfile():

    # Introduction for user
    print()
    print()
    print("***** Organizing Employee Details *****")
    print()
    print("To get started, please provide the following information: ")
    print()


    while True:

        # Gather user inputs:

        EmpFirst = get_user_text("Employee first name:   ")
        EmpLast =  get_user_text("Employee last name:    ")
        PhoneNum = get_user_phone("Employee Phone number: ")

        while True:
            StartDate = get_user_date("Start date (YYYY-MM-DD): ")
            if StartDate > CurDate:
                print("   Data Entry Error - Start Date cannot be earlier than today.")
            else:
                break
    
        while True:
            BirthDate = get_user_date("Birthdate (YYYY-MM-DD):  ") 
            if BirthDate > StartDate:
                print("   Data Entry Error - Birthdate must be earlier than start date.")
            else:
                break
    

        # Perform required calculations


        CurDate1 = date_str(CurDate)
        StartDate1 = date_str(StartDate)
        BirthDate1 = date_str(BirthDate)

        #Employee ID
        EmpID = EmpFirst[0] + EmpLast[0] + PhoneNum[6:10] + StartDate1[:2] + BirthDate1[2:6]

        #User name
        UserName = EmpFirst.lower() + "." + EmpLast.lower() + "@keyin.com"

        #Password
        Char = random.choice(SPECIAL_CHARACTERS)
        PassW = EmpLast[1] + CurDate1[3] + Char + EmpFirst.upper()[1] + EmpLast.lower()[1] + EmpFirst.lower()[0] + PhoneNum[2] + EmpFirst.upper()[0]+StartDate1[6]
        
        
        # Calculate how long the employee is working (years, months, days)

            # When No negative values, no adjustment is needed. 
            # e.g., Current date 2024-06-15, Start date 2018-01-10.


        YWPeriod = CurDate.year - StartDate.year       #Number of Years
        MWPeriod = CurDate.month - StartDate.month     #Number of Months
        DWPeriod = CurDate.day - StartDate.day         #Number of Days


            # When there are Negative Values: 
            # occurs when the current month/day is a smaller value than the start month/day
            # e.g., Current date 2024-06-15, Start date 2023-12-20.

        if DWPeriod < 0:
            MWPeriod -= 1
            DaysPrevMonth = (CurDate.replace(day=1) - timedelta(days=1)).day
            DWPeriod += DaysPrevMonth

        if MWPeriod < 0:
            YWPeriod -= 1
            MWPeriod += 12



        # Calculate Next Birthday

            # if Birth date is greater than current date that means the Birthdate will be in the same year
        if (CurDate.month, CurDate.day) < (BirthDate.month, BirthDate.day):
            NextBirthYear = CurDate.year
        else:
            # if the Birthdate is less that means the Birthdate will be in next year 
            NextBirthYear = CurDate.year + 1
        
        NextBirthday = datetime(NextBirthYear, BirthDate.month, BirthDate.day)


        MonthsNBirthday = NextBirthday.month - CurDate.month
        DaysNBirthday = NextBirthday.day - CurDate.day

        if DaysNBirthday < 0:
            MonthsNBirthday -= 1
            DaysPrevMonth = (CurDate.replace(day=1) - timedelta(days=1)).day
            DaysNBirthday += DaysPrevMonth

        if MonthsNBirthday < 0:
            MonthsNBirthday += 12


        # Calculate Retirement 
        
        RetirementDate = BirthDate.replace(year=BirthDate.year + RETIRMENT_AGE)
        YearsRetirment = RetirementDate.year - CurDate.year
        MonthsRetirement = RetirementDate.month - CurDate.month
        DaysRetirment = RetirementDate.day - CurDate.day

        if DaysRetirment < 0:
            MonthsRetirement -= 1
            DaysPrevMonth = (CurDate.replace(day=1) - timedelta(days=1)).day
            DaysRetirment += DaysPrevMonth

        if MonthsRetirement < 0:
            YearsRetirment -= 1
            MonthsRetirement += 12



        # Display output
        print()
        print("Calculating employee details...")
        time.sleep(2)  # Pauses the program for 2 seconds
        print()
        print()
        print("--------- Employee Profile ---------")
        print()
        print(f"Employee Name: {EmpFirst} {EmpLast}")
        print()
        print(f"Phone Number:  {FPhone(PhoneNum)}")
        print()
        print(f"Current Date:  {dsp_date(CurDate)}")
        print(f"Start Date:    {dsp_date(StartDate)}")
        print(f"Birth date:    {dsp_date(BirthDate)}")

        print()
        print(f"Employee ID:   {EmpID}")
        print()
        print(f"User Name:     {UserName}")
        print()
        print(f"Password:      {PassW}")
        print()
        print(f"Working Period:    {YWPeriod} years,  {MWPeriod} months, and {DWPeriod} days")
        print(f"Retirement in:     {YearsRetirment} years, {MonthsRetirement} months, and {DaysRetirment} days")
        print(f"Next Birthday in:  {MonthsNBirthday} months and {DaysNBirthday} days")
        print()
        print()


        Continue = get_user_yesno("Do you want to update the details of the last entered employee (Y / N)?: ")

        if Continue == "Y":
            print()
            print("Updating the last entered employee details...")
            print()
            continue

        # Check if user wants to continue
        Continue = get_user_yesno("Do you want to continue for another employee (Y / N)?: ")


        if Continue == "N":
            print()
            print("Thank you for using our Program. Sensitive data cleaned up!")
            print()
            break


if __name__ == "__main__":
    CreateProfile()
