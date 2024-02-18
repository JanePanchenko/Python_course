def print_function_name(function):
    def wrapper(number1: float, number2: float) -> float:
        print(f"The following function is called: {function.__name__}")
        return function(number1, number2)

    return wrapper


@print_function_name
def sum(number1: float, number2: float) -> float:
    return number1 + number2


@print_function_name
def multiply(number1: float, number2: float) -> float:
    return number1 * number2


print(sum(5, 5))
print(multiply(9, 9))
