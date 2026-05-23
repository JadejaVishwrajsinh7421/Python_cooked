#functions --> block of code that performs a specicifc task

# To make the code ease of reducant code  we use function 

#def keyword is used

#def func_name(param1,...)
#   code...
#   return val


def sum(a,b):
    # we can return the output or print them in a function 
    return a+b

print(sum(2,5))

#func is used to reducant the code

#3 number average

def avg(n1,n2,n3):
    return((n1+n2+n3)/3)

print(avg(1,3,4))

#Recursion
# -> when a func calls itself repeatedly

def back_num(n):
    if(n==0): #base case to stop the recusrion
        return
    print(n)
    
    back_num(n-1)# iterate the value
    
    
back_num(9)

def rec_fact(n):
    if(n==0 or n ==1):
        print('end')
        return 1
    else:
        print('end')
        return n*rec_fact(n-1)
print(rec_fact(4))
