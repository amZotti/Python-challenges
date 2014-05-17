def main():
    years = int(input("Enter years of loan"))
    amount = int(input("Enter loan amount"))
    rate = 5.0
    amount_increase = 0.0

    for i in range(years * 12):
        
        display(rate,amount,years, amount_increase)
        rate, amount_increase = calculate_interest(rate, amount)


def display(rate, amount, years, amount_increase):
    compound_interest = 0
    print(amount)
    print(amount_increase)
    
    compound_interest += amount_increase
    total = compound_interest + amount
    #Outline
    print("Interest Rate\tMonthly Payments\tTotal amount")
    print()

    #Content
    print(format(rate, '5.3f'), '\t',
          format((compound_interest), '5.2f'), '\t',
          format(total, '5.2f'))
    return compound_interest
    
    



def calculate_interest(rate, amount):
    rate = increase_interest(rate)
    amount_increase = (amount * rate) / 100
    
    return rate, amount_increase


def increase_interest(rate):
    if rate < 8.0:
        rate += (1/8)
        return rate
    else:
        return rate
if __name__ == "__main__":
    main()
