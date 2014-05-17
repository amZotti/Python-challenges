def main():

    try:
        splitDigits = input("Enter a four-digit integer")   
        a,b,c,d = splitDigits[0], splitDigits[1], splitDigits[2], splitDigits[3]

        print(int(d))
        print(int(c))
        print(int(b))
        print(int(a))
        
    except Exception:
        print("Please enter a valid four digit integer!")

if __name__ == "__main__":
    main()
        

    
            
            
