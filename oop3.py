# bank account == owner, account number, balance, history of the account
from datetime import date, datetime


class Client:
    def __init__(self, names, Kra_pin, dob, gender):
        self.names = names
        self.Kra_pin = Kra_pin
        self.dob = dob
        self.gender = gender

    def print_details(self):
        print(self.names)
        print(self.Kra_pin)
        print(self.dob)
        print(self.gender)

    def calc_age(self):
        today = date.today()
        birth_date = datetime.strptime(self.dob, '%d-%m-%Y')
        age = today.year - birth_date.year
        return age

class BankAccount:
    def __init__(self, owner, acc_no:str, balance:int):
        self.owner = owner
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += abs(amount)  # abs ensures it's a positive amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= abs(amount)

    def print_details(self):
        print(self.owner.names)
        print(self.acc_no)
        print(self.balance)
        print("-------------------")

Jane = Client('Jane Mwangi', 'A001', '16-01-1999', 'F')
Ahmed = Client('Ahmed Somow', 'A002', '20-03-1995', 'M')

acc1 = BankAccount(Jane,"2225587", 70_000)
acc2 = BankAccount(Jane,"2225587", 80_000)
acc3 = BankAccount(Ahmed,"3335687", 900_000)

acc1.deposit(10_000)
acc1.deposit(3_000)

acc1.print_details()
acc1.withdraw(15_000)
acc1.print_details()

print("Janes Age", Jane.calc_age())
print("Ahmed's Age", Ahmed.calc_age()),


# dob = '18-01-2004'  # d.m.y   d.m.Y
# today = date.today()
# print(f"{today.day}-{today.month}-{today.year}")
# convert string to date
# birth_date = datetime.strptime(dob, '%d-%m-%Y')
# age = today.year - birth_date.year
# print(age)


