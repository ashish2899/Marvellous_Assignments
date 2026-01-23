# Write a program which accept one number for user and check whether number is prime or not.
# Input: 5    Output: It is Prime Number

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    number = int(input("Enter a number: "))
    if is_prime(number):
        print("It is Prime Number")
    else:
        print("It is not Prime Number")

if __name__ == "__main__":
    main()