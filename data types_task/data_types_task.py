# With is the differences between ‘ ’ “ ” ‘’’ ‘’’
# I did'n seen any differenz between it

# Create a string with the name ‘mystero’
strName = 'Mystro'                             # Mystro
print(strName)
# Make the string letters capital
print(strName.upper())                         # MYSTRO
# Create a list of values from 10 to 20
listName = [10,11,12,13,14,15,16,17,18,19,20]
print(listName)                                # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Add 30 to the end of the list
listName.append(30)
print(listName)                                # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30]
# Add 40 as the second element of the list
listName.insert(1,40)
print(listName)                                # [10, 40, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30]
# Print how many elements in the list
print(len(listName))                           # 13
# replace the second element in the list with 100
listName[1] = 100
print(listName)                                # [10, 100, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30]
# Create a tuple with values from 1 to 5
tupleNama = (1,2,3,4,5)
print(tupleNama)                               # (1, 2, 3, 4, 5)
# Can we add 10 to the end of the tuple?
# No
# Create a dict of value Mahmoud:28 , ahmed:30
dictName = {'Mahmoud':28 , 'ahmed':30}
print(dictName)                                # {'Mahmoud': 28, 'ahmed': 30}
# Print Mahmoud age from the dict
print(dictName.get('Mahmoud'))                 # 28
# What is the differences between mutable and immutable data types ?
#  Lists are just like the arrays, declared in other languages. Lists need not be homogeneous always which makes
#  it a most powerful tool in Python. Lists are mutable, and hence, they can be altered even after their creation.

# Tuple is immutable: A tuple is a collection which is ordered and unchangeable, does not allow duplicate members.
# In Python tuples ar written with round or inside parentheses (), separated by commas. The parentheses are optional,
# however, it is a good practice to use them.