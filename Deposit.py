# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which prints each deposit in a new line
# Add a new method called withdrawals_statement which prints each withdrawal in a new line
# Modify the withdrawal method to include a transaction fee of 100 per transaction.
# Add a method to show the current balance


class Account:
    def __init__(self, acc_name, acc_number):
        self.acc_name = acc_name
        self.acc_number = acc_number
        self.balance=0
        self.transaction = 100
        self.deposits=[]
        self.withdraws=[]
       
 
    def deposit(self,amount):
        if amount <=0:
            return f" Deposit amount should be more than zero"
        else:
        
            self.balance += amount 
            self.deposits.append(amount)
        return f"You've  deposited this amount {amount} this is your balance {self.balance}"


    def withdraw(self,amount):
        if amount > self.balance:
            return f"Your balance {self.balance} you cannot withraw{amount}"
        elif amount < 0:
            return f"Amount must be greater else:than zero"
        else:
            self.balance -= amount + self.transaction
            self.withdraws.append(amount)
            return f"You have withdraw {amount} your balance is {self.balance}"
        
    def deposits_statement(self):
        print(*self.deposits, sep="\n")
    def withdraws_statement(self):
        print(*self.withdraws, sep="\n")
    def current_balance(self):
        balance = self.balance
        print(balance)
        
        

            
        

  