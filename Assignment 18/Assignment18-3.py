# Write a program which accept N numbers from user and store it into List. 
# Return Minimum number from that List.
# Input: Number of elements: 4
# Input Elements: 13  5   45  7
# Output: 5

def findMinimum(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

def main():
    n = int(input("Enter number of elements: "))
    
    numbers = []
    for i in range(n):
        num = int(input(f"Enter element {i + 1} :"))
        numbers.append(num)

    print("Elements in the List are :", numbers)

    minimum = findMinimum(numbers)

    print("Minimum number from the List is:", minimum)


if __name__ == "__main__":
    main()