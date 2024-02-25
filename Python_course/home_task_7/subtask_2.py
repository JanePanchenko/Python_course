def squared_pair_numbers_generator():
    for i in range(0, 1000000000):
        if i % 2 == 0:
            yield i * i


for value in squared_pair_numbers_generator():
    print(value)
