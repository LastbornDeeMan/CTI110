# CTI-110
# P4HW1 - Score List
# Cameron Davis
# 10/31/23
#

#print("How many scores do you want to enter? ")
#num_scores = int(input())

num_scores = int(input("Enter the number of scores you want to enter: "))

score_list = []

for i in range(num_scores):
    score = float(input("Enter a score: "))
    while score < 0 or score > 100:
        print("Invalid score!")
        score = float(input("Enter a score between 0 and 100: "))
    score_list.append(score)

lowest_score = min(score_list)
modified_list = score_list.copy()
modified_list.remove(lowest_score)
average = sum(modified_list) / len(modified_list)

if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print("-"*10, "Results", "-"*10)
print("Lowest score entered:", lowest_score)
print("Score List after dropping lowest score:", modified_list)
print("Average of scores in modified list:", average)
print("Letter grade:", letter_grade)


