def getRectangle(points):
 
    x = []
    y = []
    for i in range(len(points)):
            if i % 2 == 0:
                    x.append(points[i])
            else:
                    y.append(points[i])

    xMin = min(x)
    xMax = max(x)
    yMax = max(y)
    yMin = min(y)

    centerx = (xMax + xMin) / 2
    centery = (yMax + yMin) / 2
    width = xMax-xMin
    height = yMax-yMin
    
    
    print("The bounding rectangle is centered at (%0.2f, %0.2f) with width %0.2f and height %0.2f" % (centerx,centery,width,height))


def main():
      
    points = [float(i) for i in input("Enter the points: ").split()]
    getRectangle(points)


if __name__ == "__main__":
    main()
