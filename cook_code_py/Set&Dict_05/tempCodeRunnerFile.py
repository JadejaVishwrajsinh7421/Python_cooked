#Dict methods
# student = {
#     "name": "Alice",
#     "age": 20,
#     "course": "Computer Science"
# }

# print(list(student.keys()))#returns list of keys --- nested keys is not given (inner dict)

# print(len(student))#total key-values pairs

# print(student.values()) # returns list of values 

# print(list(student.items())) #return key-value pair in tuple surrround by list

# #get keys through 2 diff ways

# # if not found then 
# # print(student["name2"])#throws error

# print(student.get('name2')) #no error  ->none

# #in update we can pass new dict  or any immutable object


# student.update({"city":"Delhi"})
# print(student)

# student.update({"name":"Vishwrajsinh"})#overwrite
# print(student)

# #2 methods in pop the key-value pair
# #---------------
# student.pop("name")# if key is not found then give error 
# print(student)

# student.popitem()#removes  the last pair in dict,if nop pair exits then give error
# print(student)
# #----------------

# student.setdefault("branch","CSE")
# print(student)#add new key and value ,if value is not given defaulty and value is none

# # Creating a new dictionary with keys from a list
# keys = ['name', 'age', 'location']
# new_dict = dict.fromkeys(keys, 'Unknown')
# print(new_dict)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'location': 'Unknown'}

# # invert 