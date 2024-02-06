def print_table(number: int, operation: str) -> None:
    for i in range(1, 11):
        if operation == '+':
            print(f'{number} + {i} = {number + i}')
        elif operation == '*':
            print(f'{number} * {i} = {number * i}')


def get_sum(number: int, operation: str) -> int:
    result = 0
    for i in range(number, number + 10):
        result += i
    print_table(number, operation)
    return result


if __name__ == '__main__':
    number = int(input("Enter number: "))
    operation = str(input("Enter operation: "))
    print("Sum is: " + str(get_sum(number, operation)))
