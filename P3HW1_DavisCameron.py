"""
CTI 110
P3HW1 - Letter Grades
Davisc
9/28/23

"""

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

print("-"*10, "Results", "-"*10)

sum = module1 + module2 + module3 + module4 + module5 + module6

average = sum / len(data)
print("Sum:", sum)
print("Average:", average)

print("-"*12, "Grades", "-"*12)

print("Enter the number grade: ", end="")
num_grade = average

if num_grade >= 90:
  letter_grade = "A"
elif num_grade >= 80:
  letter_grade = "B"
elif num_grade >= 70:
  letter_grade = "C"
elif num_grade >= 60:
  letter_grade = "D"
else: 
  letter_grade = "F"

print("A grade of", num_grade, " is a", letter_grade)