# Design a Python application that creates two threads.
# Thread 1 should calculate and display the maximum element from an list.
# Thread 2 should calculate and display the minimum element from the same list.
# The list should be accepted from the user.

import threading

# def find_maximum(numbers):
#     maximum = max(numbers)
#     print(f"The maximum element is: {maximum}")

def find_maximum(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    print(f"The maximum element is: {maximum}")

# def find_minimum(numbers):
#     minimum = min(numbers)
#     print(f"The minimum element is: {minimum}")

def find_minimum(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    print(f"The minimum element is: {minimum}")

def main():
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    
    thread_max = threading.Thread(target=find_maximum, args=(numbers,))
    thread_min = threading.Thread(target=find_minimum, args=(numbers,))
    
    thread_max.start()
    thread_min.start()
    
    thread_max.join()
    thread_min.join()

if __name__ == "__main__":
    main()