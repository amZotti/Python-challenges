
def main():
    number = int(input("Input a number"))
    width = int(input("Enter the desired width"))
    print(format(number, width))
    

def format(number, width):
    length = len(str(number))
    new_number = ''
    
    if length >= width:
        return number
    
    elif length < width:
        zeros = width - length
        return(('0'*zeros) + str(number))
       
        
if __name__ == "__main__":
    main()
