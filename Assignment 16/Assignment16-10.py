# Write a program which accept name from user and display length of its name.
# Input: Marvellous
# Output: 10
def main():
    name = input("Enter your name: ")
    length = len(name)
    print("Length of your name is:", length)

if __name__ == "__main__":
    main()