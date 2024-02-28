from Python_course.home_task_9.error.full_carriage_error import FullCarriageError
from Python_course.home_task_9.passenger import Passenger
from Python_course.home_task_9.error.passenger_addition_forbidden_error import PassengerAdditionForbiddenError
from Python_course.home_task_9.train import Train

train = Train()
for i in range(0, 10):
    train.add_carriage()
print(train)

try:
    locomotive = train.get_carriage(0)
    passenger = Passenger('Jane', 'Panchenko')
    locomotive.add_passenger(passenger)
except PassengerAdditionForbiddenError as ex:
    print(ex.message)

carriage = train.get_carriage(5)
try:
    for i in range(0, 11):
        passenger = Passenger(f'Name{i}', f'Surname{i}')
        carriage.add_passenger(passenger)
except FullCarriageError as ex:
    print(ex.message)

print(f'Carriage number {carriage.number} consists of {len(carriage)} passengers')