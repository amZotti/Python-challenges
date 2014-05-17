from account import *


def main():
    account_list = Account_creation()


    while True:
        account_id = int(input("Enter a account id: "))

        if account_list[account_id]:
            ATM_menu(account_list[account_id])
        else:
            print("That ID is invalid. Try again!")
            continue
        
            
    
def ATM_menu(account_id):
    print(account_id)
    ATM_on = True
    while ATM_on == True:
        print()
        print("Main menu")
        print("1: check balance")
        print("2: withdraw")
        print("3: deposit")
        print("4: exit")

        selection = input()

        if selection == '1':
            print("The balance is ", account_id.getBalance())

        elif selection == "2":
            amount = int(input("Enter an amount to withdraw"))
            account_id.withdraw(amount)
        elif selection == "3":
            amount = int(input("Enter an amount to deposit: "))
            account_id.deposit(amount)
        elif selection == "4":
            ATM_on = False

        else:
            continue
    

def Account_creation():
    account_list = []
    for i in range(10):
        i = Account(i,100,0)
        account_list.append(i)

    return account_list






if __name__ == "__main__":
    main()
