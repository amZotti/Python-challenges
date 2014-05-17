l1 = []
for i in range(3):
    l1.append([])
    for k in range(4):
        l1[i].append(int(input("Enter a 3-by-4 matrix row for row %d" %k)))

for column in range(len(l1[0])):
    count = 0
    for row in range(len(l1[column])):
                   count += l1[row][column]
    print("The sum of row %d is %d" % (row,count))
                   
