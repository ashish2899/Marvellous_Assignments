# 7. Write a program which accept one number and display below pattern.
# Input : 5
# Output: 1   2   3   4   5
#         1   2   3   4   5
#         1   2   3   4   5
#         1   2   3   4   5
#         1   2   3   4   5
def display_pattern(num):
    for i in range(num):
        for j in range(1, num + 1):
            print(j, end="\t")
        print()

def main():
    number = int(input("Enter a number: "))
    display_pattern(number)

if __name__ == "__main__":
    main()