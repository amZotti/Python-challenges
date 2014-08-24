def checkScore(grade, best, iteration):
    if grade >= best - 10:
        letter = 'A'
    elif grade >= best - 20:
        letter = 'B'
    elif grade >= best - 30:
        letter = 'C'
    elif grade >= best - 40:
        letter = 'D'
    else:
        letter = "F"
        
    print("student", iteration, \
              "score is", grade, "and grade is", letter)
    

def main():
    best = 70
    grades = (input("Enter scores"))
    grade_list = [int(i) for i in grades.split()]
    for i in range(len(grade_list)):
        checkScore(grade_list[i], best, i)


    
if __name__ == "__main__":
    main()
