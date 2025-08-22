


class UserAccount:

    def __init__(self,username,balance,password,amount=100):
     self.username = username
     self._balance = balance
     self.__password = password
     self.amount = amount
     def deposit(amount):
         if amount >100:
             return self.amount + 10

     def withdraw(amount):
         if amount <=100:
             print(" Доступ разрешен")
             return self.amount - 50
         else:
             print("Доступ запрешен")


     def login(password):
         pass

     def get_balance():
         pass



