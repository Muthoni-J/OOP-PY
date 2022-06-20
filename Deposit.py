# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which prints each deposit in a new line
# Add a new method called withdrawals_statement which prints each withdrawal in a new line
# Modify the withdrawal method to include a transaction fee of 100 per transaction.
# Add a method to show the current balance
# Update the withdrawal method to store each withdrawal transaction as a dictionary like like this 
# {
#    "date": datetime object,
#    "amount": amount,
#    "narration": deposit or withdrawal
# }

# Update the deposit method to store each deposit transaction as a dictionary like this 
# {
#    "date": datetime object,
#    "amount": amount,
#    "narration": deposit or withdrawal
# }

# Add a new method  full_statement which combines both deposits and withdrawals into one list ordered by date and using a for loop prints each transaction in a new line like this
# 16/06/22 —----- Deposit —---- 1000

# Add a new attribute loan_balance which is zero by default.

# Add a borrow method which allows a customer to borrow if they meet these conditions:
# Customer has made at least 10 deposits.
# Loan amount requested must be more than 100
# A customer qualifies for a loan amount that is less than  or equal to 1/3 of their total sum of deposit history
# Customer account has no has no balance
# Customer has no outstanding loan
# The loan attracts  an interest of 3%.

# Add a loan repayment method with these conditions
# A customer can repay a loan to reduce the current loan balance
# Overpayment of a loan increases a customers current deposit

# Add a new method transfer which accepts two attributes (amount and instance of another account). If the amount is less than the current instances balance, the method transfers the requested amount from the current account to the passed account. The transfer is accomplished by reducing the current account balance and depositing the requested amount to the passed account.



from datetime import datetime
from time import strftime, time


class Account:
    def __init__(self, acc_name, acc_number):
        self.acc_name = acc_name
        self.acc_number = acc_number
        self.balance=0
        self.transaction = 100
        self.deposits=[]
        self.withdraws=[]
        self.statement=[]
        self.time=datetime.now().strftime("%X")
        self.loan_balance=0
        
       
 
    def deposit(self,amount):
        if amount <=0:
            return f" Deposit amount should be more than zero"
        else:
        
            self.balance += amount
            transaction={
            "amount":amount,
            "time":self.time,
            "Narration":"you have withdraw"
            }
            self.statement.append(transaction) 
            self.deposits.append(amount)
        return f"You've  deposited this amount {amount} this is your balance {self.balance}"


    def withdraw(self,amount):
        if amount > self.balance:
            return f"Your balance {self.balance} you cannot withraw{amount}"
        elif amount < 0:
            return f"Amount must be greater else:than zero"
        else:
            self.balance -= amount + self.transaction
            transaction={
            "amount":amount,
            "time":self.time,
            "Narration":"you have withdraw"
            }
            self.statement.append(transaction)
            self.withdraws.append(amount)
            return f"You have withdraw {amount} your balance is {self.balance}"
        
    def deposits_statement(self):  
      for n in self.deposits:
        print(f"Your deposits{n}")
    
    def widthdals_statement(self):     
       for n in self.withdraws:
        print(f"Your Widthdrawals{n}")
     
    def current_balance(self):
        balance = self.balance
        return(f"You current balance is{balance}")            
    def complete_statement(self):
      for transaction in self.statement:  
          amount = transaction["amount"]
          narration =transaction["narration"]
          time = transaction["time.date"]
          print(f"{time}: {narration} {amount}")
          
    def borrow (self,amount):
 
       count = sum (self.deposits)
       limit = count
       interest = amount*0.03
       if amount<=100:
           return "Loan must be more than 100"
       elif self.loan_balance>0:
           return "Loan denied, kindly repay your current loan of {self.loan}"
       elif len(self.deposits)<10:
           return f"you deposits must be at least more than 10"
       elif amount>=limit:
           return f"You have reached your limit, your loan of {amount}Kshs is denied"
       elif amount>=self.balance:
           return f"Dear customer you can't borrow that money is lower than a limit of"
       else:
           self.loan_balance>=amount
           self.loan_balance+=interest
           transaction= {
               "date": self.time,
               "amount": amount,
               "narration": "You have withdrawn"
               }
           self.statement.append(transaction)
           self.withdraws.append(amount)
           return f"Hello {self.name} your loan of {amount} has been approved and your interest is {interest} you will pay back {self.loan_balance}"
 
    def repay(self,amount):
       if amount<8:
           return f"Dear customer your payment is too low"
       elif amount<=self.loan_balance:
           paid= self.loan_balance - amount
           return f"Dear customer you have paid {amount} and your loan balance is {paid}"
       else:
           payment = amount - self.loan_balance
           self.balance+=payment
           transaction= {
               "date": self.time,
               "amount": amount,
               "narration": "You have withdrawn"
               }
           self.statement.append(transaction)
           return f"Dear customer {self.acc_name} you have fully paid your loan and the overpay of {payment} is added on your account, your new balance is {self.balance}"
       
    def transfer(self, account_instance,amount):
       total = amount + self.withdraws
       if amount<0:
           return f"Dear customer {self.acc_name} your amount is too low"
       elif total>self.balance:
           return f"Your balance is {self.balance} and you need atleast {total}"
       else:
           self.balance-=total
           return f"you have sent {amount} to {account_instance} your current balance is {self.balance}"
 

  
  