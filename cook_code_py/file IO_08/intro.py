#python perfom read, write,append operation in file

#types of files:
# 1 text file -> .txt,.docx,.log,etc
# 2 binary file -> .mp4,.mov,.png,.jpeg,etc

#f = open ("filename","mode") by default read  mode

import sys

#my default read mod  only open when we have created file not 
#new file is created
fp = open("demo.txt", "r")

data = fp.read()
print(data)

line1 = fp.readline()
print(line1)

line2 = fp.readline()
print(line2)

fp.close()


#write  mod new file create and overwrite in old file
fp = open("NewFile.txt","w")

fp.write("I want some new packages in this file12")

fp.close

#appending in the old demo file  
fp = open("demo.txt","a")

fp.write(" \n I have apppend  new line in this file")

fp.close

#reading the data from the new file created

fp = open("NewFile.txt","r")

data = fp.read()
print(data)

fp.close()

#some exclusive  mod in python

#r+ pointer is at starting for overwrite
fp = open("demo.txt","r+")

data = fp.read()
print(data)

fp.write("abc")

data = fp.read()
print(data)

fp.close

#w+ read and write ther old data is truncate
fp = open("demo.txt","w+")

data = fp.read()
print(data)

fp.write("abc")

data = fp.read()
print(data)

fp.close()

#a+ read and write but old data is not truncate and pointer is at end of line
fp = open("demo.txt","a+")

data = fp.read()
print(data)

fp.write("\nabc")

data = fp.read()
print(data)

fp.close()

#with syntax  it automatically close the file 

with open("demo.txt","w+") as f:
    print(f.read())  
    
# to delete the file we need to import os module

import os
os.remove("NewFile.txt")