import csv
import random
from faker import Faker

fake = Faker()

persons = []

for i in range(1, 51):
    person = {
        "ID": i,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "age": random.randint(20, 80)
    }

    persons.append(person)

with open("persons.csv", "w", newline="") as file:
    fieldnames = ["ID", "first_name", "last_name", "age"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(persons)

print("persons.csv ფაილი წარმატებით შეიქმნა")