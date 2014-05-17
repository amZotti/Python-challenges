import urllib.request
import re


def getContent(URL):
    raw_input = urllib.request.urlopen(URL).read().decode()
    content = re.sub('[^A-Za-z0-9\.]+', ' ', raw_input)
    return content.split(' ')


def display_pay(full_pay,assistant_pay,associate_pay,associates,assistants,full,faculity_members):
    
    total_overall = average = 0
    total_overall = full_pay+assistant_pay+associate_pay
    average = total_overall/faculity_members

    print("Total salary for all faculity members is: ","%.2f" % total_overall)
    print("Average salary for all faculity members is: ", "%.2f" % average)

    print()
    print("Total salary for associates: ","%.2f" % associate_pay)
    print("Average salary for associates: ", "%.2f" % (associate_pay/associates))

    print()  
    print("Total salary for assistants: ","%.2f" % assistant_pay)
    print("Average salary for assitants: ", "%.2f" % (assistant_pay/assistants))

    print() 
    print("Total salary for full time: ","%.2f" % full_pay)
    print("Average salary for full time: ", "%.2f" % (full_pay/full))



def calculatePay(content):
    associate_pay = assistant_pay = full_pay = 0
    faculity_members = assistants = associates = full = 0

    
    for i in range(len(content)):
        if content[i] == "associate":
            associate_pay += float(content[i+1])
            faculity_members += 1
            associates += 1

        elif content[i] == "assistant":
            assistant_pay += float(content[i+1])
            faculity_members += 1
            assistants += 1
            
        elif content[i] == "full":
            full_pay += float(content[i+1])
            faculity_members += 1
            full += 1

    display_pay(full_pay,assistant_pay,associate_pay,associates,assistants,full,faculity_members)

def main():
    URL = "http://cs.armstrong.edu/liang/data/Salary.txt"
    content = getContent(URL)
    calculatePay(content)

if __name__ == "__main__":
    main()
