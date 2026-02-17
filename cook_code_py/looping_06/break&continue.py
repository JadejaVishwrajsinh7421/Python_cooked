# break is used for to break the statement at particular point .
#used generally in the loops

#where as continue  uesd to skip a particular iteration
i =1
while i<=5:
    print(i)
    if(i == 3):
        break
    i+=1
 

i =1
while i<=10:
    if(i%2 == 0):
        i +=1
        continue
    print(i) 
    i+=1  
    
