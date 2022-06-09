# from typing_extensions import Self
# from unicodedata import name


class Account: 
       bank ="Equity"
       def __init__(self,name,deposit, withdraw):
         self.name = name
         self.deposit = deposit
         self.withdraw = withdraw
         
       def deposit(self):     
         return f"Dear {self.name} you have deposited amount{self.deposit}"
       def withdraw(self):
        return f"succesfully withraw amount of {self.withdraw}"  
      
      
