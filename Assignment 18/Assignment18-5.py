# Write a program which accept N numbers from user and store it into List. Return addition of all 
# prime numbers from that List. Main python file accepts N numbers from user and pass each number 
# to ChkPrime() function which is part of our user defined module named as MarvellousNum. Name of 
# the function from main python file should be ListPrime().
# Input: Number of elements: 11
# Input Elements: 13  5   45  7   4   56  10  34  2   5   8
# Output: 54 (13+5+7+2+5)

import MarvellousNum

def ListPrime(arr):
    sum_primes = 0
    for num in arr:
        if MarvellousNum.ChkPrime(num):
            sum_primes += num
    return sum_primes

def main():
    n = int(input("Enter number of elements: "))
    arr = []
    for _ in range(n):
        value = int(input("Enter element: "))
        arr.append(value)
    
    print("Entered elements are:", arr)
    
    result = ListPrime(arr)
    print("Sum of prime numbers:", result)

if __name__ == "__main__":
    main()