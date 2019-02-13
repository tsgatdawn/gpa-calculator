grade_point_one = 0
grade_point_two = 0
grade_point_three = 0
grade_point_four = 0


while True:
    grade_class_one = input('What grade do you have in class one? (Please enter a capital letter grade)? ')
    if grade_class_one.lower() not in ('a', 'b', 'c', 'd', 'f'):
        print('You inserted an invalid letter grade, try again.')
        continue
    else:
        break
if grade_class_one == "A" or grade_class_one == "a":
    grade_point_one += 4.0
elif grade_class_one == "B" or grade_class_one == "b":
    grade_point_one += 3.0
elif grade_class_one == "C" or grade_class_one == "c":
    grade_point_one += 2.0
elif grade_class_one == "D" or grade_class_one == "d":
    grade_point_one += 1.0
elif grade_class_one == "F" or grade_class_one == "f":
    grade_point_one += 0.0


print ('So in class one, your grade is' ,grade_class_one)
credit_class_one = input ('How much credit/s is the class worth? ')
print ("In " + "class one " + "you have " + credit_class_one + " credits.")

while True:
    grade_class_two = input('What grade do you have in class two? (Please enter a capital letter grade)? ')
    if grade_class_two.lower() not in ('a', 'b', 'c', 'd', 'f'):
        print('You inserted an invalid letter grade, try again.')
        continue
    else:
        break


if grade_class_two == "A" or grade_class_two == "a":
    grade_point_two += 4.0
elif grade_class_two == "B" or grade_class_two == "b":
    grade_point_two += 3.0
elif grade_class_two == "C" or grade_class_two == "c":
    grade_point_two += 2.0
elif grade_class_two == "D" or grade_class_two == "d":
    grade_point_two += 1.0
elif grade_class_two == "F" or grade_class_two == "f":
    grade_point_two += 0.0

print ('So in class two, your grade is' ,grade_class_two)
credit_class_two = input ('How much credit/s is the class worth? ')
print ("In " + "class two " + "you have " + credit_class_one + " credits.")

while True:
    grade_class_three = input('What grade do you have in class three? (Please enter a capital letter grade)? ')
    if grade_class_three.lower() not in ('a', 'b', 'c', 'd', 'f'):
        print('You inserted an invalid letter grade, try again.')
        continue
    else:
        break

if grade_class_three == "A" or grade_class_three == "a":
    grade_point_three += 4.0
elif grade_class_three == "B" or grade_class_three == "b":
    grade_point_three += 3.0
elif grade_class_three == "C" or grade_class_three == "c":
    grade_point_three += 2.0
elif grade_class_three == "D" or grade_class_three == "d":
    grade_point_three += 1.0
elif grade_class_three == "F" or grade_class_three == "f":
    grade_point_three += 0.0

print ('So in class three, your grade is' ,grade_class_three)
credit_class_three = input ('How much credit/s is the class worth? ')
print ("In " + "class three " + "you have " + credit_class_one + " credits.")

while True:
    grade_class_four = input('What grade do you have in class four? (Please enter a capital letter grade)? ')
    if grade_class_four.lower() not in ('a', 'b', 'c', 'd', 'f'):
        print('You inserted an invalid letter grade, try again.')
        continue
    else:
        break

if grade_class_four == "A" or grade_class_four == "a":
    grade_point_four += 4.0
elif grade_class_four == "B" or grade_class_four == "b":
    grade_point_four += 3.0
elif grade_class_four == "C" or grade_class_four == "c":
    grade_point_four += 2.0
elif grade_class_four == "D" or grade_class_four == "d":
    grade_point_four += 1.0
elif grade_class_four == "F" or grade_class_four == "f":
    grade_point_four += 0.0

print('So in class four, your grade is' ,grade_class_four)
credit_class_four = input ('How much credit/s is the class worth? ')
print("In " + "class four " + "you have " + credit_class_one + " credits.")

total_gpa = (grade_point_one + grade_point_two + grade_point_three + grade_point_four) / 4
print("Your GPA is: " + str(total_gpa))

