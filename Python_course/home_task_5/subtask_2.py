from Python_course.home_task_2.calculator import Calculator
from Python_course.home_task_5.errors import FormulaError, WrongOperatorError

calculator = Calculator()
attempts = 3

while attempts > 0:
    source_data = str(input("Enter your example: "))
    parts = source_data.split()
    supported_operations = {'*', '/'}

    try:
        if len(parts) != 3:
            raise FormulaError("Example has no 3 arguments")
        if parts[1] not in supported_operations:
            raise WrongOperatorError(f'{parts[1]} is not supported')

        operand_1 = float(parts[0])
        operand_2 = float(parts[2])
        result = 0.0

        if parts[1] == '*':
            result = calculator.multiply(operand_1, operand_2)
        elif parts[1] == '/':
            result = calculator.divide(operand_1, operand_2)

        print(round(result, 2))
    except FormulaError as ex:
        print("Formula is wrong: " + str(ex))
        attempts -= 1
    except WrongOperatorError as ex:
        print("Unsupported operation error: " + str(ex))
        attempts -= 1
    except ValueError as ex:
        print("Some of the values are invalid: " + str(ex))
        attempts -= 1
    except ZeroDivisionError as ex:
        print("Division by zero is not supported: " + str(ex))
        attempts -= 1

print("You exceeded 3 attempts!")
