

def main():
    minutesTotal = int(input("Enter the number of minutes"))
    hourTotal = minutesTotal / 60
    daysTotal = hourTotal / 24
    daysFinal = daysTotal % 365
    yearsFinal = daysTotal // 365

    print("%d minutes is approximetely %d years and %d days" %(minutesTotal,yearsFinal,daysFinal))


if __name__ == "__main__":
    main()
