import csv

students = []

with open("students2.csv") as file:
    reader = csv.reader(file)
    for name, house, home in reader:
        students.append({"name": name, "house": house, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}, and comes from {student['home']}")




