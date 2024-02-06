import json

with open('departments.json') as file_content:
    json_object = json.load(file_content)

for department in json_object['departments']:
    if department['expenses'] < department['incomes']:
        for employee in department['employees']:
            employee['salary'] = round(employee['salary'] * 1.1, 2)

with open('new_costs.json', 'w') as new_file_content:
    json.dump(json_object, new_file_content)
