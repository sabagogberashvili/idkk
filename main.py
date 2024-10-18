from datetime import date

class Customer:
    def __init__(self, name, date_of_birth, balance):
        self.name = name
        self.date_of_birth = date_of_birth
        self.balance = balance

    @property
    def age(self):
        return date.today().year - self.date_of_birth.year

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    @property
    def budget(self):
        return sum(customer.balance for customer in self.customers)

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, customer):
        self.customers.remove(customer)

    def can_get_loan(self, customer, amount):
        return customer.balance >= amount / 2


customer1 = Customer("John Doe", date(1990, 5, 23), 1000)

print(f"Initial balance: {customer1.balance}")

customer1.deposit(500)
print(f"Balance after deposit: {customer1.balance}")

customer1.withdraw(200)
print(f"Balance after withdrawal: {customer1.balance}")

bank = Bank("MyBank")
bank.add_customer(customer1)

loan_amount = 1000
is_eligible = bank.can_get_loan(customer1, loan_amount)
print(f"Is customer eligible for a loan of {loan_amount}? {is_eligible}")