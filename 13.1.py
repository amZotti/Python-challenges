def main():
    raw = open('text.txt','r')
    text = raw.read()
    #read() receives entire text via as a string data type

    string_to_remove = input("Enter the string you wish to remove")


    new_text = text.replace(string_to_remove, '')
    raw = open('text.txt','w')
    raw.write(new_text)
    raw.close()

if __name__ == "__main__":
    main()
