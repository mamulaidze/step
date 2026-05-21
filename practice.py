class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"

p1 = Person("Otar", 34)
print(p1)

def serializer(person):
    return f"name: {person.name}, age: {person.age}"

ser_data = serializer(p1)
print(ser_data)

with open("person.txt", "w") as file:
    file.write(ser_data)

with open("person.txt", "r") as file:
    data = file.read()
    print(data)


def deser(data):
    davita = data.split(", ")
    name = davita[0].split(": ")[1]
    age = int(davita[1].split(": ")[1])
    return Person(name, age)
deser1 = deser(data)
print("Deserialized person:", deser1)