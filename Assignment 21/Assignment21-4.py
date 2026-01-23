# Design a Python application that creates two threads.
# Thread 1 should compute the sum of elements from a list.
# Thread 2 should compute the product of elements from the same list.
# Return the results to the main thread and display them.

import threading
def compute_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def compute_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

def main():
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    
    result = [0, 0]  # To store sum and product
    
    thread_sum = threading.Thread(target=compute_sum, args=(numbers, ),)
    thread_product = threading.Thread(target=compute_product, args=(numbers, ))

    result[0] = thread_sum
    
    thread_sum.start()
    thread_product.start()
    
    thread_sum.join()
    thread_product.join()
    
    print(f"The sum of the elements is: {thread_sum}")
    print(f"The product of the elements is: {thread_product}")

if __name__ == "__main__":
    main()