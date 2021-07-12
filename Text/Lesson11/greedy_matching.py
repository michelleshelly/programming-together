import re

x = 'My 3 favourite numbers are 1 and 7'
y = re.findall('[0-9]+',x)
print(y)

# S is non-white space. s is white space
# \n is next line
#\\ to escape the \s which is finding white space. so will find literally a \ in sentence
# '[0-9]+ ?' ? at the back shows non greedy matching

