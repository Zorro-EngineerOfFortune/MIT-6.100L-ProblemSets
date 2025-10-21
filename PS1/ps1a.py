## 6.100L PSet 1: Part A
## Name:Ruslan Nevzorov
## Time Spent:
## Collaborators: None

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################

# Constants and Initial Variables
portion_down_payment = 0.25  # The required percentage for the down payment
r = 0.05  # Annual investment return rate (r)
months = 0  # Counter for the number of months passed
amount_saved = 0.0  # Current total amount of savings
monthly_saved_salary = 0.0  # Placeholder for monthly contribution

# Get user inputs as strings and converts them into floats
yearly_salary = float(input("please state your starting yearly salary: "))
portion_saved = float(
    input("please indicate in fractions what portion of your salary should be saved: ")
)
cost_of_dream_home = float(input("please state the cost of your dream house: "))

# Calculate fixed initial values
down_payment = portion_down_payment * cost_of_dream_home
monthly_salary = yearly_salary / 12

# Main calculation loop
while amount_saved <= down_payment:
    # 1. Calculate the return on investment for the month
    invest_return = amount_saved * (r / 12)
    # 2. Add monthly contribution and investment return to total savings
    monthly_saved_salary = portion_saved * monthly_salary
    amount_saved += monthly_saved_salary + invest_return
    # 3. Increment the month counter
    months = months + 1
    print(months)
print("here is how many months it will take to get the dream house -", months)
