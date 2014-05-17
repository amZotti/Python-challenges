import math

def area(n, side):
    area= (n * (side * side))/(
        4 * math.tan(math.pi/n))
    return area

def main():
    
    sideNumber = int(input("Enter the number of sides :"))
    sideLength = float(input("Enter the side: "))

    
    print("The area of the polygon is %f" %(area(sideNumber, sideLength)))
    

if __name__ == "__main__":
    main()
