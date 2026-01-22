#Dictionary in python 
#store data in key:value pairs 
 
#unordered,mutuabale,and not have duplicate keys
#follows generally hashmap data structure


#dict ={keY:values}

details={ "name" :"vishwrajsinh" ,
        "roll": 360,
        "subject":"Python"
}

print(details)
print(type(details))
#keys can  never be mutuable object ,tuple is might be key but not list 

#to print the values through keys
print(details['name'])


#to assign new values in keys 
details["name"] = 'Jadeja Bapu'#overwrite 
print(details['name'])

#to create null dict
null_dict ={}
print(null_dict)

#nested dict 
#by create value in dict foramt

student = {
    "name" :"rahul",
    "subjects" :{
        "phy" : 97,
        "chem":99,
        "math" :100
    },
    "roll" : 96336
}

print(student["subjects"]["chem"])


#class lecture imp for creating dict 

#1 list of tuple
li =[(1,"one"),(2,"two"),(3,"three")]
new_dict2 = dict(li)
print(new_dict2)

#2 two lists is given  by zip()
li1 = [1,2,3,4]
li2 = ['one','two','three','four']

new_dict3 = dict(zip(li1,li2))
print(new_dict3)

#3 by enumerate() --only have values but didn't have keys then sys allow to generate
li3 = ['one','two','three','four',"five"]
new_dict4 = dict(enumerate(li3 , start=1)) #default start  with 0
