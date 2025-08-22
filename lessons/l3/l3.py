


import random

class BankAccount:

    def __init__(self, customer, balance, password):
        self.customer = customer
        self._balance = balance
        self.__password = password

    def __random_password(self):
        return random.randint(1, 6 )

    def login(self, password):
        if self.__password == password:
            print('Вы вошли!!')
        else:
            print("не верный пароль!!!")

    def get_random_password(self):
        return self.__random_password()

account1 = BankAccount("John Doe", 1000, 12345)

print(dir(account1))

print(account1._BankAccount__random_password())
    # def get_balance(self):
    #     return print(self._balance)
    #
    # def get_random_password(self):
    #     return self.__random_password()