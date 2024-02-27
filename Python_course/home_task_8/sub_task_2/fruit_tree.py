from Python_course.home_task_8.sub_task_2.tree import Tree


class FruitTree(Tree):    # inheritance
    def __init__(self, height: float, specious: str, age: float, is_deciduous: bool, is_evergreen: bool, fruit_type: str):
        super().__init__(height, specious, age, is_deciduous, is_evergreen)
        self.__fruit_type = fruit_type    # encapsulation

    def grow_per_month(self) -> None:
        self._height += 1.7

    def __str__(self) -> str:
        return f'{super().__str__()}, fruit_type = {self.__fruit_type}'
