# we for loop and while loop in the python

# used for repation work 
i =0
while i<5:  #this infinte condition if i>0
    print("hello")
    i+=1

#1 to 5 print

i =0
while i<=5:
    print(i)
    i+=1

print("loop ended")

# :: for loops ::
#for loops used in sequential traversal
li = [1,2,3,4,5]
for el in li:
    print(el)
    
tup1 = (23,34,56,67,45,63)
for el in tup1:
    print(el)
    
#in string character
str1 = "hello world"
for el in str1:
    print(el)

#we have for-else loop whenever we use break and continue statement
#then we use this type of loop:
str1 = "hello world"
for char in str1:
    if(char == 'o'):
        print("o is found")
        break
    print(char)
else:
    print("end")
    
#as we have break the loop then else part is not execute then we simple write print
#else part ma mostly ee code write kar vanu jema whole loop kaam thai pache use kare sakee

#Range functions returns a sequence of a number start with 0
#by default and increments(by 1) by default 

#range(start,stop,step)  ending number is not allowed 
print("range")
for i in range(2):
    print(i)
    
for i in range(1,5):
    print(i)
    
for i in range(1,10,2):
    print(i)
    
# Pass Statement:
# It is a null statement that does nothing. It is used as a 
#placeholder for future code:

#generalused in exception and handling of custom exceptions

for i in range(10):
    pass
  
print("hello")
