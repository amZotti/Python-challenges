import math

def main():
    radius, length= input("Enter the radius and length of a cylinder: ").split(",")
    radius, length =float(radius.strip()), float(length.strip())
    area = radius * radius * math.pi
    volume = area * length
    print(" The area is " + format(area, "5.2f"))
    print(" The volume is " + format(volume, "5.2f"))
if __name__ == "__main__":
    main()
