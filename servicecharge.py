class BankAccount:
    def __init__(self, name , account_number , balance ):
        self.name = name 
        self.__account_number = account_number
        self.__balance = balance
    def __service_charge(self):
        tax = (1/100)* self.__balance
        self.__balance = self.__balance - tax
        return self.__balance
    def deposit(self, amount: float):
        if(amount>0):
            self.__balance += amount
            self.__service_charge()
        return self.__balance
    def withdraw(self, amount):
        if(amount> 0 and amount <=self.__balance):
            self.__balance  -= amount
            self.__service_charge()
        return self.__balance

    @property
    def balance(self):
        return self.__balance
    
account = BankAccount("Randy Riches", "12345-6789", 1000)
account.withdraw(100)
print(account.balance)
account.deposit(100)
print(account.balance)
    