def main():
    print("Miles\t\t Klometers\t|\t Kilometers\t Miles\n")
    NUMBER_OF_KILOMETERS = [20, 25, 30, 35, 40, 45, 50, 60, 65]
    NUMBER_OF_MILES = range(1,11)

    
    kilometersToMiles = [kilometer * 0.621371 for kilometer in NUMBER_OF_KILOMETERS]

    milesToKilometers = [miles * 1.609 for miles in NUMBER_OF_MILES]

    

    for i in range(9):
        print(NUMBER_OF_MILES[i], "\t\t", format(milesToKilometers[i], "<10.3f"),
        "\t|\t",  NUMBER_OF_KILOMETERS[i], "\t\t", format(kilometersToMiles[i], "<10.3f"))

if __name__ == "__main__":
    main()


#Note: the book states that 9 miles == 15.481 kilometers, this is incorrect.
    #The correct answer is 15.481
    
