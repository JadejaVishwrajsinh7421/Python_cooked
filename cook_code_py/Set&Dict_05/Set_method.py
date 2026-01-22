# set methods

#imp--
#set is mutuable but their elemnts are immutable direct change 
# of element not occur and also unorederd nature of set ,we can't use index->>,
# we go through the methods 

collections = set()

collections = {"hello", " world", " of ","python"}

collections.add(1)
collections.add(2)
collections.add(2)#not enter in the set
collections.add((1,2,3))
print(collections)

# collections.remove(5)#gives error if not found

print(collections.discard(5)) #doesn't give error return None

a = collections.pop()#return the element which removed
print (a)
print(collections)

collections.update("computer")#pass any iterable object
print(collections)

info = {'hi','guyss'}

info = collections.copy()
print(info)#info is changed to same as collections

# ---------maths concept of set------#

set1 = {1,2,3,4}
set2 = {1,3,6,5}

# 1. union (combine both set)
set3 = set1.union(set2)
print(set3)

# 2.set1 - set2 elements
set3 = set1.difference(set2)
set4 = set2.difference(set1)
print(set3)
print(set4)

#3. A B common
set3 = set1.intersection(set2)
print(set3)

#set diff_update
a = {1,2,3,4}
b = {1,3,6,5}
set4 = a.difference(b)
print(set4)

#🔹 Updating Sets (In-place) no new set is creted all logic is applied in set a
a.update(b)#a = a union B
print(a)

a.intersection_update(b)# a = a intersect b
print(a)

a.difference_update(b)#a = a-b
print(a)

a.symmetric_difference_update(b)#a = (a union b) - (a insetect b)
print(a)


#general reationship b/w 2 sets

#---They DO NOT change the set — they only return True or False.

# 1

a={1,2}
b={1,2,3,4}

print(a.issubset(b))

#2

a = {1, 2, 3, 4}
b = {2, 3}
print(a.issuperset(b))

a = {1, 2}
b = {1, 2, 3}

print(a.issuperset(b))

# 3
a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))

a = {1, 2}
b = {1, 2, 3}

a = {1, 2}
b = {2, 3}

print(a.isdisjoint(b)) 