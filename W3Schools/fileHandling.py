#Create a file and read from it
"""
with open("family.txt","w") as file:
    file.write("My Siblings include:")
with open("family.txt","r") as file:
    print(file.read())
"""

#To check if a file exists in the Operating system
"""
import os
print(os.path.exists("oop.py"))
"""
#Opening a file,reading the contents and closing it
"""
file=open("ip.py","r")
contents=file.read()
print(contents)
file.close()
"""
#Automatically open files,read the contents and close it
"""
with open("recursion.py","r") as file:
    contents=file.read()
    print(contents)
"""
# Reading a file line by line

"""
file=open("mymodule.py","r")
for line in file:
    print(line.strip()) # .strip() to remove newline characters
file.close()
"""

# Using readLine()
"""
file=open("recursion.py","r")
line=file.readline()
while line:
    print(line.strip())
    line=file.readline()
file.close()
"""

#Reading Binary Files
"""
file=open("example.bin","rb")
contents=file.read()
print(contents)
file.close()

Explanation: This code reads a file in binary mode ("rb")
and prints its content as bytes, which is necessary for handling non-text files
"""

#Reading Specific Parts of a File
"""
file=open("recursion.py","r")
content=file.read(10)
print(content)
file.close()
"""
#Reading CSV Files

"""
import csv
import io

# Create a CSV sample in memory
csv_data = """
"""Name,Club,Salary
Simba,Mancity,769400
Sane,Chelsea,48000
Rooney,Manchester United,129087
"""
"""
csvfile = io.StringIO(csv_data)
csvreader = csv.reader(csvfile)
for row in csvreader:
    print(row)

Explanation: Instead of a physical file, we used StringIO to create a file-like object.
The CSV reader parses each line into a list of values.
"""

#Reading JSON Files
"""
import json
with open("sample1.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print(data)
"""

#Overwritting a existing file
"""
with open("goat.txt","w") as file:
    file.write("This is an overwritten file.")
with open("goat.txt","r") as file:
    content=file.read()
    print(content)
"""
#Create only if it does not exist
"""
try:
    with open("file.txt", "x", encoding="utf-8") as f:
        f.write("Created using exclusive mode.\n")

except FileExistsError:
    print("file.txt already exists, exclusive creation aborted.")
"""

#Deleting a file
"""
import os
if os.path.exists("goat.txt"):
    os.remove("goat.txt")
    print("File is successfully removed")
else:
    print("File doesn`t exist")
"""
#Using the join() method to write multiple lines to a file
"""
lines=["Line A","Line B","Line C"]
text="\n".join(lines)+"\n"
with open("line.txt","w") as f:
    f.write(text)
with open("line.txt","r") as f:
    print(f.read())
"""

lines=["One\n","Two\n","Three\n"]
with open("sfjdh.txt","w") as f:
    f.writelines(lines)
with open("sfjdh.txt","r") as f:
    print(f.read())