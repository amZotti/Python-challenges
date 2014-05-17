def main():
    s = input("Enter a string: ").strip()

    if isPalindrome(s):
        print(s, "is a palindrome")
    else:
        print(s, "is not a palindrome!")

def isPalindrome(s):
    low = 0

    high = len(s)-1

    while low < high:
        if s[low] != s[high]:
            return False

        low += 1
        high -= 1
    return True

main()
