from Python_course.home_task_9.passenger import Passenger
from Python_course.home_task_9.error.passenger_addition_forbidden_error import PassengerAdditionForbiddenError
from Python_course.home_task_9.railway_carriage import RailwayCarriage


class Locomotive(RailwayCarriage):

    def __init__(self):
        super().__init__(0)

    def add_passenger(self, passenger: Passenger) -> None:
        raise PassengerAdditionForbiddenError('You cannot add a passenger in locomotive')

