from math import *

def main():
    print("Degrees\t\t     Sin\t     Cos\n")
    for i in range(0,370,10):
        print(i, end = '')
        print('\t\t',format(sin(radians(i)), '8.4f'), end = '')
        print('\t',format(cos(radians(i)), '8.4f'), end = '')
        print()
        
        
        


if __name__ == "__main__":
    main()
