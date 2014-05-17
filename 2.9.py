def main():
    currentTemperature = float(input("Enter the temperature in Fahrenheit between -58 and 41: "))

    currentWindSpeed = float(input("Enter the wind speed in miles per hour: "))

    windChillIndex = 35.74 + (0.6215 * currentTemperature) - (35.75 * (currentWindSpeed ** 0.16)) + (0.4275 * (currentTemperature * (currentWindSpeed ** 0.16)))

    print("The wind chill index is %f" %windChillIndex)

if __name__ == "__main__":
    main()
