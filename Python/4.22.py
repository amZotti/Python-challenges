import math

def main():
    raw_x, raw_y = input("Enter a point with two coordinates").split(",")
    
    x = float(raw_x)
    y = float(raw_y)

    
    
    

    if math.sqrt((abs(y) ** 2) + (abs(x) ** 2)) <= 10:
        print("Point (%f,%f) is in the circle" % (x,y))
    else:
        print("Point (%f,%f) is not in the circle" % (x,y))

    



if __name__ == "__main__":
    main()
