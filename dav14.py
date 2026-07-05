# 1. BMI კალკულატორი

weight = float(input("შეიყვანეთ წონა კგ-ში: "))
height = float(input("შეიყვანეთ სიმაღლე მეტრებში: "))

bmi = weight / (height ** 2)

print("BMI არის:", bmi)

if bmi < 19:
    print("Underweight")
elif bmi >= 19 and bmi <= 25:
    print("Normalweight")
else:
    print("Overweight")


print("------------------------")


# 2. კალკულატორი

num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

operator = input("შეიყვანეთ ოპერატორი (+, -, *, /): ")

if operator == "+":
    print("შედეგი:", num1 + num2)
elif operator == "-":
    print("შედეგი:", num1 - num2)
elif operator == "*":
    print("შედეგი:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("შედეგი:", num1 / num2)
    else:
        print("ნულზე გაყოფა არ შეიძლება")
else:
    print("არასწორი ოპერატორი")


print("------------------------")


# 3. სამი რიცხვიდან ყველაზე დიდის პოვნა

number1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
number2 = int(input("შეიყვანეთ მეორე რიცხვი: "))
number3 = int(input("შეიყვანეთ მესამე რიცხვი: "))

if number1 == number2 or number1 == number3 or number2 == number3:
    print("შეიყვანეთ განსხვავებული რიცხვები")
else:
    if number1 > number2 and number1 > number3:
        print("ყველაზე დიდი რიცხვია:", number1)
    elif number2 > number1 and number2 > number3:
        print("ყველაზე დიდი რიცხვია:", number2)
    else:
        print("ყველაზე დიდი რიცხვია:", number3)