#  as in docx said that string is immutable

username = 'vishwraj'
print (username)

username  = 'chai aur code'
print (username)

# same for integer
x = 10
y = x
print(x,y)
x= 15
print(x,y) #here x is changed but y is not


''' Inner working 
as python as advaced garbage collector as that changed the refernce of object when we changed the
 value inside sys there is no change in the value of 'vishwraj' it just change refe. to 'chai aur code' 

same happen in the case of integer

where x ref. to 10 and when y=x that directly mean that y is refe. to object '10' to x and then the
x=15 y's ref. is not changed'''