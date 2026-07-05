import math

# 1. მართკუთხა სამკუთხედის ჰიპოთენუზა და ფართობი

cathetus1 = int(input("შეიყვანეთ პირველი კათეტი: "))
cathetus2 = int(input("შეიყვანეთ მეორე კათეტი: "))

hypotenuse = math.sqrt(cathetus1 ** 2 + cathetus2 ** 2)
area = (cathetus1 * cathetus2) / 2

print("ჰიპოთენუზა არის:", hypotenuse)
print("ფართობი არის:", area)

print("------------------------")

# 2. წამების გადაყვანა საათებში, წუთებში და წამებში

seconds = int(input("შეიყვანეთ წამების რაოდენობა: "))

hours = seconds // 3600
seconds = seconds % 3600

minutes = seconds // 60
seconds = seconds % 60

print("საათი:", hours)
print("წუთი:", minutes)
print("წამი:", seconds)