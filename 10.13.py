def eliminateDuplicates(lst):
    
    nums = [i for i in set(lst) if i.isdigit()]
    print("The distinct numbers are: ", end = "")

    for i in nums:
        print(i," ",end = "")

def main():
    raw = input("Enter ten numbers: ")
    eliminateDuplicates(raw)

if __name__ == "__main__":
    main()
