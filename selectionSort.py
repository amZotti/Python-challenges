def selectionSortHelper(l1,low,high):

    if low < high:  #implied base case
        
        minValue = l1[low]
        minIndex = low
        
        for i in range(len(l1[low + 1 :high + 1])):
            if l1[i] < minValue:
                #CHANGE NOW!
                minValue = l1[i]
                minIndex = i

        l1[minIndex] = l1[low]
        l1[low] = minValue

    return selectionSortHelper(l1,low + 1,high)


def selectionSort(l1):
    return selectionSortHelper(l1,0,len(l1)-1)
