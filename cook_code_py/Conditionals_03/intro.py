# age = 21

# if(age>=18):
#     print("you can vote if u can have voting card")
    
#eg-2

light  = "red"

if(light == 'red'):
    print("stop")
elif(light == 'yellow'):
    print("wait")
else:
    print("Go")
    
#eg-3
num = 5
if(num > 2):
    print("the num is greater than 2")
    
if(num >3):
    print("the num is greater than 3")
    
##########diff in if and if block and if-elif block

if(num>2):
    print("the num is greater than 2")
    
elif(num >3):
    print("the num is greater than 3")

## output is:
# the num is greater than 2
# the num is greater than 3
# the num is greater than 2n 

marks =  int(input("enter the marks:"))

if marks >= 90:
    grade = 'A'
elif marks >=80 and marks <90:
    grade = 'B'
elif marks >=70 and marks < 80:
    grade ='C'
else:
    grade ='D'

print("the grade is:",grade)