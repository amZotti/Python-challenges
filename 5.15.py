def main():
    
    processing = True
    n = 12000



    while processing:
      
        if is_Cube_Root(n) == True:
            print("Cube root closest to 12,000 is", n)
            processing = False
        else:
            n -= 1


def is_Cube_Root(n):
        floatroot = (n ** (1.0 / 3.0))
        introot = int(round(floatroot))
        return introot*introot*introot == n
    
if __name__ == "__main__":
    main()

