#check odd and even:

num = int(input("Enter the num"))

if(num % 2 == 0):
    print("the num is even")
else:
    print("the num is odd")

#greatset of 3 number:

num1,num2,num3 = input("enter the 3 number").split(',')

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

max =0

if(num1 > num2):
    if(num1>num3):
        max = num1
    else:
        max= num2
else:
    if(num2>num3):
        max = num2
    else:
        max = num3
print("the maximum num is:",max)

#check the num is multiple of 7

num4 = int(input("enter the num to check multiple of 7 "))

if(num4 % 7 == 0):
    print("yes it is multiple of 7:",num4)
else:
     print("no it is not multiple of 7:",num4)
