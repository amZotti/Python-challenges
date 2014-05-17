#4.3
def main():
    a, b, c, d, e, f  = [float(number) for number in input("Enter a, b, c, d, e, f: ").split(',')]

    


    if ((a * d) - (b * c)) == 0:
        print("The equation has no solution")
        
    else:

        x = ((e * d) - (b * f))/ (
        (a * d) - (b * c) )

        y = ((a * f) - (e * c)) / (
        (a * d) - (b * c) )

        print("x is %f and y is %f" % (x,y))

if __name__ == "__main__":
    main()
