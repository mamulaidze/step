from faker import Faker
import random
import json

fake = Faker()

students = []

for i in range(1, 101):
    student = {
        "student_id": i,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "age": random.randint(18, 70),
        "is_active": random.choice([True, False])
    }

    students.append(student)

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

with open("students.json", "r") as file:
    students_data = json.load(file)

active_students = []

for student in students_data:
    if student["is_active"] == True:
        active_students.append(student)

with open("active_students.json", "w") as file:
    json.dump(active_students, file, indent=4)

print("ყველა სტუდენტი ჩაიწერა students.json ფაილში")
print("აქტიური სტუდენტები ჩაიწერა active_students.json ფაილში")