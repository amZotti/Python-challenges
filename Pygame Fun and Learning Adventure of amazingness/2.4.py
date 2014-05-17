def main():

    pounds = float(input("Enter a value in pounds: "))
    kilograms = pounds * 0.454
    print(format(kilograms, '1.4f') + ' kilograms is %f pounds' %pounds)

if __name__ == "__main__":
    main()
