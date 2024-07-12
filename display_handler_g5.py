# display_handler.py

# import libraries
from datetime import datetime


#sprintQ3



def date_str(DateValue):
    # Function will accept a value and format it
    DateValueStr = DateValue.strftime("%Y%m%d")
    return DateValueStr 


def dsp_date(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd
    DateValueStr = DateValue.strftime("%Y-%m-%d")
    return DateValueStr


def FPhone(PhoneNum):
    # Returns a phone number in this format: (999) 999-9999
    Phone = "(" + PhoneNum[0:3] + ") " + PhoneNum[3:6] + "-" + PhoneNum[6:]
    return(Phone)


def float_value(value):
    # Function will accept a value and format it to $#,###.##.
    ValueStr = f"${value:,.2f}"
    return ValueStr




