import random

secret_number = random.randint(1, 100)
lives = 5

print("Guessing Game")
print("გამოიცანი რიცხვი 1-დან 100-მდე")
print("შენ გაქვს 5 სიცოცხლე")

while lives > 0:
    try:
        guess = int(input("შეიყვანე რიცხვი: "))
    except ValueError:
        print("გთხოვ შეიყვანე მხოლოდ რიცხვი!")
        continue

    if guess == secret_number:
        print("გილოცავ, შენ მოიგე!")
        break

    elif guess < secret_number:
        print("ჩაფიქრებული რიცხვი მეტია")

    else:
        print("ჩაფიქრებული რიცხვი ნაკლებია")

    lives -= 1
    print("დარჩენილი სიცოცხლე:", lives)

if lives == 0:
    print("შენ წააგე!")
    print("ჩაფიქრებული რიცხვი იყო:", secret_number)