#concate
str1 = 'jadeja'
str2 = " vishwrajsinh"
print(str1+str2)

#length
a= len(str1)
print(a)

#if want add empty string 
final_str =str1+" "+str2
print(len(final_str))

#indexing in strings
#######"1 2 3 4 5 6 7 8 9 10 11"
str3 = "C S E _ S t u d e n t"
ch = str3[2]
print(ch)

#we cannot  manuipate chars in strings ,
#  instead we only do asccess only
# we say strings are immutable objs

#slicing in strings
str4 = "Darshan_university"
print(str4[2:6])

print(str4[8:])
print(str4[:6])

#we -ve indexing during the silicing of string
str5 = "apple"
print(str5[-3:-1])#pl

# reverse the string
print(str5[-1::-1])
 