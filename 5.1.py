
def main():


    operating = True
    total = 0
    average = 0
    positiveNumber = 0
    negativeNumber = 0
    totalAttempts = 0

    while operating:
        user_Input=int(input("Enter an integer, the input ends if it is 0: "))
        if user_Input < 0:
            negativeNumber += 1
            total += user_Input
        elif user_Input > 0:
            positiveNumber += 1
            total += user_Input
        elif user_Input == 0 and total == 0:
            print("You didn't enter any number")
            operating = False
        elif user_Input == 0:
            totalAttempts = positiveNumber + negativeNumber
            average = total / totalAttempts
            print("The number of positives is ", positiveNumber)
            print("The number of negatives is ", negativeNumber)
            print("The total is ", total)
            print("The average is ", average)
            break
        
    
        

if __name__ == "__main__":
    main()
