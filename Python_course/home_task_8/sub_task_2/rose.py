from Python_course.home_task_8.sub_task_2.flower import Flower


class Rose(Flower):    # inheritance

    def __init__(self, height: float, specious: str, age: float, petal_color: str, is_thorned: bool):
        super().__init__(height, specious, age, petal_color)
        self._is_thorned = is_thorned    # encapsulation

    def grow_per_month(self) -> None:
        self._height += 12.5

    def __str__(self) -> str:
        return f'{super().__str__()}, rose is_thorned = {self._is_thorned}'