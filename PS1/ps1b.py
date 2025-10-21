## 6.100L PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################

yearly_salary = float(input("please state your starting yearly salary: "))
portion_saved = float(
    input("please indicate in fractions what portion of your salary should be saved: ")
)
cost_of_dream_home = float(input("please state the cost of your dream house: "))
semi_annual_raise = float(
    input("please state the semi raise of your salary, in decimals: ")
)

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

portion_down_payment = 0.25  # The required percentage for the down payment
r = 0.05  # Annual investment return rate (r)
months = 0  # Counter for the number of months passed
amount_saved = 0  # Current total amount of savings (starts at 0)
monthly_saved_salary = 0  # Current monthly saved salary (starts at 0)


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ##
###############################################################################################
# Calculate fixed initial values (one-time calculations)
# Calculating the monthly salary and the initial monthly contribution.
# The amount contributed each month will change as the salary changes.
down_payment = portion_down_payment * cost_of_dream_home
monthly_salary = yearly_salary / 12

# Main calculation loop
while amount_saved <= down_payment:
    # 1. Calculate the return on investment for the month
    # This MUST remain in the loop as amount_saved changes monthly.
    invest_return = amount_saved * (r / 12)
    # 2. Calculate the monthly contribution from the current salary
    monthly_saved_salary = portion_saved * monthly_salary
    # 3. Update the total savings
    amount_saved += monthly_saved_salary + invest_return
    # 4. Increment the month counter
    months = months + 1
    # 5. Check for and apply the semi-annual raise
    # The raise is applied AFTER month 6, 12, 18, etc.
    # Use modulo (%) to check if 6 months have passed.
    if months % 6 == 0:
        monthly_salary = monthly_salary + monthly_salary * semi_annual_raise
    print(months)
# Output the final result
print("here is how many months it will take to get the dream house -", months)
