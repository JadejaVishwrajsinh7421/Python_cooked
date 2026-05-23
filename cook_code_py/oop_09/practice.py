# 1 create student class that takes name,marks of 3 subject
# in construictor argu theen create a method to print the message

class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
        
    def avg_marks(self):
        avg =(self.marks3+self.marks2+self.marks1)/3
        print("the avg is:",avg)
        
s1 = Student("vishwraj",98,99,87)
s1.name= "vdhg"
print(s1.name)
s1.avg_marks()
        
# 2 create accoiunt class with balance and  
# account no.create methods for debit,credit and print the balance

class Account:
    def __init__(self,balance,accno):
        self.balance=balance
        self.accno=accno
    def get_balance(self):
        return self.balance
        
    def debit(self,amount):
        self.balance -= amount
        print("Amount debitted is",amount)
        print("Total Amount is:",self.get_balance())
    def credit(self,amount):
        self.balance +=amount
        print("Amount credited is ",amount)    
        print("Total Amount is:",self.get_balance())

        
acc1 = Account(10000.1,124560)
acc1.debit(1000.1)
acc1.credit(250.1)

#q3 --59.01 min-- que
import math 

class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def areaOfCircle(self):
        return (self.radius**2)*(math.pi)
         
    def perimeterOfCircle(self):
        return math.pi*2*self.radius
    
c1 = Circle(4)
print(c1.areaOfCircle())
print(c1.perimeterOfCircle())

#q4 

class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print("role is",self.role,"and working in the department",self.dept,"with salary",self.salary)  
 
class Enginner(Employee):
    def __init__(self,name,age):
        super().__init__("Enginner", "IT", 7500000)
        self.name = name
        self.age = age
        
        
e1= Employee("Accountant","Finance","1250000")
e1.showDetails()

e2 = Enginner("Vishwrajsinh","21")
e2.showDetails()

#q5
class Order:
    def __init__(self,item,price):
        self.price = price
        self.item =item
    
    def __gt__(self,o2):
        if (self.price > o2.price):
            return True
        else:
            return False
    
o1 =Order("Chips",20)
o2 = Order("tea",10)

print(o1>o2) #dunder paaji zindabad :-):-)
print(o2>o1)


             