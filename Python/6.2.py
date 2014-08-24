def main():
    sumDigits(int(input("Enter an integer with no commas please")))




def sumDigits(n):
    final = 0
    start = n
    
    for i in range(len(str(n))):
        final += (n % 10)
        n = n // 10
    print("The sum of all digits in integer %s are %d" % (start,final))


if __name__ == "__main__":
    main()
