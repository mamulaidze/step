from functools import reduce


# 1
numbers = [(1, 3), (4, 2), (2, 5)]

sorted_numbers = sorted(numbers, key=lambda x: x[1])
print(sorted_numbers)


# 2
def divide_numbers():
    try:
        num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
        num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

        result = num1 / num2
        return result

    except ValueError:
        print("აუცილებლად უნდა შეიყვანოთ მთელი რიცხვები!")

    except ZeroDivisionError:
        print("ნულზე გაყოფა არ შეიძლება!")


print(divide_numbers())


# 3
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]

cheap_products = list(filter(lambda product: product["price"] < 100, products))
print(cheap_products)

product_names_prices = list(map(lambda product: (product["name"], product["price"]), products))
print(product_names_prices)

sorted_products = sorted(products, key=lambda product: product["price"])
print(sorted_products)

total_price = reduce(lambda total, product: total + product["price"], products, 0)
print(total_price)


# 4
def sum_numbers(n):
    if n == 1:
        return 1

    return n + sum_numbers(n - 1)


print(sum_numbers(5))