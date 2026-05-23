# as due to fuctional programming we reducant your code  \
# and reuseabliity is in code 
# we move to toward prcedural to fuctional programming
# when we want real world situation to solve then it is time to objecvt oriented concepts in the prog
# in this we work with class,objects,constructors,methods,function,and many more
# class is is blueprint for creating  the objects

# class creating:
class Student:
    name = "karan" # same name for evry student
    
#objects creation: 
s1 = Student()
print(s1)
print(s1.name)

s2 = Student()
print(s2.name)

# # contructor in python is (__init__) function  excute during object creation
# # if we not write then also it will create  automatically 
# #first parameter is "self"  it will idcate refrence of new object(car1 to car)
# # it always first parameter then u can another paramter to it
# # not need to write self agru as "self" instead we can write "abc" what we need 
# # using self we can acesses the variable of the class
class Car:
    #default constructor
    def __init__(self):
        pass
    
    #parameterized constructor
    def __init__(self,model,year_manuf=25):
        print("add in new car in gearage.....")
        self.model = model # some attributes are not same ∴ we go throught this way
        self.manuf = year_manuf
    color ="blue"
    brand = "BMW"

car1 = Car("12xcv")
print(car1.manuf)
print(car1.model)
print(car1.brand)
print(car1.color)

car2 = Car("1245cv")
print(car2.model)
print(car2.brand)
print(car2.color)

car3 = Car("1278lv",24)
print(car3.manuf)
print(car3.model)
print(car3.brand)
print(car3.color)

#Attributes
#we have class level and  instance level attributes

#eg in class student  name is diffrent ∴ name is instance attribute but 
# if the divsion is same for all ∴ it is class level

#same name of class and obj attribute then always precedence class.attr > obj.attr  
class Student:
    college_name = "Darshan University" #class attribute
    
    def __init__(self,name,marks=35):
        print("add in new student.....")
        self.name = name 
        self.marks = marks
    
    
    
s1 = Student("vishwrajsinh",58)
print(s1.name,s1.marks,s1.college_name)
   
s2 = Student("arjun",78)
print(s2.name,s2.marks,s2.college_name)

# Methods 
# methods are the func that belong to objects

class Student:
    college_name = "Darshan University" #class attribute
    
    def __init__(self,name,marks=35):
        print("add in new student.....")
        self.name = name 
        self.marks = marks
    
    def hello(self): #we have to pass the self to invoke the class method to object level:
        print("hello",self.name)
    
    def getmarks(self):
        return self.marks
    
s1 = Student("vishwrajsinh",58)
print(s1.name,s1.marks,s1.college_name)
s1.hello()
   
s2 = Student("arjun",78)
print(s2.name,s2.marks,s2.college_name)
print(s2.getmarks())

#types of methods :

#1 static method 
# method in which we don't use self  parameter and work at class level 
# general used in utility work in class 

class student:
    @staticmethod #we used this decorator to make method static one
    def college():
        print("Darshan college")
      
student.college()  #by using class name insted of making object

#2 class methods 
# it is bound to class and recevies the class as an impact first agru

class Person:
    name= "anonyums"
    # def change_name(self,name):
        # self.name= name 

    @classmethod
    def change(cls,name):
        cls.name=name
    
p1 = Person()
p1.change("Pappu")
print(p1.name)
print(Person.name) 
# as it is behave diffrent for person and p1 therfore we use diffrent 

# 3.property dectorator/ methods
# we use this when any method in the class to use the method as attribute/property
class student:
    def __init__(self,math,phy,chem):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    # def cal_Percent(self):
    #     self.percent= str((self.phy+self.math+self.chem)/3)+"%"
    #     return self.percent
    
    @property
    def percentage (self):
        return str((self.phy+self.math+self.chem)/3)+"%"
    # it auto maatically change percentage if some student marks is change
    
stu1 = student(87,98,56)
print(stu1.cal_Percent())

stu1.phy =89
#to change marks we have to again calcu percent and then print to solve this we have property decorator
print(stu1.cal_Percent())

