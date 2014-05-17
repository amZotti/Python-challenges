def qsort(array = [4,2,5,11,424,6,2]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x== pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        return qsort(less)+equal+qsort(greater)

    else:
        return array
