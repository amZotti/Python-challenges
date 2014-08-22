def main():

    filename = 'widgetsdemo.py'
    infile = open(filename,'r')
    text = ''.join(infile.readlines()).lower()
    counts = 26 * [0]

    for i in text:
        if i.isalpha():
            counts[ord(i)-ord('a')] += 1

    print(counts)
    
if __name__ == "__main__":
    main()



