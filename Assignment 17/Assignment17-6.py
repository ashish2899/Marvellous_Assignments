# Write a program which accept one number and display below pattern.
# Input: 5
# Output:     *   *   *   *   *
#             *   *   *   *   
#             *   *   *   
#             *   *   
#             * 

def dispaly_pattern(no):
    for i in range (no,0,-1):
        for j in range(i):
            print("*", end="\t")
        print()

def main():
    value = int(input("Enter number:"))
    dispaly_pattern(value)

if __name__ == "__main__":
    main()