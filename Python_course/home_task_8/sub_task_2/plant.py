from abc import abstractmethod, ABC


class Plant(ABC):    # abstraction, inheritance
    def __init__(self, height: float, specious: str, age: float):
        self._height = height    # encapsulation
        self.__specious = specious    # encapsulation
        self.__age = age    # encapsulation

    @abstractmethod    # abstraction
    def grow_per_month(self) -> None:
        pass

    def __str__(self) -> str:
        return f'Plant: height = {self._height}, specious = {self.__specious}, age = {self.__age}'