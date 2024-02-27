from Python_course.home_task_8.sub_task_2.flower import Flower
from Python_course.home_task_8.sub_task_2.fruit_tree import FruitTree
from Python_course.home_task_8.sub_task_2.plant import Plant
from Python_course.home_task_8.sub_task_2.rose import Rose
from Python_course.home_task_8.sub_task_2.tree import Tree


def grow(plant: Plant) -> None:
    plant.grow_per_month()    # polymorphism


chamomile_flower = Flower(7, 'aster family', 25, 'white')
rose_flower = Rose(10, 'roses family', 21, 'red', True)
oak_tree = Tree(150, 'beech family', 53650, True, False)
apple_tree = FruitTree(120, 'fruit family', 13990, False, False, 'apple')

print(f'Before growing: {chamomile_flower}')
grow(chamomile_flower)
print(f'After growing: {chamomile_flower}')

print(f'Before growing: {rose_flower}')
grow(rose_flower)
print(f'After growing: {rose_flower}')

print(f'Before growing: {oak_tree}')
grow(oak_tree)
print(f'After growing: {oak_tree}')

print(f'Before growing: {apple_tree}')
grow(apple_tree)
print(f'After growing: {apple_tree}')
