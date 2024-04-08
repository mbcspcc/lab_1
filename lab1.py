#*****************************************************************************
# Author:          Margret Bailey G04288409
# Assignment:      CIS-133Y 2024 Spring Lab 1
# Date:            04/07/24
# Description:     A test/debug/refactor of a program designed to calculate
#                    total costs (item cost(s), calculated tax, shipping)
#                    and display the results to screen with total remit amt
# Input:           4 inputs (1 repeating); itemCost (float - 1-n entries),
#                    more (string) - asks user whether there are more items,
#                    taxRate (float), shippingCost (float)
# Output:          totalCost (float - sum of itemCost entries),
#                    taxRate * totalCost (float), shippingCost (float),
#                    remittance line (float); various string wrapper
# Sources:         Class materials
#*****************************************************************************



# Shopping program
# Inputs: float cost, float taxRate, float shipping
# Outputs: float totalPrice

def main():
    taxRate = 0.0
    shippingCost = 0.0
    totalCost = 0.0

    totalCost = getItemCosts()
    taxRate, shippingCost = getOtherCosts()
    printReceipt(totalCost, taxRate, shippingCost)

    print("Thank you!")
#    print(totalCost)
#    print(taxRate)
#    print(totalCost * taxRate)
#    print(shippingCost)

# getItemCosts() prompts a user for a list of item
# costs and returns the sum
def getItemCosts():
    itemCost = 0.0
    totalCost = 0.0
    more = 'y'

    while more == 'y':
        itemCost = float(input("Enter item cost $ "))
        totalCost = totalCost + itemCost
        more = input("Do you have more items (y/n): ")

    return totalCost

# getOtherCosts() prompts a user for the tax rate
# and shipping costs and returns both inputs
def getOtherCosts():
    taxRate = 0.0
    shippingCost = 0.0

    taxRate = float(input("\nEnter tax rate (i.e. .075 for 7.5%): "))
    shippingCost = float(input("Enter shipping costs $ "))

    return taxRate, shippingCost

# printReceipt() accepts total cost, tax rate, and
# shipping costs and calculates and prints the tax 
# amount, and total cost
def printReceipt(totalCost, taxRate, shippingCost):
    print("\nSubtotal: $ ", format(totalCost, ".2f"))
    print("Tax: $", format((taxRate * totalCost), ".2f"))
    print("Shipping: $", format(shippingCost,".2f"))
    print("------------------------")
    print("Please pay: $", format(totalCost + (taxRate * totalCost) + shippingCost, ".2f"))

main()