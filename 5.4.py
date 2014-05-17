
def main():

    print("Miles\t\tKilometers\n")
    for i in range(1,10):
        print(i,"\t\t\t", end = '')
        print(format((i * 1.609), '5.2f'))
              #+ format(5.55, "6.3f") % (i, i * 2.2))
        
    
        

if __name__ == "__main__":
    main()
