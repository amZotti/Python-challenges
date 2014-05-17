def main():
    reverse(input("Enter a number you want reversed!"))

def reverse(number):
    print("The reversal of %s is %s" % (number, number[::-1]))


if __name__ == "__main__":
    main()
