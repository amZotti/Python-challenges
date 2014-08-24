import re

def main():
    file_in = input("Enter a filename: ")
    content = open(file_in,'r')
    raw = content.read()

    print(count_characters(raw),"characters")
    print(count_words(raw),"words")
    print(line_count(raw),"lines")
    



def count_characters(raw):
    return len(raw)

def count_words(raw):
    just_Words = re.sub('[^A-Za-z]+', ' ', raw)
    word_count = 0
    raw_list = just_Words.split(' ')

    for i in raw_list:
        if i.isalpha():
            word_count += 1
            
    return word_count

def line_count(raw):
    just_Lines = re.sub('[^\n]','',raw)
    #NOTE: there is a '+ 1' to account for the first line
    #Which does not have a newline statement since that is the starting location
    return len(just_Lines) + 1
    
    
    


if __name__ == "__main__":
    main()
