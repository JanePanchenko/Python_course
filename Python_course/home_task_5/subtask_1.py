source_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
source_numbers = list(map(int, source_numbers))
square_lambda = lambda number: number ** 2
squared_numbers = map(square_lambda, source_numbers)
result = zip(source_numbers, squared_numbers)
print(dict(result))
