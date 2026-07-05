import csv


def create_users_csv(count):
    users = []

    for i in range(1, count + 1):
        first_name = input("შეიყვანეთ სახელი: ")
        last_name = input("შეიყვანეთ გვარი: ")

        while True:
            try:
                age = int(input("შეიყვანეთ ასაკი: "))
                break
            except ValueError:
                print("ასაკი უნდა იყოს მთელი რიცხვი!")

        user = {
            "ID": i,
            "first_name": first_name,
            "last_name": last_name,
            "age": age
        }

        users.append(user)

    with open("users.csv", "w", newline="") as file:
        fieldnames = ["ID", "first_name", "last_name", "age"]

        csv_writer = csv.writer(file)
        csv_writer.writerow(fieldnames)

        dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
        dict_writer.writerows(users)


def filter_students():
    failed_students = []
    passed_students = []

    with open("students.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for student in reader:
            grade = int(student["Grade"])

            if grade < 50:
                failed_students.append(student)
            elif grade > 50:
                passed_students.append(student)

    with open("failed_students.csv", "w", newline="") as file:
        fieldnames = failed_students[0].keys() if failed_students else ["Name", "Grade"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(failed_students)

    with open("passed_students.csv", "w", newline="") as file:
        fieldnames = passed_students[0].keys() if passed_students else ["Name", "Grade"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(passed_students)


create_users_csv(3)
filter_students()