class Employee:
    def __init__(self, name, salary):
        self.name = name

        if salary < 0:
            self.salary = 0
        else:
            self.salary = salary

    def show_info(self):
        print(f"სახელი: {self.name}")
        print(f"ხელფასი: {self.salary}")

    def work(self):
        print("თანამშრომელი მუშაობს")

    def raise_salary(self, amount):
        self.salary += amount


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)

        self.programming_language = programming_language

    def code(self):
        print("კოდის წერა მიმდინარეობს")

    def work(self):
        print("დეველოპერი კოდს წერს")


class Designer(Employee):
    def __init__(self, name, salary, design_tool):
        super().__init__(name, salary)

        self.design_tool = design_tool

    def create_design(self):
        print("დიზაინის შექმნა მიმდინარეობს")

    def work(self):
        print("დიზაინერი დიზაინს ქმნის")


dev1 = Developer(
    "გიორგი",
    5000,
    "Python"
)

designer1 = Designer(
    "ნინო",
    4000,
    "Figma"
)


dev1.show_info()
dev1.work()
dev1.code()

