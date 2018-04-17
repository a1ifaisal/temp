class Employee:
    raise_amount = 1.04 #class variable (these are shared across instances i.e. across all Employees)
    
    #note self is current instance of class
    #note cls is shared among all instances
    
    def __init__(self, firstName, lastName, Ppay): #method
        self.first = firstName  #instance variable
        self.last = lastName
        self.pay = Ppay
        
    def fullname(self): #regular method
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        pass
    
    @classmethod    #alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod   #static method - generic to class
    def is_workday(day):
        print(day.weekday())
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
emp_1 = Employee('Phill', 'Ibrahim', 50) #instance of Employee class
print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)

#print(emp_1.raise_amount)

#static methods vs class methods vs regular methods

#Employee.set_raise_amount(2)
#print(emp_1.raise_amount)

emp_str_1 = 'Def-Jam-100'
#first, last, pay = emp_str_1.split('-')
#print(first)
#emp_2 = Employee(first, last, pay)
#print(help(emp_2))
emp_2 = Employee.from_string(emp_str_1)
print(emp_2.fullname())

import datetime
my_date = datetime.date(2018, 4, 7)
print(Employee.is_workday(my_date))
