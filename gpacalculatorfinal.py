def main_code():
    main_code()
restart = 0
gradeDict = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0}
ans = 0
cred = 0
credSum = 0
gradePointSum = 0
rate = 0
yesOrNo = 0
# Asking user how many classes they would like to calculate GPA for
nameOfUser = input("Hello there student! What is your name?")
print("Okay, " + nameOfUser + " time to calculate your GPA!")
print("Loading")
print(".")
print(".")
print(".")

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
            grade_of_class = input("What is the letter grade of your class?")
            if grade_of_class.lower() not in ('a', 'b', 'c', 'd', 'f'):
                print('You inserted an invalid letter grade, try again.')
                continue

            else:
                grade_of_class = grade_of_class.upper()
                cred = 0
                while not cred:
                    try:
                        cred = float(input("Enter the credits this class is worth."))
                    except ValueError:
                        print("Please enter only numeric values")
                        cred = 0

                    continue
                else:
                    gradePoint = gradeDict[grade_of_class] * cred
                gradePointSum = gradePointSum + gradePoint
                credSum = credSum + cred
                break
    print("Robots are calculating your GPA! Please wait.")
    print(".")
    print(".")
    print(".")


    # Calculate GPA and credits
    numeric_grade_of_class = gradeDict[grade_of_class]
    gradeSum = gradeSum + numeric_grade_of_class
    gpa = gradePointSum / credSum
    # Code gotten from https://stackoverflow.com/questions/9232256/round-up-to-second-decimal-place-in-python (To round GPA)
    from math import ceil

    num = gpa
    num = ceil(num * 100) / 100.0
    roundedGPA = str(num)
    print("Your GPA is: " + roundedGPA)
    if gpa > 3.0:
        print("Wow! Great grades!")
    while not rate:
        try:
            rate = int(input("Please rate your experience with this calculator from 1 to 5"))
            if rate not in (1, 2, 3, 4, 5):
                raise ValueError
        except ValueError:
            rate = 0
            print("Please insert a value between 1 and 5")

    if rate < 3:
                print("Sorry, this GPA calculator is still in development. Good luck with your classes!")
    else:
                print("We're glad you liked our calculator, good luck with your classes!")

restartProgram = input("Would you like to calculate your GPA again? 1 for yes, 2 for no.")

if restartProgram == "1":
        main_code()
else:
    exit()






