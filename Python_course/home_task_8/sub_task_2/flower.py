from Python_course.home_task_8.sub_task_2.plant import Plant


class Flower(Plant):    # inheritance

    def __init__(self, height: float, specious: str, age: float, petal_color: str):
        super().__init__(height, specious, age)
        self.__petal_color = petal_color    # encapsulation

    def grow_per_month(self) -> None:
        self._height += 10.0

    def __str__(self) -> str:
        return f'{super().__str__()}, flower petal_color = {self.__petal_color}'
