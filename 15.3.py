def gcd(m,n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)





def main():
    print("Enter two numbers and I will calculate the greatest common\
denominator between the two of them, just for you!")
    
    m = int(input("\nEnter the first number now"))
    n = int(input("Enter second number now"))
    result = gcd(m,n)
   

    print("The divisor both these values share is: %d" %(result))





if __name__ == "__main__":
    main()
