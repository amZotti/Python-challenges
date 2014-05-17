import json

def largestNum(l1, **kwargs):
    try:
        maxNum = kwargs['maxNum']
    except:
        maxNum = 0

    if len(l1) < 1:
        return maxNum
    else:
        if l1[-1] > maxNum:
            maxNum = l1.pop() 
        else:
            l1.pop()
          
    
    return largestNum(l1, maxNum=maxNum)

def main():
    var = input("Please enter a LIST of integers and I will magically show you the largest of them all!")
    l1 = json.loads(var)
    print(largestNum(l1))

if __name__ == "__main__":
    main()
