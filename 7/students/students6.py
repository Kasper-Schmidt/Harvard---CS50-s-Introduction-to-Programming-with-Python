import csv

students = []

with open("students3.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        #students.append({"name": row["name"], "home": row["home"]})
        students.append(row) # Det samme

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} comes from {student['home']}")




