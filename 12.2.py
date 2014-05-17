
class Location:
    def __init__(self,row,column,maxValue):
        self.row = row
        self.column = column
        self.maxValue = float(maxValue)
        print("The location of the largest element is %d at (%d, %d)"%(self.maxValue,self.row,self.column))



def getValues():
    row,column = [int(i) for i in input("Enter the number of rows and columns in the list: ").split(',')]
    l1=[]

    for k in range(row):
        l1.append([])
    for i in range(row):
        print("Enter row: ",i)
        l1[i] = input().split()
        
        if len(l1[i]) == column:
            pass
        else:
            print("Invalid entry, Enter",column,"values,not",len(l1[i]),". Aborting!")
            break

    return l1


def locateLargest():
    l1 = getValues()
    maxValue = max(max(l1))
    row =  l1.index(max(l1))
    column = l1[row].index(maxValue)

    
    return Location(row,column,maxValue)
        
def main():
    locateLargest()

if __name__ == "__main__":
    main()


