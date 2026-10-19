# Samat
# 10/18/2026
# Averages 3 exam grades, then prints the average, the letter grade,
# and whether the student is passing.
# 90+ A, 80-89 B, 70-79 C, 60-69 D, 0-59 F

examOne = int(input("Input exam grade one: "))
examTwo = int(input("Input exam grade two: "))
examThree = int(input("Input exam grade three: "))

grades = [examOne, examTwo, examThree]
total = 0
for grade in grades:
    total = total + grade

avg = round(total / len(grades))

if avg >= 90:
    letterGrade = "A"
elif avg >= 80:
    letterGrade = "B"
elif avg >= 70:
    letterGrade = "C"
elif avg >= 60:
    letterGrade = "D"
else:
    letterGrade = "F"

print("Exams: " + str(examOne) + ", " + str(examTwo) + ", " + str(examThree))
print("Average: " + str(avg))
print("Grade: " + letterGrade)

if letterGrade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")
