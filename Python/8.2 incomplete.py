str1 = input("Enter a phrase please")
str2 = input("Enter a word you wish to find")




for i, char in enumerate(str1):
    if str2[0] == char:
        print("found first instance of letter at,", i)
        print(str2 == str1[i:i + len(str2)])
        
