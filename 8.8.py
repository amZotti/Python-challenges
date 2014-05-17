

def main():
    MESSAGE = "Please enter a binary string consisting of only 0's and 1's"
    print(binaryToDecimal(input(MESSAGE)))

def binaryToDecimal(binaryString):
    return int(binaryString,base=2)



if __name__ == "__main__":
    main()
