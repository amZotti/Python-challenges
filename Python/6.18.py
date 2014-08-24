from random import randint


def main():
    printMatrix(int(input("Enter n: ")))






def printMatrix(n):
    for i in range(n):
        print()
        for i in range(n):
            print(randint(0,1), ' ', end = '')
            
    
if __name__ == "__main__":
    main()
