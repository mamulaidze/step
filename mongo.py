from pymongo import MongoClient
import random

client = MongoClient("mongodb://localhost:27017/")

db = client["shop"]
products = db["products"]

products.delete_many({})

categories = ["Electronics", "Books", "Clothes"]

product_list = []

for i in range(1, 51):
    quantity = random.randint(0, 100)

    product = {
        "name": "Product " + str(i),
        "category": random.choice(categories),
        "price": random.randint(50, 3000),
        "quantity": quantity,
        "available": quantity != 0
    }

    product_list.append(product)

products.insert_many(product_list)

print("ყველა პროდუქტი:")
for product in products.find():
    print(product)

print("\nხელმისაწვდომი პროდუქტები:")
for product in products.find({"available": True}):
    print(product)

print("\nპროდუქტები, რომლის ფასი მეტია 1000-ზე:")
for product in products.find({"price": {"$gt": 1000}}):
    print(product)

print("\nპროდუქტების რაოდენობა კატეგორიების მიხედვით:")
for category in categories:
    count = products.count_documents({"category": category})
    print(category, "-", count)

print("\nერთ-ერთი პროდუქტის რაოდენობის შეცვლა:")

products.update_one(
    {"name": "Product 1"},
    {"$set": {"quantity": 25, "available": True}}
)

updated_product = products.find_one({"name": "Product 1"})
print(updated_product)

client.close()