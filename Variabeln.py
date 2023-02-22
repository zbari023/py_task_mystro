# Create a Boolean variable named x
x = True
print(x)                              # True
# Create an integer variable named y
y = 5
print(type(y))                        # <class 'int'>
# Create a float variable named z
z = 0.572
print(type(z))                        # <class 'float'>
# Create a string variable names s
s = "Ziad"
print(type(s))                        # <class 'str'>
# Convert the int variable to float
y2 = float(y)
print(type(y2))                       # <class 'float'>
# Can we convert the str to int ?
# s2 = int(s)                         # No , give us a Error , but we can convert integer/float to string
# print(s2)
z2 = str(z)
print(type(z2))                       # <class 'str'>
# Create a list of numbers from 1 to 5
listName = [1,2,3,4,5]
print(type(listName))                 # <class 'list'>
# Create a tuple from 10 to 15
tupleName = (10,11,12,13,14,15)
print(type(tupleName))                # <class 'tuple'>
# Convert the list to tuple
tupleName2 = tuple(listName)          # listName = [1,2,3,4,5]
print((tupleName2))                   # (1, 2, 3, 4, 5)
# Create a dict of 3 values
info = {"Ziad":27 , "Thomas":30 , "cristoph":37}
print(type(info))                     # <class 'dict'>
# Can we use semi colon ; with python
# yes, by defintion a variabels
a = 2 ; b = 3 ; c = 5

# 1) Python is interpreted or compiled ?
# Both
#  run the code via interpreter
# Compiles and converts the program to bytecode, and directly bytecode is loaded in system memory.
# Then compiled bytecode interpreted from memory to execute it.

# 2) What is the differences between low level & high level ?
# * High-level languages:

# + Feature abstraction
# + Are closer to human languages, and are more readable
# + Do not deal with memory management
# + Examples include: Java, Python, Ruby, and C#

# * Low-level languages::

# + Do not feature abstraction
# + Are readable by machines, and are not close to human language
# + Involve memory management
# Examples include assembly language and machine code
