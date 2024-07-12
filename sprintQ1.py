# Description: A program to process salesperson travel claims
# Author: Sprint Study Group 5
# Dates: June 17-18, 2024 

# Import libraries.

import datetime
from input_handler_g5 import get_user_text

# Define program constants.
DAILY_RATE = 85.00
HST_RATE   = 0.15
RENTAL_PAY = 65.00
BONUS_DAYS = 100.00
BONUS_OWN  = 0.04 # cents per kilometer on own vehicle
BONUS_TYPE = 45.00
BONUS_DEC  = 50.00
KILO_RATE = 0.17
MAX_DAY = 7
KM_MAX = 2000


# Define program functions.



def Calculate_Bonus(NumDays,KmTraveled,CarUsed,ClaimType,StartDate):
   bonus=0
   if NumDays > 3:
      bonus+=BONUS_DAYS
   if KmTraveled > 1000 and CarUsed=="O":
      bonus+=(KmTraveled-1000)*BONUS_OWN

   if ClaimType=="E":
      bonus+=NumDays*BONUS_TYPE

   if StartDate >= datetime.datetime(StartDate.year, 12, 15) and StartDate <= datetime.datetime(StartDate.year, 12, 22):
      bonus+=(NumDays*BONUS_DEC)
     
   return bonus


# Main program starts.

def make_claim():

   # Gather user input.
   print()
   while True:
      UserChoice = input("Would you like to start a new claim (Y / N): ").upper()
      print()
      if UserChoice not in ["Y", "N"]:
         print("     Data Entry Error - invalid characters, Y or N only.")
      elif UserChoice == "N":
         print("Ending the program...") 
         print()
         break
      else:
               
         while True:
            EmpNum = input("Enter your 5-digit employee number (99999): ")

            if EmpNum == "":
               print("     Data Entry Error - Employee Number cannot be blank.")
            elif len(EmpNum) != 5:
               print("     Data Entry Error - Employee Number must have 5 digits.")
            elif not EmpNum.isdigit():
               print("     Data Entry Error - Employee Number contains invalid characters, please re-enter.")
            else: 
               break


         FirstName = get_user_text("Enter your first name: ")
         LastName =  get_user_text("Enter your last name:  ")
         Location =  input("Enter your branch location: ").title().strip()
         (print)

               
         while True:
            try:
               StartDate = input("Enter trip start date (YYYY-MM-DD): ")
               StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
            except:
               print("     Data Entry Error - start date is not in a valid format.")
            else:
               break

                           
         while True:
            try:
               EndDate = input("Enter trip end date (YYYY-MM-DD):   ")
               EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
               if StartDate > EndDate:
                  print("   Data Entry Error - End date must be later than the start date.")
               elif (EndDate - StartDate).days <= 0 or (EndDate - StartDate).days > MAX_DAY:
                  print(f"   Data Entry Error - End date must be after the start date by no more than {MAX_DAY} days.")
               else:
                  break
            except:
               print("     Data Entry Error - end date is not in a valid format.")

         print()         
         while True:

            Vehicle = input("Did you travel in your own car (O) or rented (R)?: ").upper() 
            if Vehicle == "O": 
               while True:
                  print("    Note: You will be compensated for kms travelled in excess of 1000 (to a max of 2000km).")
                  print()
                  try:
                     TotKilo = input("Please enter the number of kilometers travelled (must be under 2000km): ")     
                     VehicleDsp = "Own"
                     TotKilo = float(TotKilo)
                     if TotKilo > KM_MAX:
                        print(f"   Data Entry Error - Kilometer traveled cannot exceed {KM_MAX}")
                     else:
                        VehicleDsp = "Own"
                        print()
                        break
                  except :
                     print("   Data Entry Error - Please enter a valid number for kilometers.")
               break
            elif Vehicle == "R":
               VehicleDsp = "Rented"
               TotKilo = 0 #No kilometers needed for rented vehicle
               break
            else:
               print("    Data Entry Error - Invalid characters, O or R only.")

            
                 
        
                                    
         ClaimType = input("Enter Standard (S) or Executive (E) claim type:    ").upper()
         if ClaimType == "S":
            ClaimTypeDsp = "Standard"
         else:
            ClaimTypeDsp = "Executive"


        

           

         NumDays = (EndDate - StartDate).days + 1
         PerDiemAmt = NumDays * DAILY_RATE


         if Vehicle == "O":
            CarAmt = TotKilo * KILO_RATE
         else:
            CarAmt = NumDays*RENTAL_PAY

         TotalBonus =Calculate_Bonus(NumDays,TotKilo,Vehicle,ClaimType,StartDate)

        

         

         ClaimAmt = PerDiemAmt + CarAmt + TotalBonus  

         HST = ClaimAmt * HST_RATE

         TotClaim = ClaimAmt + HST


         # Format display output. 
         StartDateDsp = datetime.datetime.strftime(StartDate, "%Y-%m-%d")
         EndDateDsp = datetime.datetime.strftime(EndDate, "%Y-%m-%d")
         PerDiemAmtDsp = "${:,.2f}".format(PerDiemAmt)
         CarAmtDsp = "${:,.2f}".format(CarAmt)
         TotalBonusDsp = "${:,.2f}".format(TotalBonus)  
         ClaimAmtDsp = "${:,.2f}".format(ClaimAmt)
         HSTDsp = "${:,.2f}".format(HST)
         TotClaimDsp = "${:,.2f}".format(TotClaim)

         # Display results.
         print()
         print()
         print(f"  ------------------------------------------------------------------------")
         print(f"                           NL Chocolate Company                                                 ")
         print(f"                             123 Cocoa Street                                                   ")
         print(f"                          St. John's, NL A1A 1A1                                                ")
         print(f"  ------------------------------------------------------------------------")
         print(f"   Employee #:   {EmpNum:>5}                    Location: {Location:<9s}                    ")
         print(f"  ------------------------------------------------------------------------")
         print(f"   Customer:   {LastName + ', ' + FirstName:<20s}       Vehicle Type:     {VehicleDsp:<9}   ")
         if Vehicle == "O":
            print(f"                                          Km Driven:      {TotKilo:>9.2f}                ")
         print(f"                                                                                            ") 
         print(f"   Start Date: {StartDateDsp}                 End Date:         {EndDateDsp}                ")
         print(f"   Claim Type: {ClaimTypeDsp:<14}             Num Travel Days:  {NumDays}                   ")  
         print()                       
         print(f"                                          -----------------------------")
         print(f"                                          Per Diem Amount:{PerDiemAmtDsp:>12s}              ")
         print(f"                                          Car Amount:     {CarAmtDsp:>12}                   ")                      
         print(f"                                          Bonus Amount:   {TotalBonusDsp:>12}               ")
         print(f"                                          Claim Amount:   {ClaimAmtDsp:>12s}                ")
         print(f"                                                                                            ")
         print(f"                                          HST:            {HSTDsp:>12s}                     ")
         print(f"                                                             ---------                      ")
         print(f"                                          Claim Total:    {TotClaimDsp:>12s}                ")
         print()
         print(f"  ------------------------------------------------------------------------")
         print(f"   Please submit this form with all associated receipts & invoices       ")
         print("                       within 72hrs of return.  ")
         print(f"  ------------------------------------------------------------------------")  
         print()             
         print(f"""   Note: Applicable bonuses calculated based on length of time, 
         travelled, travel over holidays, kilometers driven, and claim type. """)
         print()






# Housekeeping.

if __name__ == "__main__":
  make_claim()