grade_point_one = 0
grade_point_two = 0
grade_point_three = 0
grade_point_four = 0


grade_class_one = input ('What grade do you have in FAT? ')
if grade_class_one == "A":
    grade_point_one += 4.0
elif grade_class_one == "B":
    grade_point_one += 3.0
elif grade_class_one == "C":
    grade_point_one += 2.0
elif grade_class_one == "D":
    grade_point_one += 1.0
elif grade_class_one == "F":
    grade_point_one += 0.0
else :
    print('You inserted a wrong grade!')

print ('So in FAT, your grade is' ,grade_class_one)
credit_class_one = input ('How much credit/s is the class worth? ')
print ("In " + "FAT " + "you have " + credit_class_one + " credits.")

grade_class_two = input ('What grade do you have in Writing 121? ')

if grade_class_two == "A":
    grade_point_two += 4.0
elif grade_class_two == "B":
    grade_point_two += 3.0
elif grade_class_two == "C":
    grade_point_two += 2.0
elif grade_class_two == "D":
    grade_point_two += 1.0
elif grade_class_two == "F":
    grade_point_two += 0.0
else:
    print('You inserted a wrong grade!')
print ('So in Writing 121, your grade is' ,grade_class_two)
credit_class_two = input ('How much credit/s is the class worth? ')
print ("In " + "Writing 121 " + "you have " + credit_class_one + " credits.")

grade_class_three = input ('What grade do you have in CAD 1? ')

if grade_class_three == "A":
    grade_point_three += 4.0
elif grade_class_three == "B":
    grade_point_three += 3.0
elif grade_class_three == "C":
    grade_point_three += 2.0
elif grade_class_three == "D":
    grade_point_three += 1.0
elif grade_class_three == "F":
    grade_point_three += 0.0
else :
    print('You inserted a wrong grade!')
    print('You inserted a wrong grade!')
print ('So in CAD 1, your grade is' ,grade_class_three)
credit_class_three = input ('How much credit/s is the class worth? ')
print ("In " + "CAD 1 " + "you have " + credit_class_one + " credits.")

grade_class_four = input ('What grade do you have in AP Computer Science Principles? ')

if grade_class_four == "A":
    grade_point_four += 4.0
elif grade_class_four == "B":
    grade_point_four += 3.0
elif grade_class_four == "C":
    grade_point_four += 2.0
elif grade_class_four == "D":
    grade_point_four += 1.0
elif grade_class_four == "F":
    grade_point_four += 0.0
else :
    print('You inserted a wrong grade!')
print('So in AP Computer Science Principles, your grade is' ,grade_class_four)
credit_class_four = input ('How much credit/s is the class worth? ')
print("In " + "AP Computer Science Principles " + "you have " + credit_class_one + " credits.")

total_gpa = (grade_point_one + grade_point_two + grade_point_three + grade_point_four) / 4
print("Your GPA is: " + str(total_gpa))

