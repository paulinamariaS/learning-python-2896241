#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def func1():
    print("I am a function")

# TODO: function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# TODO: function that returns a value
def cube(x):
    return x*x*x

# TODO: function with default value for an argument
def power(num, x=1):
    result = 1;
    for i in range(x):
        result = result*num
    return result

# TODO: function with variable number of arguments
def multi_add(*args):       # it means that i can pass a variable number of arguments
    result = 0
    for x in args:
        result=result+x
    return result


# func1()         # the function is called directly which executes the content of the funcion
# print(func1())  # the fnc is also called inside the print sttement, so the output is the same as before. The value 'none' is a result of calling print fnc
# print(func1)    # functions are the values that can be passed around

# func2(10, 20)
# print(func2(10,20))
# print(cube(3))

print(power(2))
print(power(2,3))

print(power(x=3, num=2))        # you dont have to call the function with particular order, as log as you supply the names with the values

print(multi_add(4,5,10,4))