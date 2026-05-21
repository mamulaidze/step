class Student:
    status = True
    pay= 1000
    def __init__(self,first_name,last_name,age,grades):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = grades
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    def discount(self):
        if self.age <18:
            return self.pay*0.8
        return self.pay
    def calculate_avg(self):
        return sum(self.grades)/len(self.grades)
    def is_passing(self):
        if self.calculate_avg() > 90:
         return f"{self.get_full_name()}. ქულა:{self.calculate_avg()} exelent"
    
        elif self.calculate_avg() <90 and self.calculate_avg() > 70:
            return f"good"
        elif self.calculate_avg() < 70:
            self.status = False
            return "oh no"
    
        
student1 = Student(
    "Giorgi",
    "Mamulaidze",
    17,
    [95, 90, 100, 92]
)

print(student1.calculate_avg())
print(student1.is_passing())
print(student1.status)