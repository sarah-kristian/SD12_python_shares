# Description: Equipment Maintenance Scheduler
# Author:      Study Group 5
# Date:        2024-06-18 to 2024-06-22


import datetime
import time
import random
from input_handler_g5 import get_user_date, get_user_float, get_user_yesno, get_user_info
from display_handler_g5 import dsp_date, float_value


# Define program constants and global variables
USEFUL_LIFE_YEARS = 15
SALVAGE_RATE= 0.10
TODAY = datetime.datetime.now()
'''
CLEAN_PERIOD = ""       # days    
CHECK_PERIOD = ""       # weeks  
MJR_INSPEC_PERIOD = ""  # months  
'''

CLEAN_PERIOD = "clean_period"       # days    
CHECK_PERIOD = "check_period"       # weeks  
MJR_INSPEC_PERIOD = "mjr_inspec_period"  # months  

equipment_list = []

#schedules types

fast_schedule = {
CLEAN_PERIOD : 3,        # basic  cleaning  in  3  days
CHECK_PERIOD : 2,        # tube  and  fluid  checks  in 2 weeks 
MJR_INSPEC_PERIOD : 1,   # major  inspection  in  1 month
}


reg_schedule = {
CLEAN_PERIOD : 10,       # days  
CHECK_PERIOD : 3,        # weeks  
MJR_INSPEC_PERIOD : 6,   # months 
}

slow_schedule = {
CLEAN_PERIOD : 20,        # days    
CHECK_PERIOD : 5,         # weeks   
MJR_INSPEC_PERIOD : 11,   # months 
}



# Functions

def print_table(headers, combined_lists):
    # Creates table with a header 
    column_widths = [max(len(str(item)) for item in column) for column in zip(headers, *combined_lists)]
    row_format = " | ".join("{:<" + str(width) + "}" for width in column_widths)
    print(row_format.format(*headers))
    print("-+-".join("-" * width for width in column_widths))
    for row in combined_lists:
        print(row_format.format(*row))


def print_summary_list(title, lists):
    # Creates summary list for all pieces of equipment entered
    print()
    print(title)
    print("-" * 41)
    for index, item in enumerate(lists, 1):
        title = f"EQUIPMENT {index}"
        print(f"{title:^41}")
        print("-" * 41)
        for key, value in item.items():
            print(f"{key + ':':<26}{value:>15}")
        print("-" * 41)



# Main program: 

def  MaintenanceScheduler():
# Introduction for user
    print()
    print()
    print("***** Welcome to the Marine Equipment Maintenance Scheduler *****")
    print()
    print()
    print("To get started, please provide the following information: ")
    print()

    # User input to enter main loop

