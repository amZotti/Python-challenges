import re


def main():
    genome = input("Enter a genome string: ")
    slices = re.findall("ATG.*?(?:TAG|TAA|TGA)", genome)
    if slices:
        for i in slices:
            print(i[3:-3])
    else:
        print("No genes found")
        
    
    
    


if __name__ == "__main__":
    main()
