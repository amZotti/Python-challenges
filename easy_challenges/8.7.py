str1 = str(input("enter a phone number please"))



def main():
    newstr = ''
    for letter in str1:
        if letter.isdigit() or letter == '-':
            newstr += letter
        else:
            newstr += str(letterConversion((letter).lower()))
        

    print(newstr)


def letterConversion(letter):
    if letter in 'abc':
        return 2
    elif letter in 'def':
        return 3
    elif letter in 'ghi':
        return 4
    elif letter in 'jkl':
        return 5
    elif letter in 'mno':
        return 6
    elif letter in 'pqrs':
        return 7
    elif letter in 'tuv':
        return 8
    elif letter in 'wxyz':
        return 9
    elif letter == "'":
        return ""
    else:
        return letter

if __name__ == "__main__":
    main()



    
    
