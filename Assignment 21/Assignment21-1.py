# Design a Python application that creates two threads named Prime and NonPrime.
# Both threads should accept a list of integers.
# The Prime thread should display all prime numbers from the list.
# The NonPrime thread should display all non-prime numbers from the list.

import threading

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_thread(numbers):
    print("Prime Numbers:")
    for num in numbers:
        if is_prime(num):
            print(num)

def non_prime_thread(numbers):
    print("Non-Prime Numbers:")
    for num in numbers:
        if not is_prime(num):
            print(num)

def main():
    numbers = [10, 15, 23, 42, 7, 8, 19, 4, 6, 11]

    prime = threading.Thread(target=prime_thread, args=(numbers,))
    non_prime = threading.Thread(target=non_prime_thread, args=(numbers,))

    prime.start()
    non_prime.start()

    prime.join()
    non_prime.join()

if __name__ == "__main__":
    main()
