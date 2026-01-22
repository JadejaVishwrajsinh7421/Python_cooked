#Intro tuples

#same as working as of lists but they are immutable 

tup = (87,65,3345,456)
print(tup)
print(type(tup))

#allows indexing acess 
print(tup[0])

#but we can't change 
# tup[0] = 23 throws exception

#create ways

#1 empty tuple
tup = ()
print(tup)
print(type(tup))

#2.single element
tup = (1,)
print(tup)
print(type(tup))
 ### tup(1) not alowed to form tuple
 
#3. by func
tup1 = tuple()
print(tup1)
print(type(tup1))
#4. by range()
tup2 =  tuple(range(1,7))
print(tup2)
print(type(tup2))