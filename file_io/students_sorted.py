students = []

with open('students.csv') as file:
    for line in file:
        name, house = line.rstrip().split(',')
        student = {'name': name, 'house': house}
        students.append(student)

def get_house(student):
    return student['house']

# version 1 ordernado por casa
# for student in sorted(students, key=get_house):
#     print(f"{student['name']} is in {student['house']}")

# version 2 ordernado por nombre
# for student in sorted(students, key=lambda student: student['name']):
#     print(f"{student['name']} is in {student['house']}")