# Step 1: Create and write data into practice.txt

data = """Hi everyone
we are learning File I/O

using Java.

I like programming in Java.
Apna College

Let's Practice
"""

with open("practice.txt", "w") as f:
    f.write(data)

print("practice.txt created successfully")


# Step 2: Replace all occurrences of "Java" with "Python"

with open("practice.txt", "r") as f:
    content = f.read()

new_content = content.replace("Java", "Python")

with open("practice.txt", "w") as f:
    f.write(new_content)

print("\nAll occurrences of 'Java' replaced with 'Python'")


# Step 3: Search if the word "learning" exists or not

with open("practice.txt", "r") as f:
    content = f.read()

if "learning" in content:
    print("\n'learning' exists in the file")
else:
    print("\n'learning' does not exist in the file")


# Step 4: Find in which line the word "learning" occurs first
def check_word():
    word= "learning"
    with open("Practice.txt","r") as f:
        data = f.read()
        if(data.find(word)!=-1):
            print("found")
        else:
            print("not found")
            
def check_line():
    word = 'pr'
    data = True
    line = 1
    with open("Practice.txt","r") as f:
        while(data):
            data =  f.readline()
            if(word in data):
                print(line)
            line+=1
    return -1

check_word()
check_line()



# Step 5: Count even numbers from a file containing numbers separated by commas

numbers_data = "1,2,3,4,5,6,7,8,9,10"

with open("numbers.txt", "w") as f:
    f.write(numbers_data)

count = 0

with open("numbers.txt", "r") as f:
    data = f.read()

nums = data.split(",")

for val in nums:
    if int(val) % 2 == 0:
        count += 1
 
print(f"\nCount of even numbers: {count}")

