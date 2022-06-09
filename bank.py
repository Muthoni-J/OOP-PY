class Account:
    def __init__(self, name, acc_number):
        self.balance = 0
        self.name = name
        self.acc_number = acc_number 
                 
    def deposit(self,amount):
        self.balance+= amount 
        return f"You've  deposited this amount {amount} this is your balance {self.balance}"


    def deposit(self,deposit):
        self.balance+= deposit
        if deposit <=0:
            return f"Deposit amount shoul be more than zero"
        else:
            self.balance+= deposit
            return f"You have deposited{deposit}.Your new balance is {self.balance}"
        
    def withdraw(self,amount):
        if amount > self.balance:
            return f"Your balance {self.balance} you cannot withraw{amount}"
        elif amount < 0:
            return f"Amount must be greater else:than zero"
        else:
            self.balance -= amount
            return f"You have withdraw {amount} your balance is {self.balance}"