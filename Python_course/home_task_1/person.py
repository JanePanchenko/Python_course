
class Person():
    def __init__(self, salary: float, age: int, name: str, gender: bool, friends: list):
        self.salary = salary
        self.age = age
        self.name = name
        self.gender = gender
        self.friends = friends

    def __str__(self):
        return ("Salary: " + str(self.salary) + " "
                + "\nAge: " + str(self.age) + " "
                + "\nName: " + self.name + " "
                + "\nGender: " + str(self.gender) + " "
                + "\nFriends: " + str(self.friends)) + "\n"
