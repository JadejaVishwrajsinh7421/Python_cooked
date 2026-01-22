# 1. store following  in py dict:
    # table : "a piece of furniture", lists of facts & figure
    # cat : "a small animal" 
    
dict= {
    "cat":"a small animal",
    " table":["a piece of furniture", "lists of facts & figure"]
}
print(dict)
print(dict.values())

# 2. you are given a list of subject for student . 
# assume one class is reqn for 1 subject . how many classrom are needed by students
li = ["python","java","c++","js","java","python","c++","c"]

set1 =set(li)
classroom = len(set1)
print("classroom is needed",classroom)

# 3. wap to enter marks of 3 sub from user and store them in dict . 
# start an empty dict & add one bt one.use sub name as key

marks = {}
x = int(input ("enter marks of phy :"))
marks.update({"phy":x})

x = int(input ("enter marks of chem :"))
marks.update({"chem":x})

x = int(input ("enter marks of maths :"))
marks.update({"maths":x})

print(marks)

# 4. figure out a way to store 9 and 9.0 separate values in the set 
values ={9,9.0}
print(values)
# as 9 and 9.0 is same 

values = {9,"9.0"}
print(values)
  # another apporach use tuple
values2 = {("float",9.0),("int",9)}  
print(values2)


