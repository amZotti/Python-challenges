def main():
    ssn = input(("enter SSN in format:\
    dddd-dd-ddd, where d is a digit")).strip()
    ssn = ssn[1:-1]

   
    if ssn[:3].isdigit() and ssn[3] == "-" and ssn[6] == "-" and \
    ssn[7:].isdigit() and len(ssn) == 11:
        print("SSN is valid")
    else:
        print("SSN is invalid")
        

if __name__ == "__main__":
    main()
