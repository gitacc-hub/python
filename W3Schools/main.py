"""import mymodule as md"""
#There is a built-in function to list all the function names (or variable names) in a module.
# The dir() function:
"""
x=dir(md)
print(x)
"""


#You can choose to import only parts from a module, by using the from keyword.
"""from mymodule import greeting"""


#A date in Python is not a data type of its own,
# but we can import a module named datetime to work with dates as date objects.
"""
import datetime as time
x=time.datetime.now()
print(x)
"""


#Return the year and name of weekday:
"""
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
"""

#Create a date object
"""
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)
"""

"""
import datetime as time
x=time.datetime.now()
print(x.strftime("%I"))

B-Full Month(October)
b-Short version of Month e.g(Oct)
d-Day of the month(23)
Y-Full version of year
p-AM/PM
"""