
def main():

    print("Kilograms\t\tPounds\n")
    for i in range(1,201):
        print(i,"\t\t\t", end = '')
        print(format((i * 2.2), '5.2f'))
              #+ format(5.55, "6.3f") % (i, i * 2.2))
        
    
        

if __name__ == "__main__":
    main()
