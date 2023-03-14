# Create a simple function that takes 2 numbers and print their values
x = 5
y = 4


def myfunc(x=0, y=0):
    return print(f'x = {x} , y = {y}')


myfunc(x, y)        # x = 5 , y = 4
myfunc()            # x = 0 , y = 0

# Create a function that can take any number of arguments and print the sum of them
def mysum(i=0 ,j=0):
    return i + j
print(mysum(8,3))

# Create the same sum function using the lambda
myadd = lambda x, y : x + y
print(myadd(9,8))

# Write the difference between the local variable and global variable:
# Global variables are declared outside the functions whereas local variables are declared within the functions.
# Local variables are created when the function starts its execution and are lost when the function ends.
# Global variables, on the other hand, are created as the execution of the program begins and are lost when
# the program is ended.
