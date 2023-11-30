   # A brief description of the project
   # 9/19/23
   # CTI-110 P2HW1 - Travel
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

print("-------------Travel---------------")
print(f"Destination is \t{destination}")
print(f"Gas costs \t${gas:.2f}")
print(f"Hotel costs\t${accomadations:.2f}")
print(f"Food costs \t${food:.2f}")
print("----------------------------------")
expenses = gas + accomadations + food 
print("Expenses", expenses)

balance = budget - expenses
print("Balance", balance)