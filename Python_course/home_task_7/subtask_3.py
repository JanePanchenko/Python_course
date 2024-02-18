import time


def evaluate_function_execution_time(function):
    def wrapper(value: int) -> int:
        start_time = time.time()
        result = function(value)
        end_time = time.time()
        print(f"Execution of function {function.__name__} took {end_time - start_time} seconds")
        return result

    return wrapper


@evaluate_function_execution_time
def calculate_sum_of_diapason(value: int) -> int:
    result = 0
    for counter in range(0, value):
        result += counter

    return result


print(f"The result is {calculate_sum_of_diapason(50000000)}")
