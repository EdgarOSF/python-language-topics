import random


def random_number():
    return random.randint(10000, 99999)

class BankAccount:
    def __init__(self, holder_name: str):
        self.id_number = random_number()
        self.holder_name = holder_name
        self.balance = 0

    def display_details(self):
        return (
                f"[{self.id_number}] "
                f"Holder Name: {self.holder_name}, "
                f"Balance: ${self.balance}")
    
    def deposit(self, mount: int):
        if mount < 0:
            print("The mount not be negative.")
        else:    
            self.balance += mount
            print(f"You deposit: ${mount}, your new balance is: ${self.balance}")

    def withdraw(self, mount: int):
        if mount > self.balance:
            print("You dont have enought founds")
        else:    
            self.balance -= mount
            print(f"You withdraw: ${mount}, you new balance is: ${self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, holder_name: str, minimun_balance: int):
        super().__init__(holder_name)
        self.minimun_balance = minimun_balance

    def withdraw(self, mount: int):
        if self.balance - mount < self.minimun_balance:
            print("Error, the withdraw cannot be less of the minimun balance")
        else:
            super().withdraw(mount)


# Create a account
count1 = SavingsAccount('Edgar Sanchez', 100)
count1.display_details()
count1.deposit(500)
count1.withdraw(100)
count1.withdraw(350)

print()

count2 = BankAccount('Carlos Espejel')
count2.display_details()
count2.deposit(300)
count2.withdraw(250)
count2.deposit(-10)

print()

count3 = BankAccount('Eduardo Camarena')
count3.display_details()
count3.deposit(670)
count3.withdraw(340)

print()




