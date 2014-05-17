def main():
    feet = float(input("Enter a value for feet"))
    meters = feet * 0.305
    print(format(feet, '4.1f') + ' feet is ' + format(meters, '4.4f') + " meters")


if __name__ == "__main__":
    main()
    
