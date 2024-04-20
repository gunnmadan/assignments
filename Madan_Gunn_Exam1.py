exam_grade = float(input("Enter your exam grade: "))

if exam_grade >= 90: 
    letter_grade = "A"
elif exam_grade >= 80: 
    letter_grade = "B"
elif exam_grade >= 70: 
    letter_grade = "C" 
elif exam_grade >= 60: 
    letter_grade = "D"
else: 
    letter_grade = "F"

print("Your letter grade is: ", letter_grade)

if letter_grade == 'A' or letter_grade == 'B' or letter_grade == 'C':
    print("You Passed")
else: 
    print("You Failed")
