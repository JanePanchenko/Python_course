from Python_course.home_task_9.error.full_carriage_error import FullCarriageError
from Python_course.home_task_9.passenger import Passenger


class RailwayCarriage:
    __passenger_list = []

    def __init__(self, number: int):
        self.number = number

    def add_passenger(self, passenger: Passenger) -> None:
        if len(self.__passenger_list) == 10:
            raise FullCarriageError('There is no free place in this carriage')
        self.__passenger_list.append(passenger)

    def __len__(self):
        return len(self.__passenger_list)

