marks1 = 78
marks2 = 45
marks3  = 95

# to make in simple combined marks  we use lists data structure
marks=[95,78,45,74,63,92]
print(marks)
print(type(marks)) # give type of ds
print(len(marks)) #return total element

#lists are diff from arrays in c and java 
# as lists have orderd , hetergeneos and mutuable data type have duplicate data

str1 =  "hello"
print(str1[0]) #acess the element but not change 
# str[1] = 'w' not possible 

# in list this possible
print(marks[0])
marks[0] = 52

#list slicing and indexing is possible same as string
print(marks[:4]) #end_ide is not include
print(marks[2:]) 
print(marks[2:4])