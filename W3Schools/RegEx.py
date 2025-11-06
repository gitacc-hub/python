#This is not a RegEx tutorial
#import re

#There are four functions. findall(),search(),split(),sub()

# 1)Search() - searches the string for a match
"""
txt="Spain is in Europe."
x=re.search("Portugal",txt)

if x:
    print("We have a match")
else:
    print("There is no match.")
"""

#2) findall() -returns a list containing all matches.
"""
txt="The ball is falling"
x=re.findall("all",txt) #Returns ['all'] ['all'].
x=re.findall("play",txt) #Return [] since there are no matches.
print(x)
"""

# This code uses regular expression \d+ to find all sequences of one or more digits in the given string.

import re
string = "Hello my Number is 123456789 and my friend's number is 987654321"
            
regex = '\d+'
match = re.findall(regex, string)
print(match)

#3) split() -returns a list where the string has been split at each match
"""
txt="The game is fun today."
x=re.split('\s',txt)
print(x)
"""

# 4)Finditer Function
# re.finditer() only takes one string argument.

"""
txt1="I have two phone numbers: 074,888,9448 and 078,299,9233"
txt2="She has two phone numbers: 073,118,0000 and 072,387,1144"
combined_text=txt1+" "+txt2
pattern=r"\d+"
matches=re.finditer(pattern,combined_text)

for match in matches:
    print(f"Found {match.group()} at position {match.start()}-{match.end()}")
"""
