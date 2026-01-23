# Write a program which accept one number from user and return its factorial.
# Input:  5   Output: 120

def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

def main():
    number = int(input("Enter a number: "))
    print("Factorial of", number, "is", factorial(number))

if __name__ == "__main__":
    main()