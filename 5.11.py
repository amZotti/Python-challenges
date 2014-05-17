def main():
    number_of_students = int(input("How many students? "))
    scores = []
    max1 = 0
    max2 = 0
    for i in range(1, number_of_students + 1):
        scores.append(int(input("Input score for student number %d: " %i)))
                          
    max1 = max(scores)
    scores.remove(max(scores))
    max2 = max(scores)

    print("Top two scores were %d and %d" % (max1, max2))



if __name__ == "__main__":
                          main()


    
