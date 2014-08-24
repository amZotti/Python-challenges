def percentage(whole, rate = 5):
    return (rate * whole) / 100


def main():
    tuition = 10000
    TUITION_AFTER_TEN_YEARS = 10
    TOTAL_COST_AFTER_FOUR_YEARS = 4
    cost = 0

    for year in range(TUITION_AFTER_TEN_YEARS):
        tuition += percentage(whole = tuition)

    for year in range(TOTAL_COST_AFTER_FOUR_YEARS):
        tuition += percentage(whole = tuition)
        cost += tuition

    print("Tuition is: ", '$',format(tuition, '<6.2f'))
    print("Cost of four years of school is: ", '$',format(cost, '<6.2f'))
        
        
    



if __name__ == "__main__":
    main()
