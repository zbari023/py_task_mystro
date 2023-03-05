# Check if 10 is bigger than 15 or not
x=10
print(x > 15)                            #False
#If 10 is not bigger than 15 print x is smaller than 15
if not (x > 15):
    print("x is smaller than 15")        # x is smaller than 15
# In which cases we will use all
# when we use more than one condition in if case

# What is the differences between all , and
# What is the differences between any , or
# If we need all the conditions to be true we will use
# write s simple ternary operator
a = 7
b = 2
if a > b:
    print("a is bigger than b")
elif a<b:
    print(" b is bigger than a ")
else:
    print("a is equal to b")
listName=[2,9,6,8,10]
if 4 in listName:
    print(True)
elif 4 not in listName:
        print(False)
if 8 and 6 in listName:
    print(True)
if 3 or 6 in listName:
    print(True)
if all([2,4,5]) in listName:
    print(True)
elif not all([2,4,5]) in listName:
    print(False)