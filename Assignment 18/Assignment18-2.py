# Write a program which accept N numbers from user and store it into List. Return Maximum number 
# from that List.
# Input: Number of elements: 7
# Input Elements: 13  5   45  7   4   56  34
# Output: 56

def findMaximum(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

def main():
    n = int(input("Enter number of elements: "))
    
    numbers = []
    for i in range(n):
        num = int(input(f"Enter element {i + 1} :"))
        numbers.append(num)

    print("Elements in the List are :", numbers)

    maximum = findMaximum(numbers)

    print("Maximum number from the List is:", maximum)


if __name__ == "__main__":
    main()