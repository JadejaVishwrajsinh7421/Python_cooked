# wap to ask 3 user to enter name of their 3 fav movie ans store them in the list

# list1 = []

# print("enter 3 movies in the list")
# mov1 = input("enter 1st ")
# mov2 = input("enter 2nd ")
# mov3 = input("enter 3ed ")

# list1.append(mov1)
# list1.append(mov2)
# list1.append(mov3)

# print(list1)


# # m-2
# list2 =[]
# list2.append( input("enter 1st "))
# list2.append( input("enter 2st "))
# list2.append( input("enter 3st "))

# # wap to check if a list contains a palindrome of elements

# li1= list(map(str ,input().split()))
# li2 = li1.copy()
# li2.reverse()
# print(li2)
# if (li2 ==li1):
#     print("palindrome list ")   
# else:
#     print("not palindrome list")
    
#wap to count the students with grade "A"
tup1 = ('c' ,'d','a','a','b','f','a','a','c','d')

print('no of a grades in the class',tup1.count('a') )

#store the above values in a list and sort them from 'a' to 'd'

li =  list(tup1)
li.sort()
print(li)