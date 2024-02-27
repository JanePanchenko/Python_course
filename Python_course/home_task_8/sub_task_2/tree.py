from Python_course.home_task_8.sub_task_2.plant import Plant


class Tree(Plant):    # inheritance
    def __init__(self, height: float, specious: str, age: float, is_deciduous: bool, is_evergreen: bool):
        super().__init__(height, specious, age)
        self.__is_deciduous = is_deciduous    # encapsulation
        self.__is_evergreen = is_evergreen    # encapsulation

    def grow_per_month(self) -> None:
        self._height += 2.5

    def __str__(self) -> str:
        return f'{super().__str__()}, tree is_deciduous = {self.__is_deciduous}, tree is_evergreen = {self.__is_evergreen}'

