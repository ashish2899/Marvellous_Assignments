# Write a program which display first 10 even numbers on screen.
# Output:     2   4   6   8   10  12  14  16  18  20
def display_even_numbers(n):
    for i in range(1, n + 1):
        print(i * 2, end='   ')

def main():
    num = 10
    display_even_numbers(num)

if __name__ == "__main__":
    main()