def getMatrix():
    matrix = []

    numberOfRows = int(input("Enter number of rows"))
    numberOfColumns = int(input("Enter number of columns"))
    for row in range(numberOfRows):
        matrix.append([])
        for column in range(numberOfColumns):
            value = int(input("Enter a value and press enter: "))
            matrix[row].append(value)
    return matrix

def accumulate(m):
    total = 0
    for row in m:
        total += sum(row)

    return total

def main():
    m = getMatrix()
    print(m)
    print("\nSum of all elements is", accumulate(m))

if __name__ == "__main__":
    main()
 
