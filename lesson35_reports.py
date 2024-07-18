# Description: Practice with Python file I/O and generating reports
    # There are three functions that generate reports from a data file containing customer information
# Author: Phredd 
# Date: Jul 18, 2024




# Import the required libraries
from datetime import datetime


# Define the program constants and global variables
INTEREST_RATE = 0.05
MIN_PAY_RATE = 0.10
TODAY = datetime.now()
TODAY_DSP = TODAY.strftime('%b %d, %Y')


# Read and display the contents of the data file
#file_path = 'Python/lesson_practice/Lesson35_CustExtra.dat'

file_path = 'Lesson35_CustExtra.dat'

with open(file_path, 'r') as file: # Open the file in read mode 
    data = file.readlines()        # Read the lines of the file into a list








# Define funtions. There are three, two detailed reports and one exception report. 


# Function 1: extract and format the customer data for a detailed report of customer listings 

def detailed_report(data):
    # Define column headers and their widths
    columns = [
        ("CUSTOMER", "NUMBER", 10),
        ("CUSTOMER", "NAME", 20),
        ("PHONE", "", 14),
        ("        BALANCE", "         DUE", 15),
        ("      NEXT PAY", "      DATE", 20)
    ]
    
    # Create header lines dynamically
    header_line_1 = "".join([f"{column[0]:^{column[2]}}" for column in columns])
    header_line_2 = "".join([f"{column[1]:^{column[2]}}" for column in columns])

    header_lines = [
        "THE COMPANY NAME",
        "CUSTOMER LISTING",
        "",
        header_line_1,
        header_line_2,
        "="*80
    ]
    
    # Define footers
    footer = "="*80
    footer_total_template = "Total customers: {total_customers:<3}    ${total_balance:,.2f}"

    # Extract and format customer data. This will be the rows for the table. 
    customer_lines = []
    total_customers = 0
    total_balance = 0.0

    for line in data:
        # Assuming each line contains: customer_number, customer_name, phone, balance_due, next_pay_date
        fields = line.strip().split(',')
        customer_number = fields[0]
        customer_name = fields[1]
        phone = fields[2]
        balance_due = float(fields[3])
        balance_due_dsp = f"${balance_due:,.2f}"
        next_pay_date = datetime.strptime(fields[9].strip(), '%Y-%m-%d')
        next_pay_date_dsp = next_pay_date.strftime('%b %d, %Y')

        # Format the customer line
        customer_line = (
            f" {customer_number:<{columns[0][2]}}"
            f"{customer_name:<{columns[1][2]}}"
            f"{phone:^{columns[2][2]}}"
            f"{balance_due_dsp:>{columns[3][2]}}" 
            f"{next_pay_date_dsp:>{columns[4][2]}}"
        )

        # Add the customer line to the list of customer lines 
        customer_lines.append(customer_line)

        # Update the total customers and total balance
        total_customers += 1
        total_balance += balance_due

    # Construct the report
    report ='\n'.join(header_lines) + '\n' + \
            '\n'.join(customer_lines) + '\n' + \
            footer + '\n' + \
            footer_total_template.format(
                total_customers=total_customers,
                total_balance=total_balance
            )

    return report





# Function 2: extract and format the customer data for a detailed report giving customer status information

def detailed_report2(data):
    # Define column titles and their widths
    # The column titles are spline into two parts so they can be on two lines in the report
    # The last item in each tuple is the width of the column
    column_titles = [
        (" CUSTOMER ", " NUMBER ", 10),
        (" CUSTOMER ", " NAME ", 20),
        (" PHONE ", " NUMBER ", 14),
        (" BALANCE ", "DUE ", 14),
        (" MINIMUM ", "PAYMENT ", 14),
        (" DAYS SINCE ", " LAST PUR ", 12),
        (" DAYS SINCE ", " LAST PAY ", 12),
        (" CUSTOMER ", " STATUS ", 11),
    ]
    header_line1 = "".join([f"{column_title[0]:^{column_title[2]}}" for column_title in column_titles])
    header_line2 = "".join([f"{column_title[1]:^{column_title[2]}}" for column_title in column_titles])

    header_lines = [
        "THE COMPANY NAME",
        f"OVER CREDIT LIMIT REPORT AS OF {TODAY_DSP}",
        "",
        header_line1,
        header_line2,
        "="*111
    ]

    # definte rows (customer_lines) for the report
    customer_lines = []  # List to store the formatted customer lines

        #Initialize total variables
    total_customers = 0
    total_over_limit = 0


    for line in data:
         # Extract customer data from the file 
         # assumes each line in the file contains each item in the order listed, 
         # and that each item is seperated by a comma
        fields = line.strip().split(',')
        customer_number = fields[0]
        customer_name = fields[1]
        phone_number = fields[2]
        balance_due = float(fields[3])
        balance_due_dsp = f"${balance_due:,.2f}"
        credit_limit = float(fields[4])
        last_purchase_date = datetime.strptime(fields[5].strip(), '%Y-%m-%d')
      #  last_purtchase_amt = float(fields[6])
        last_pay_date = datetime.strptime(fields[7].strip(), '%Y-%m-%d')


        # calculate & format the payment due & amount over the credit limit for current line
        
        days_since_last_purchase = (TODAY - last_purchase_date).days
        days_since_last_pay = (TODAY - last_pay_date).days

        if balance_due <= credit_limit:
            minimum_payment = balance_due * MIN_PAY_RATE
            customer_status = "OK"
        elif balance_due > credit_limit:
            minimum_payment = (balance_due * MIN_PAY_RATE) + (balance_due - credit_limit)
            customer_status = "OVER"


        min_pay_dsp = f"${minimum_payment:,.2f}"

        # determine customer status
        if customer_status == "OVER":
            total_over_limit += 1
        
        if 0 <= credit_limit - balance_due <= 200:
            customer_status = customer_status + "-CHECK"
        
        if days_since_last_purchase > 60:
            customer_status = customer_status + "-PURCH"

        if days_since_last_pay > 30:
            customer_status = customer_status + "-PAY"


        # creating rows (customer lines) for report
        customer_line = (
            f" {customer_number:<{column_titles[0][2]}}"
            f"{customer_name:^{column_titles[1][2]}}"
            f"{phone_number:^{column_titles[2][2]}}"
            f"{balance_due_dsp:>{column_titles[3][2]}}"
            f"{min_pay_dsp:>{column_titles[4][2]}}"
            f"{days_since_last_purchase:^{column_titles[5][2]}}"
            f"{days_since_last_pay:^{column_titles[6][2]}}"
            f"{customer_status:>{column_titles[7][2]}}"
        )

        customer_lines.append(customer_line)

        # Update the total customers over the limit
        total_customers += 1

    
    footer_lines = [
        "="*111,
        f"TOTAL CUSTOMERS: {total_customers:<3}",
        f"CUSTOMERS OVER LIMIT: {total_over_limit:>3}"
    ]

    # Construct the report, joining headers, rows (customer_lines), and footers
    report = '\n'.join(header_lines) + '\n' + \
             '\n'.join(customer_lines) + '\n' + \
             '\n'.join(footer_lines) + '\n' 
                                                          
    return report






