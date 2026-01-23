# Create on module named as Arithmetic which contains 4 functions as Add() for addition, 
# Sub() for subtraction, Mult() for multiplication and Div() for division. All functions 
# accepts two parameters as number and perform the operation. Write on python program which 
# call all the functions from Arithmetic module by accepting the parameters from user.

import Arithmetic

def main():
    print("Enter two numbers:")
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))

    addition = Arithmetic.Add(num1, num2)
    subtraction = Arithmetic.Sub(num1, num2)
    multiplication = Arithmetic.Mult(num1, num2)
    division = Arithmetic.Div(num1, num2)

    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")

if __name__ == "__main__":
    main()