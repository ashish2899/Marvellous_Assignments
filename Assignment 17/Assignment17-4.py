# Write a program which accept one number form user and return addition of its factors.
# Input: 12   Output: 16  (1+2+3+4+6)

def sum_of_factors(num):
    if num <= 0:
        return "Please enter a positive integer"
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total

def main():
    number = int(input("Enter a number: "))
    print("Sum of factors of", number, "is", sum_of_factors(number))

if __name__ == "__main__":
    main()