# in this we direct use varaible not use function
print(stu1.percentage)
stu1.chem =78
print(stu1.percentage)



#oops concepts:

# 1 abstracation 
# hiding the information details of a class and only 
# showing the essential feature to the users

class Car:
    def __init__(self):
        self.acc =False
        self.brk=False
        self.clutch = False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car is started..........")
        
car1 = Car()
car1.start() 
# here we only see the print message but actually 
# we not showing the values true and false this how the abstraction works

# 2 encapsulation 
# wrapping data and functions into a single unit(object)

# private,protected,public attributes and methods:

# private methods are meant to be used only within the clas 
# and are not accesible from outside  of the class
# in python not exactly same like as java or c++ oop concepts 
# as we easily access the private by using name managlaing 

class Acc:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass =acc_pass 
        # we can not show pass to other and 
        # not print outside the class we used "double __ to make variable or method private"
    
    def reset_pass(self):
        print(self.__acc_pass)
        # in class we use but noot outside the class
    
acc1 = Acc("1233455","#fjbjk")
acc1.reset_pass()


#del key word:
# it is used  to delete object prop or obj itself

# del s1.name
# del s1
class student:
    def __init__(self,name):
        self.name = name
    
s1 = student("vishubha")
del s1.name
# print(s1.name) it give exception
del s1 
# print(s1) it give exception

# 3 Inheritance 
# when one class derives the properties and methods of another class

# types of inhertiance 
# 1. single  #2.Multi level #3.Multiple

# eg 1
class Car:
    color ="Black"
    @staticmethod
    def start():
        print("Car is started...")
    
    @staticmethod    
    def stop():
        print("Car is stoped")

class ToyotaCar(Car):
    def __init__(self,name):
       self.name = name 

car1 = ToyotaCar("Glanza")
car2 = ToyotaCar("Innova")

print(car1.start())
#as we not write in start func in toyota but it is 
# dervied from super class "car"

#2
class Car:
    color ="Black"
    @staticmethod
    def start():
        print("Car is started...")
    
    @staticmethod    
    def stop():
        print("Car is stoped")

class ToyotaCar(Car):
    def __init__(self,brand):
       self.brand = brand  

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type
    
car1 =Fortuner("disel")
car1.start()


3
class A:
    varA="welcome to class A"
    
class B:
    varB ="welcome to class B"

class C(A,B):
    varC = "Welcome to class C"
    
c1 =C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

#Super Method
#Super() method is used to access the method of the parent class in the child class
class Car:
    color = "Black"

    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car is started...")

    @staticmethod
    def stop():
        print("Car is stopped")


class ToyotaCar(Car):
    def __init__(self, brand, type):

        # call Car constructor
        super().__init__(type)

        self.brand = brand


class Fortuner(ToyotaCar):
    def __init__(self, brand, type):

        # call ToyotaCar constructor
        super().__init__(brand, type)


car1 = Fortuner("Toyota", "Diesel")

print(car1.brand)
print(car1.type)

car1.start()

# 4 Polymorphism
# when same operator is allowed to have diffrent meaning
# according to the context

# eg operator and & dunder function
# operator overloading
print(1+2)
print("apna "+"college") 
print([1,2]+[3])

#for complex number 
class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img        

    def showNum(self):
        print(self.real,"i +",self.img,"j")
        
    def __add__(self,num2): #__ add__ act as dunder func where we cxan add direct 2 complex number        
        nreal = self.real +num2.real
        nimg = self.img + num2.img
        return complex(nreal,nimg)
    
    def __sub__(self,num2): 
        nreal = self.real -num2.real
        nimg = self.img - num2.img
        return complex(nreal,nimg)
    
        
        
num1 = complex(1,3)
num1.showNum()

num2  = complex(4,86)
num2.showNum()
 
num3 =num1.__add__(num2)
num3.showNum()

num4 = num1+num2
num4.showNum()

num5 = num1-num2
num5.showNum()

