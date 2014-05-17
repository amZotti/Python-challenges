from collections import Counter

def main():
    original_nums = input("Enter integers between 1 and 100: ")
    nums = [i for i in original_nums.split()]
    
    counts = Counter(nums).most_common()
    for i in counts:
        print(i,"occurs",counts[i],"time")
   
    '''for i in counts:
        if counts[i] == 1:
            print(i,"occurs",counts[i],"time")
        else:
            print(i,"occurs",counts[i],"times")'''

    

    
if __name__ == "__main__":
    main()


