#lists Methods 

list1 = [2,1,34,56,34]

list1.append(48) #add in las
print(list1)

list2 =list1.reverse() #return none but have yo store another list
print(list1)
print (list2)#none

list1.sort() #ascending
print(list1)

list1.sort(reverse= True)#desc
print(list1)

list1.insert(2,454) #insert at specific index 
print(list1)

list1.remove(1)#remove element
print(list1)

list1.pop(0) # removes at elements at index and return it
print(list1)

a= list1.count(34)#count ocuurence of element
print(a)

# b =list1.index(44)
# print(b) #not in the list give error

a =list1.index(48)
print(a) #returns index of the element

list3 = ['vishwrajsinh','jadeja']
list1.extend(list3)#we can pass iterable object 
print(list1)#updated in list1

#if we add add to lists by '+' it will genrated in new lists

list1.clear()
print(list1)#returns => []

# almost all mthods are cover 