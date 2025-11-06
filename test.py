#This is the main file
import re
numbers="My phone numbers 078922938221 and 0748889448"
pattern=r"\d+"
search=re.findall(pattern,numbers)
print(search)