class BankAccount:
    bank_name = "TBC Bank"
    __total_accounts = 0

    def __init__(self, owner, balance):
        self._owner = owner

        if BankAccount.validate_amount(balance):
            self.__balance = balance
        else:
            self.__balance = 0

        BankAccount.__total_accounts += 1
        self.__account_number = f"AN{BankAccount.__total_accounts:04d}"

    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.__balance += amount
        else:
            print("არასწორი თანხა")

    def withdraw(self, amount):
        if not BankAccount.validate_amount(amount):
            print("არასწორი თანხა")
        elif amount > self.__balance:
            print("ანგარიშზე საკმარისი თანხა არ არის")
        else:
            self.__balance -= amount

    def check_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def change_owner(self, new_owner):
        self._owner = new_owner

    @classmethod
    def get_total_accounts(cls):
        return cls.__total_accounts

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    def __str__(self):
        return f"Account: {self.__account_number} | Owner: {self._owner}"


account1 = BankAccount("Giorgi Mamulaidze", 1000)
account2 = BankAccount("Nino Beridze", 2000)

print(account1)
print(account2)

account1.deposit(500)
account1.withdraw(300)

print(account1.check_balance())
print(account1.get_account_number())
print(BankAccount.get_total_accounts())