# 9/22/23
# CTI-110 P2HW2 - List
# Cameron Davis

#Asks the user to enter grades for following tests. Each grade is to be requested in a separate statement
print("Enter grade for module 1:")
module1 = int(input())
print("Enter grade for module 2:")
module2 = int(input())
print("Enter grade for module 3:")
module3 = int(input())
print("Enter grade for module 4:")
module4 = int(input())
print("Enter grade for module 5:")
module5 = int(input())
print("Enter grade for module 6:")
module6 = int(input())
data = [module1, module2, module3, module4, module5, module6]

#The program should store the grades entered in a list. Give the list created a descriptive name
print("-"*10, "Results", "-"*10)
print("Best Grade:", max(data))
print("Worst Grade:",  min(data))

sum = module1 + module2 + module3 + module4 + module5 + module6
print("Sum of grades:", sum)

average = sum / len(data)
print("Sum:", sum)
print("Average:", average)
