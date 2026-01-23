# Create on module named as Arithmetic which contains 4 functions as Add() for addition, 
# Sub() for subtraction, Mult() for multiplication and Div() for division. All functions 
# accepts two parameters as number and perform the operation. Write on python program which 
# call all the functions from Arithmetic module by accepting the parameters from user.

def Add(num1, num2):
    return num1 + num2

def Sub(num1, num2):
    return num1 - num2

def Mult(num1, num2):
    return num1 * num2

def Div(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error! Division by zero."