# Main Loop
    while True:
    # Input Validation
  
        equip_name = get_user_info("Equipment name:  ").title()


        while True:
            Cost = get_user_float("Enter the purchase cost of the equipment:      ")
            if Cost < 100 or Cost > 10000:
                print("   Data Entry Error - Cost should be between $100 and $10,000.")
            else:
                break

        while True:      
            PurchDate = get_user_date("Enter purchase date (YYYY-MM-DD):              ")
            if PurchDate > datetime.datetime.now():
                print(f"   Data Entry Error - Purchase date should be in the past.")
            elif datetime.datetime.now().year - PurchDate.year > USEFUL_LIFE_YEARS:
                print(f"   We do not maintain equipment older than 15 years.")
            else:
                break      

        print()
        print("""Three schedule types are available, depending on your needs:
              
        Schedule Type       |   Typical    |  Accelerated  |  Relaxed
        --------------------+--------------+---------------+-----------
        Basic Clean         |   10 days    |    3 days     |  20 days
        Fluid & Tube Checks |    3 weeks   |    2 weeks    |   5 weeks
        Major Inspection    |    6 months  |    1 months   |  11 months
              """)
        
        while True:
            schedule_type = get_user_info("Please select a schedule type (typical, accelerated, relaxed): ").lower()
            if schedule_type in ["relaxed", "r"]:
                pace = slow_schedule
                schedule_type = "Relaxed"
                break
            elif schedule_type in ["typ", "t", "typical"]:
                pace = reg_schedule
                schedule_type = "Typical"
                break        
            elif schedule_type in ["accelerated", "a"]:
                pace = fast_schedule
                schedule_type = "Accelerated"
                break
            else:
                print("   Data Entry Error - please choose A, T, or R.")

    # Calculations

        
        OrderNum = f"MER-{TODAY.month}-{TODAY.day}-{random.randint(1,101)}"

        # Maintenance Schedule
        CleanDate = PurchDate + datetime.timedelta(days=pace[CLEAN_PERIOD])
        if CleanDate < TODAY:
            pastdue_msg = "Behind schedule!"
        else: 
            pastdue_msg = "None"
        TubeFluidDate = PurchDate + datetime.timedelta(weeks=pace[CHECK_PERIOD])



                # Calculate Major Inspection Date
        Month = PurchDate.month + pace[MJR_INSPEC_PERIOD]     #First we add 6 months to purchase Date
        Year = PurchDate.year + (Month - 1) // 12  # this will maintain the year to be either in same year or next year

                #(If the purchased month was in 07 (July) when we add 6 months it will be 13. the below will solve the problem )
        Month = (Month - 1) % 12 + 1   # To ensure the month in the required span (e.g., adding 6 month)
        day = PurchDate.day
        try:
            MajorInspecDate = PurchDate.replace(year=Year, month=Month, day=day)
        except:
                #Calculate the last day of the current month when it is needed
            LastMonthDay = (PurchDate.replace(year=Year, month=Month + 1, day=1) - datetime.timedelta(days=1)).day
            MajorInspecDate = PurchDate.replace(year=Year, month=Month, day=LastMonthDay)



        # Monthly Amortization Calculation
        SalvageValue = Cost * SALVAGE_RATE
        MonAmortization = (Cost - SalvageValue) / (USEFUL_LIFE_YEARS * 12)


        # Store equipment data in dictionary and add to list
        equipment_data = {
            "Equipment Name": equip_name,
            "Maintenance Pace": schedule_type, 
            "Purchase Date": dsp_date(PurchDate),
            "Cost": float_value(Cost),
            "Basic Cleaning Date": dsp_date(CleanDate),
            "Tube and Fluid Check Date": dsp_date(TubeFluidDate),
            "Major Inspection Date": dsp_date(MajorInspecDate),
            "Salvage Value": float_value(SalvageValue),
            "Monthly Amortization": float_value(MonAmortization),
            "Alert Message": pastdue_msg 
        }
        equipment_list.append(equipment_data)


    # Format display outputs

        longbar = "-" * 41                                                      #longbar = (f"{"-" * 41}")
        equipment_name_length = len(equipment_data["Equipment Name"])
        titlebar = "-" * int(10 - (equipment_name_length * 0.5))                #titlebar = (f"{"-" * int(10-(len(equipment_data["Equipment Name"]))* .5)}")

    # Display output

        print()
        print("Generating details for review...")
        time.sleep(1)
        print()
        print()
        print(f"{titlebar}{' ' + equipment_data['Equipment Name'] + ' Maintenance Details '}{titlebar}")
        print()
        print(f"{'Purchase Date: ':<28} {equipment_data['Purchase Date']:>12}")
        print(f"{'Purchase Value: ':<28} {equipment_data['Cost']:>12}")
        print()
        print(f"{'Schedule Type: ':<28} {schedule_type:>12}")
        print(f"{'Basic Cleaning Date: ':<28} {equipment_data['Basic Cleaning Date']:>12}")
        print(f"{'Tube and Fluid Check Date: ':<28} {equipment_data['Tube and Fluid Check Date']:>12}")
        print(f"{'Major Inspection Date: ':<28} {equipment_data['Major Inspection Date']:>12}")
        print()
        print(f"{'Salvage Value: ':<28} {equipment_data['Salvage Value']:>12}")
        print(f"{'Monthly Amortization: ':<28} {equipment_data['Monthly Amortization']:>12}")
        if CleanDate < TODAY:
            print()
            print("*ALERT: maintanence is behind schedule*")
        print()
        print(longbar)
        print("\n")


        Continue = get_user_yesno("Do you want to update the details of the last entered equipment (Y / N)?: ")
    
        if Continue == "Y":
            print("Updating the last entered equipment details...")
            print()
            del equipment_list[-1]
            time.sleep(1)
            continue

        Continue = get_user_yesno("\nDo you want to continue for another piece of equipment (Y / N)?: ")

        if Continue == "N":
            break

# End main loop
# Extracting the 'Cost' value from each dictionary
    headers = ["Equipment", "Cleaning", "Checks", "Inspection"]

    all_equip_names = [equipment['Equipment Name'] for equipment in equipment_list]
    all_cleaning_dates = [equipment['Basic Cleaning Date'] for equipment in equipment_list]
    all_check_dates = [equipment['Tube and Fluid Check Date'] for equipment in equipment_list]
    all_inspection_dates = [equipment['Major Inspection Date'] for equipment in equipment_list]

    combined = list(zip(all_equip_names,all_cleaning_dates, all_check_dates, all_inspection_dates))


# Display all entered equipment details
    print()


    whale = """
                  .
                 ":"
               ___:____     |"\/"|
             ,'        `.    \  /
             |  O        \___/  |
           ~^~^~^~^~^~^~^~^~^~^~^~"""
    
    print(whale)
    print("       MARINE EQUIPMENT MAINTENANCE")
    print()
    print()
    print(f"Order#: {OrderNum}      Date: {dsp_date(TODAY)}")
    print("-----------------------------------------")
    print()
    print_summary_list("Summary of All Entered Equipment: \n", equipment_list)
    print()
    print()
    print("Summary of Maintenance Dates:\n")
    print()
    print_table(headers, combined)
    print()
    print()
    print("------------------------------------------------")
    print("{:^47}".format("Your Trusted Partner in Marine Maintenance"))
    print(f"------------------------------------------------")
    print(f"")
    print(f"")


# Housekeeping
    print("Thanks for using our maintenance scheduler. Have a nice day.")


if __name__ == "__main__":
    MaintenanceScheduler()

