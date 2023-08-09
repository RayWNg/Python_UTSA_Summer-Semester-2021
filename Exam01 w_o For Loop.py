# Exam 01, Chapters 01-04
# Student Name: Raymond Ng
# Student ID: JQG999

# This program calculates a car salesperson's paycheck in a given month
# based on the following conditions
# Every salesperson gets 10 percent commission of total sales amount
# Sales totals greater than 50 thousand dollars get 5 percent bonus of
# total sales amount
# 8 or more cars sold earns salesperson a 3 percent bonus of total sales amount
# Sales totals greater than 50 thousand dollars and8 or more cars earns
# the salesperson an 8 percent bonus of total sales amount

def commission_calculator():                                     # Using 'def' to mark the start of the function header
    
    print("To Calculate Salesperson\'s Paycheck")

    total_cars_sold = int(input("Enter Number of Cars Sold: "))  # Number of cars sold
    total_sales = 0
    
    # for i in range(total_cars_sold):
    total_sales = int(input("Sales Amount: $"))    # Total sales of cars
    
    # Calculating commissions
    paycheck = total_sales / 10                           # 10 percent commission of total sales amount
    
    if(total_cars_sold >= 8 and total_sales > 50000):     # If 8 or more cars sold and amount is more than 50 thousand dollars
        paycheck += (total_sales * (8 / 100))             # 8 percent bonus
    elif(total_sales > 50000):                            # If sales is more than 50 thousand dollars
        paycheck += (total_sales * (5 / 100))             # 5 percent bonus
    elif(total_cars_sold >= 8):                           # If sold number of cars is 8 or more
        paycheck += (total_sales * (3 / 100))             # 3 percent bonus
    else:
        paycheck = paycheck
        
    print()
    print("Total Sales Amount of Cars Sold: $", total_sales)
    print()
    print("Salesperson\'s Paycheck is: $", paycheck)
    print()
    print()    
    
commission_calculator()

print("Would you like to Calculate Another Saleperson\'s Paycheck? (Choose an option)")
print("1. Calculate Another Paycheck")
print("2. Exit")

n = int(input("Enter Option Here: "))

if n==1:                         # If user chooses to calculate another salesperson's paycheck
    commission_calculator()
else:
    pass                         # If user chooses to exit the program