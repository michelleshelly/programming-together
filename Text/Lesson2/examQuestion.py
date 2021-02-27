
studentInput = input('What is 5 * 5?')
#scope
integerConvertedStudentInput = 0 #default

try:
    #some code
    integerConvertedStudentInput = float(studentInput)
except:
    #exception handling code
    print("That is not even a number")

if (integerConvertedStudentInput == 5*5):
    print("correct!")
else:
    print("wrong!")