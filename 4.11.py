def main():
    
    year  = int(input("Enter a four digit year please"))
    month_number = int(input("Enter month please (From 1 to 12)"))
    month = which_month(month_number)

    

    
    leap_Year = False
    
    if year % 4 == 0:
        leap_Year = True

    if leap_Year == True and month_number == 2:
        print("There are 28 days in %s, %d" % (month,year))
    elif leap_Year == False and month_number == 2:
        print("There are 29 days in %s, %d" % (month,year))
    elif month_number % 2 == 0:
        print("There are 31 days in %s, %d" % (month,year))
    elif month_number % 2 == 1:
        print("There are 30 days in %s, %d" % (month,year))
        

def which_month(month):
    if month == 1:
        return "January"
    elif month == 2:
        return "February"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    elif month == 12:
        return "December"
    else:
        print("You enetered an invalid number. Enter number between 1 and 12 please")
        


    

if __name__ == "__main__":
    main()
    
