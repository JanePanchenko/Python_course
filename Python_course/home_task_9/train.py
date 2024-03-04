from typing import List

from Python_course.home_task_9.locomotive import Locomotive
from Python_course.home_task_9.railway_carriage import RailwayCarriage


class Train:

    def __init__(self):
        self.__railway_carriage_list: List[RailwayCarriage] = [Locomotive()]

    def add_carriage(self):
        number_of_carriages = len(self.__railway_carriage_list)
        carriage = RailwayCarriage(number_of_carriages)
        self.__railway_carriage_list.append(carriage)

    def get_carriage(self, number: int) -> RailwayCarriage:
        for carriage in self.__railway_carriage_list:
            if carriage.number == number:
                return carriage

    def __len__(self) -> int:
        return len(self.__railway_carriage_list) - 1

    def __str__(self) -> str:
        train_representation = '<='
        for carriage in self.__railway_carriage_list:
            train_representation += '-['
            if isinstance(carriage, Locomotive):
                train_representation += 'HEAD'
            else:
                train_representation += str(carriage.number)
            train_representation += ']'
        return train_representation
