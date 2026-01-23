# Write a program which accept N numbers from user and store it into List. Accept one another 
# number from user and return frequency of that number from List.
# Input: Number of elements: 11
# Input Elements: 13  5   45  7   56  34  2   5   65
# Element to search: 5
# Output: 3

def findFrequency(numbers, searchElement):
    frequency = 0
    for num in numbers:
        if num == searchElement:
            frequency += 1
    return frequency

def main():
    n = int(input("Enter number of elements: "))
    
    numbers = []
    for i in range(n):
        num = int(input(f"Enter element {i + 1} :"))
        numbers.append(num)

    print("Elements in the List are :", numbers)

    searchElement = int(input("Enter element to search frequency: "))

    frequency = findFrequency(numbers, searchElement)

    print(f"Frequency of {searchElement} is:", frequency)

if __name__ == "__main__":
    main()