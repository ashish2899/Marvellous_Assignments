# Write a program which accept one number and display below pattern.
# Input: 5
# Output:
# 1
# 1   2
# 1   2   3
# 1   2   3   4
# 1   2   3   4   5
def display_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="\t")
        print()

def main():
    number = int(input("Enter a number: "))
    display_pattern(number)

if __name__ == "__main__":
    main()