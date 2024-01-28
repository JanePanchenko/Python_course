from Python_course.HomeTask1.person import Person

john_salary = 100.55
john_age = 30
john_name = "John Smith"
john_gender = False
jonn_friends = ["Pol", "Fil", "Jack"]


marta_salary = 111.99
marta_age = 32
marta_name = "Marta Lonth"
marta_gender = True
marta_friends = ["Miki", "lyi", "Pil"]


john: Person = Person(john_salary, john_age, john_name, john_gender, jonn_friends)
print(john)

marta: Person = Person(marta_salary, marta_age, marta_name, marta_gender, marta_friends)
print(marta)


people_name = ['Pol', 'Marta', 'Pol', 'Lyi', 'Miki', 'Lyi', 'Miki', 'Lyi']
print(people_name)
print(set(people_name))
