def gadaxda(func):
    def wrapper(balansi,gadasaxdeli):
        gadasaxdeli_sakomosioti = gadasaxdeli +1

        return func(balansi,gadasaxdeli_sakomosioti)
    return wrapper

@gadaxda
def  tranzaqcia (balance,amount):
    if balance-amount<0:
        return f"არასაკმარისი თანხა, თქვენი ბალანსია {balance}₾"
    else:
        return balance - amount
    

print(tranzaqcia(100, 20))
print(tranzaqcia(10, 15))