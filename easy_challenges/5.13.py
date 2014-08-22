def main():
    list_of_fives = []
    list_of_sixes = []
    for i in range(100,201):
        if i % 5 == 0:
            list_of_fives.append(i)
        elif i % 6 == 0:
            list_of_sixes.append(i)
    print(list_of_fives)
    print(list_of_sixes)
            
    

if __name__ == "__main__":
                          main()
