# Write a program which accept number from user and check whether that number is positive or 
# negative or zero.
# Input: 11       Output: Positive Number
# Input: -8       Output: Negative Number
# Input: 0        Output: Zero

def CheckNumber(num):
    if num > 0:
        print("Positive Number")
    elif num < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    print("Enter a number:")
    value = int(input())
    CheckNumber(value)

if __name__ == "__main__":
    main()