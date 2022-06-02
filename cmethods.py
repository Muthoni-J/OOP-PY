# Add these methods to class student - full_name, year_of_birth, initials. Create two instances and verify the work as expected
# Add these methods to class Account - deposit, withdraw. Create two instances of account and verify they work as expected.
from yaml import full_load


class Student:
    school ="Akirachix"
    
    def __init__(self,full_name,year_of_birth):
        self.full_name = full_name
        self.year_of_birth = year_of_birth
    #    self.full_name = full_name
    #    self.year_of_birth = year_of_birth
       
    def full_name(self):     
       return f"Hi {self.full_name}year_of_birth {self.full_name}"
    def year(self):
        age= 2022 - self.year_of_birth
        return f"you were born in {self.year_of_birth }"  
    def initials(self):   
     return f"Your name is {self.full_name} born {self.year_of_birth}" 
    def name(self): 
        x= self.full_name.split()
        return f"full{self.full_name}" 
#  Joan = Student(full_name = "Joan Muthoni",year_of_birth = 1998)   
# Joan.year_of_birth()
# from cmethods import Student

# class Account: 
    #    bank ="Equity"
#      def __init__(self,deposit, withdraw):
#          self.deposit = deposit
#          self.withdraw = withdraw