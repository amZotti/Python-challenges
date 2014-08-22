def getPentagonalNumber(n):
    return (n * ((3 * n) - 1))/2
    

def main():
    for i in range(1, 100, 10):
        print(' '.join(['%6d' % getPentagonalNumber(n) for n in range(i, i + 10)]))


if __name__ == "__main__":
    main()
