gp = 0

grade_class_one = input ('What grade do you have in FAT? ')
if grade_class_one == "A":
    gp = gp + 4.0
elif grade_class_one == "B":
    gp = gp + 3.0
elif grade_class_one == "C":
    gp = gp + 2.0
elif grade_class_one == "D":
    gp = gp + 1.0
elif grade_class_one == "F":
    gp = gp + 0.0
grade_class_one = int(grade_class_one)
print ('So in FAT, your grade is' ,grade_class_one)
credit_class_one = input ('How much credit/s is the class worth? ')
print ("In " + "FAT " + "you have " + credit_class_one + " credits.")

grade_class_two = input ('What grade do you have in Writing 121? ')
grade_class_two = int(grade_class_two)
if grade_class_two == "A":
    gp = gp + 4.0
elif grade_class_two == "B":
    gp = gp + 3.0
elif grade_class_two == "C":
    gp = gp + 2.0
elif grade_class_two == "D":
    gp = gp + 1.0
elif grade_class_two == "F":
    gp = gp + 0.0
print ('So in Writing 121, your grade is' ,grade_class_two)
credit_class_two = input ('How much credit/s is the class worth? ')
print ("In " + "Writing 121 " + "you have " + credit_class_one + " credits.")

grade_class_three = input ('What grade do you have in CAD 1? ')
grade_class_three = int(grade_class_three)
if grade_class_three == "A":
    gp = gp + 4.0
elif grade_class_three == "B":
    gp = gp + 3.0
elif grade_class_three == "C":
    gp = gp + 2.0
elif grade_class_three == "D":
    gp = gp + 1.0
elif grade_class_three == "F":
    gp = gp + 0.0
print ('So in CAD 1, your grade is' ,grade_class_three)
credit_class_three = input ('How much credit/s is the class worth? ')
print ("In " + "CAD 1 " + "you have " + credit_class_one + " credits.")

grade_class_four = input ('What grade do you have in AP Computer Science Principles? ')
grade_class_four = int(grade_class_four)
if grade_class_four == "A":
    gp = + 4.0
elif grade_class_four == "B":
    gp = + 3.0
elif grade_class_four == "C":
    gp = + 2.0
elif grade_class_four == "D":
    gp = + 1.0
elif grade_class_four == "F":
    gp = + 0.0
print ('So in AP Computer Science Principles, your grade is' ,grade_class_four)
credit_class_four = input ('How much credit/s is the class worth? ')
print ("In " + "AP Computer Science Principles " + "you have " + credit_class_one + " credits.")

total_gpa = grade_class_one + grade_class_two + grade_class_three + grade_class_four
print("Your GPA is: " + total_gpa)

