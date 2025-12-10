# Ana Otero
# Date: October 31, 2025
# P4HW1 - Score List and Grade Calculation
# Pseudocode:
# 1. Ask user how many scores they want to enter
# 2. Loop through that number of scores
# 3. Validate input (must be between 0 and 100)
# 4. Store valid scores in a list
# 5. Remove the lowest score
# 6. Display lowest score, modified list, average, and letter grade
num_scores = int(input("How many scores do you want to enter? "))
scores = []
for i in range(num_scores):
 score = float(input(f"Enter score #{i+1}: "))
 while score < 0 or score > 100:
 print("INVALID Score entered!!!!")
 print("Score should be between 0 and 100")
 score = float(input(f"Enter score #{i+1} again: "))
 scores.append(score)
lowest = min(scores)
scores.remove(lowest)
average = sum(scores) / len(scores)
if average >= 90:
 grade = "A"
elif average >= 80:
 grade = "B"
elif average >= 70:
 grade = "C"
elif average >= 60:
 grade = "D"
else:
 grade = "F"
print("----------------Results-----------------")
print(f"Lowest Score : {lowest:.1f}")
print(f"Modified List : {scores}")
print(f"Scores Average : {average:.2f}")
print(f"Grade : {grade}")
print("----------------------------------------")