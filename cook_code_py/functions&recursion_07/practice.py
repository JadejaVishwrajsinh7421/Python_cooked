# wap to  print the len of list

cities = ['delhi','mumbai','noida','pune','morbi']

def print_len(list):
    print(len(list))
    
print_len(cities)

#wap to print the elements of  a list in a ingle line
def print_elements(list):
    for i in list:
        print(i,end=' ')#for same line

print_elements(cities)

#find factorial of n 
n=int(input("enter the element n for factorial"))

def my_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return(fact)

print(my_fact(n))
        
#convert usd to inr in function

usd = int(input("enter no of dollar to convert into inr"))

def inr_convertor(n):
    inr =n*95
    print(inr)

inr_convertor(usd)

#take a input odd even in function
 
no = int(input("enter number"))

def odd_even_str(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")
        
#recursion prog

# wap to find sum of  n nunmber using recursion

n = int(input("enter the value of n"))

def n_sum(a):
    if(a==0):
        return 0
    else:
        return a+n_sum(a-1)
    
print(n_sum(n))

# print all elements of list 

list1 = ['vbfb',"vsdu",'hjgr',"hhudsh"]

def print_list(list,idex=0):
    if (idex == len(list)):
        return 
    print(list[idex])
    print_list(list,idex+1)
    
print_list(list1)