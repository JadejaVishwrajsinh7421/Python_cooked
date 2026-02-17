#print 1 to 100
i=1
while i<=100:
    print(i)
    i+=1
    
for i in range(1,101):
    print(i)
    
#100 to 1
i=100
while i>=1:
    print(i)
    i-=1
    
for i in range(100,0,-1):
    print(i)
    
#print multiplication of  n table 
i =0 

n = int(input("enter a number"))
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1

for  i in  range(1,11):
    print(n,"*",i,"=",n*i)
#print  list with square of num upto 100

i=0
index =0
li=[]
while i<=10:    
    li.append(i*i)
    i+=1
   
while index <len(li):
    print(li[index]) 
    index+=1

#search a number in the list given by user
i=0
a= int(input("enter a num to search in the list"))
b =tuple(li)

while i <= len(b):
    if(a == b[i]):
        print(b[i])
        break
    else:
        print("Not found")
    i+=1
    
#using for print the elements of the list:

li1 = [1,2,3,4,5,6,7,8,9,10]
for i in li1:
    print(i)
    
##search a number in the list given by user by li
nums = (1,4,9,16,25,36,49,64,81,100,49)
x = int(input("enter a num"))

for i in range(0,len(nums)):
    if(x == nums[i]):
        print("index is:",i)
        break
  
#wap to find the sum of first n number

n = int(input("enter a num"))
i,sum=1,0

while i !=n:
    sum +=i
    i+=1
print("sum is:",sum)

#factorial of first n number
num = int(input("enter a num for factorial"))
fact=1
for i in range(1,num+1):
    fact *=i
print("fact is:",fact)