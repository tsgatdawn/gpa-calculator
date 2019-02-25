gradeDict = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0}
ans = 0
# Asking user how many classes they would like to calculate GPA for
while not ans:
    try:
        ans = int(input("Please input how many classes you would like to calculate your GPA for?"))
        if ans not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
            raise ValueError
    except ValueError:
        ans = 0
        print("Please insert a realistic number.")
# Using a for loop to stop whenever the user reached their class count
gradeSum = 0
for i in range(0, ans):
    # Asking user what grade they have for the class
    while True:
        grade_of_class = input("What is the letter grade of your first class?")
        if grade_of_class.lower() not in ('a', 'b', 'c', 'd', 'f'):
            print('You inserted an invalid letter grade, try again.')
            continue
        else:
            grade_of_class = grade_of_class.upper()
            break
# Calculate GPA
    numeric_grade_of_class = gradeDict[grade_of_class]
    gradeSum = gradeSum + numeric_grade_of_class
    GPA = gradeSum / ans
print(GPA)