# Function 3: extract and format the customer data for an exception report of customers over the credit limit

def exception_report(data):
    # Define column titles and their widths
    # The column titles are spline into two parts so they can be on two lines in the report
    # The last item in each tuple is the width of the column
    column_titles = [
        ("CUSTOMER", "NUMBER", 10),
        ("CUSTOMER", "NAME", 20),
        ("PHONE", "NUMBER", 14),
        ("   CREDIT", "  LIMIT", 11),
        ("  AMOUNT", "  OVER", 11),
        ("NEXT PAY", "DATE", 16),
        ("     PAYMENT", "     DUE", 14),
    ]
    header_line1 = "".join([f"{column_title[0]:^{column_title[2]}}" for column_title in column_titles])
    header_line2 = "".join([f"{column_title[1]:^{column_title[2]}}" for column_title in column_titles])

    header_lines = [
        "THE COMPANY NAME",
        f"OVER CREDIT LIMIT REPORT AS OF {TODAY_DSP}",
        "",
        header_line1,
        header_line2,
        "="*97
    ]

    # definte rows (customer_lines) for the report
    customer_lines = []  # List to store the formatted customer lines

        #Initialize total variables
    total_customers = 0
    total_payment_due = 0.0


    for line in data:
         # Extract customer data from the file 
         # assumes each line in the file contains each item in the order listed, 
         # and that each item is seperated by a comma
        fields = line.strip().split(',')
        customer_number = fields[0]
        customer_name = fields[1]
        phone_number = fields[2]
        balance_due = float(fields[3])
        credit_limit = float(fields[4])
        credit_limit_dsp = f"${credit_limit:,.2f}"
        next_pay_date = datetime.strptime(fields[9].strip(), '%Y-%m-%d')
        next_pay_date_dsp = next_pay_date.strftime('%b %d, %Y')


        # calculate & format the payment due & amount over the credit limit for current line
        amount_over = balance_due - credit_limit
        amount_over_dsp = f"${amount_over:,.2f}"

        payment_due = (INTEREST_RATE * credit_limit) + balance_due
        payment_due_dsp = f"${payment_due:,.2f}"

        
        # creating rows (customer lines) for report
        customer_line = (
            f" {customer_number:<{column_titles[0][2]}}"
            f"{customer_name:^{column_titles[1][2]}}"
            f"{phone_number:^{column_titles[2][2]}}"
            f"{credit_limit_dsp:>{column_titles[3][2]}}" 
            f"{amount_over_dsp:>{column_titles[4][2]}}"
            f"{next_pay_date_dsp:>{column_titles[5][2]}}"
            f"{payment_due_dsp:>{column_titles[6][2]}}"
        )

        # add the row to the customer_lines list if the customer is over the credit limit
        if amount_over > 0:
            customer_lines.append(customer_line)

        # Update the total customers over the limit
        total_customers += 1

        # Update the total amount of payments due
        total_payment_due += payment_due
        total_due_dsp = f"${total_payment_due:,.2f}"
    
    footer_lines = [
        "="*97,
        f"Total customers: {total_customers:<3}    {total_due_dsp:>73}"
    ]

    # Construct the report, joining headers, rows (customer_lines), and footers
    report = '\n'.join(header_lines) + '\n' + \
             '\n'.join(customer_lines) + '\n' + \
             '\n'.join(footer_lines) + '\n' 
                                                          
    return report






# Main program starts here

# Generate reports (i.e., run the functions)
customer_listing = detailed_report(data)
extra_listing = detailed_report2(data)
over_credit_limit = exception_report(data)



# Output the reports
print()
print("Sample detailed report\n")
print(customer_listing)

print()
print("Sample detailed report 2\n")
print(extra_listing)

print()
print("Sample exception report\n")
print(over_credit_limit)
