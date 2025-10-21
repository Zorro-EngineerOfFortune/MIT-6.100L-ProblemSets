## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("please state the initial deposit: "))
#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
house_cost = 800000
down_payment = house_cost * 0.25
months = 36
steps = 0
r = 0
amount_saved = 0
##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
while amount_saved < down_payment - 100:
    if initial_deposit >= down_payment - 100:
        print("here is the rate of return: 0.0")
        break
    amount_saved = initial_deposit * ((1 + r / 12)) ** months
    steps += 1
    r = r + 0.01
    if r > 1:
        r = None
        steps = 0
        break
print("here is the rate of return:", r, "here is amount of steps:", steps)
