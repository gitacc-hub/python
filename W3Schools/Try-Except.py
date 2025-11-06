"""
x=100
try:
    print(x)
except:
    print("An error occurred")
finally:
    print("The try-except block is finished")
"""

#Open a file,read the contents and close the file using try-except-finally
"""
try:
    with open("new.txt","w") as file:
        file.write("This is a new file.")
    with open("new.txt","w") as file:
        contents=file.read()
        print(contents)
    
except Exception as e:
    print("An error occurred:",e)
finally:
    file.close()
"""

#Overwrite an existing file
"""
with open("testfile.txt","w") as f:
    f.write("Overwriting the file contents.")
    f.write("Adding more contents.")
with open("testfile.txt","r") as f:
    print(f.read())
"""

#Raising an exception
"""
x=-1
if x<0:    
    raise Exception("X cant be a negative number")
"""
#Raise a TypeError if x is not an integer:

"""
x=input("Enter a number: ")
if not type(x) is int:
    raise TypeError("Only integers allowed")
else:
    print("You entered:",x)
"""

#Checking if two values are strings and integers using try-except
"""
name=input("Enter your name: ")
age=input("Enter your age: ")

if not name.replace(" ","").isalpha():
    raise TypeError("Invalid input.Name should only contain letters.")
else:
    try:
        age=int(age)
    except:
        raise TypeError("Invalid input.Age should only contain numbers.")
    print("Your name is",name)
    print("You are",age,"years old.")
"""