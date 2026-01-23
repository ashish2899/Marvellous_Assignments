# Write a program which accept N numbers from user and store it into List. Return addition of all 
# elements from that List.
# Input: Number of elements: 6
# Input Elements: 13  5   45  7   4   56
# Output: 130

def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    n = int(input("Enter number of elements: "))
    
    numbers = []
    for i in range(n):
        num = int(input(f"Enter element {i + 1} :"))
        numbers.append(num)

    print("Elements in the List are :", numbers)

    total = 0

    total = sum(numbers)

    print("Addition of all elements is:", total)



if __name__ == "__main__":
    main()