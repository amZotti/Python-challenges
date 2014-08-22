from collections import Counter

def count(s1,s2):
    #how many times does s2 occur in s1?
    split_s1 = s1.split()
    split2_s1 = [i.strip(',') for i in split_s1]
    
    raw_count = Counter(split2_s1)
    
    
    return raw_count[s2]


def main():
    print(count("system error, syntax error", "error"))

    


if __name__ == "__main__":
    main()
