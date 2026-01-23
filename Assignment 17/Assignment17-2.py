# Write a program which accept one number and display below pattern.
# Input:  5
# Output:     *   *   *   *   *
#             *   *   *   *   *
#             *   *   *   *   *
#             *   *   *   *   *
#             *   *   *   *   *

def display_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end="   ")
        print()

def main():
    num = int(input("Enter a number: "))
    display_pattern(num)

if __name__ == "__main__":
    main()