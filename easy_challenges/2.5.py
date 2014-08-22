def main():
    subtotal, rate = input("Enter the subtotal and a gratuity rate: ").split(',')
    subtotal, rate = float(subtotal), float(rate)
    gratuity = (subtotal * (rate / 100))
    total = subtotal + gratuity
    print("The gratuity is " + format(gratuity, '.2f') + "$ and the total is " +\
          format(total, ".2f") + "$")

if __name__ == "__main__":
    main()
