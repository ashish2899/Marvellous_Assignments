# Write a program which accept number from user and return addition of digits in that number.
# Input: 5187934  Output: 37
def add_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

def main():
    user_input = int(input("Enter a number: "))
    result = add_digits(user_input)
    print("Addition of digits:", result)

if __name__ == "__main__":
    main()