from Python_course.home_task_2.calculator import Calculator

number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))
function = input("Enter your function: ")

calculator = Calculator()

if function == '+':
    print(calculator.sum(number_1, number_2))

if function == '-':
    print(calculator.subtract(number_1, number_2))

if function == '*':
    print(calculator.multiply(number_1, number_2))

if function == '/' and number_2 != 0:
    print(calculator.divide(number_1, number_2))
if number_2 == 0:
    print("You can't divide by zero")
