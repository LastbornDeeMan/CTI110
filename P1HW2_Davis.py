# Ask user to enter their budget
# Ask user to enter travel destination
# Ask user for amount they will spend on gas
# Ask user for amount they will spend on accommodation
# Ask user for amount they will spend on food
# Add expenses
# Subtract expenses from budget
# Display results

# 9/19/23
# CTI-110 P1HW2 - Travel Expense
# Cameron Davis

print("What is your budget?")
budget = int(input())
print("What is your travel destination?")
destination = input() 
print("How much will you spend on gas?")
gas = int(input())
print("How much are you spending on accomadations?")
accomadations = int(input())
print("How much will you spend on food?")
food = int(input())

expenses = gas + accomadations + food 
print("Expenses", expenses)

balance = budget - expenses
print("Balance", balance)
