# Write a program which accept number from user and print that number of "*" on screen.
# Input: 5
# Output:     *    *   *   *   *

def print_stars(count):
    for i in range(count):
        print("*", end="   ")

def main():
    try:
        number = int(input("Enter a number: "))
        if number < 0:
            print("Please enter a non-negative integer.")
        else:
            print_stars(number)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()