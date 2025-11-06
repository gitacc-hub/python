"""
msg="Hello" # Msg is now a global vaariable
def greet():
    print("Inside function: ",msg)
greet()
print("Outside Function: ",msg)
"""

#2) Difference between local and global variable
"""
def greet():
    msg="Hi there"
    print(msg)
msg="Python is awesome"
greet()
print(msg)
"""

#Global VS Local
"""
a = 1  # Global variable

def first():
    print("This is:", a)  # Uses global a

def second():
    a = 2  # Local shadows global
    print("This is:", a)

def third():
    global a
    a = 3  # Modifies global a
    print("This is:", a)

first()
second()
third()

"""

