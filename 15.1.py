
def sumDigits(n, **kwargs):
    #Handle holding variable using exception and optional variable
    try:
        total = kwargs['total']
    except:
        total = 0

    if n < 1: #Base case
        return total
    else:
            
        total += n%10 #Add to holding variable
        n = n // 10   #Remove last digit
        return sumDigits(n,total = total)
        

def main():
    var = int(input("Please enter a integer to calculate its sum kthnx"))
    print(sumDigits(var))




if __name__ == "__main__":
    main()
