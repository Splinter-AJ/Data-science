lst=[]

def Create():
    lst1=[]


    Account_number = int(input("Enter Account number : "))
    Account_holder_name = input("Enter your name: ")
    Address = input("Enter Your Address: ")
    Fixed_Deposit = int(input("Enter your Fixed Deposit : "))
    if Fixed_Deposit >= 500:
        lst1.append(Account_number)
        lst1.append(Account_holder_name)
        lst1.append(Address)
        lst1.append(Fixed_Deposit)
        lst1.append("\n")
        lst.append(lst1)
    else:
        print("Fixed Deposit must be above or equal to 500 ")
def Deposit():

    print("Search Account number: ")
    id = int(input("Enter Account number:"))
    Amount = int(input("Enter the amount to be added: "))
    flag = 0
    x = 0

    for x in lst:
        flag = 0
        if id == x[0]:
            flag = 1
            break
    if flag == 1:
            print("*" * 150)
            if (Amount % 100) == 0:
                x[3]+=Amount
            else:
                print("please enter multiples of 100 :")
            print("*" * 150)
    else:
            print('NOT Found!')


def Withdraw():
    print("Search Account number: ")
    id = int(input("Enter Account number:"))
    Amount = int(input("Enter the amount you need to withdraw: "))
    flag = 0
    x = 0

    for x in lst:
        flag = 0
        if id == x[0]:
            flag = 1
            break
    if flag == 1:
        print("*" * 150)
        if (x[3] >= Amount + 500) and Amount % 100 ==0:
            x[3] -= Amount
        else:
            print("Please make sure the you have at least 500 rs as balance:  ")
        print("*" * 150)

    else:
        print('NOT Found!')

def Balance():
    print("Search Account number: ")
    id = int(input("Enter Account number:"))

    flag = 0
    x = 0
    for x in lst:
        flag = 0
        if id == x[0]:
            flag = 1
            break
    if flag == 1:
        print("*" * 150)
        print("Your Balance is ",x[3])
        print("*" * 150)
    else:
        print('NOT Found!')







while True:
    print("Available operations: \n1) Create Account \n2) Deposit amount \n3) Withdraw Amount \n4) Balance \n5) EXIT")
    option = int(input("Enter your option: "))

    if option == 1:
        Create()
    elif option == 2:
        Deposit()
    elif option == 3:
        Withdraw()
    elif option == 4:
        Balance()

    else:
        exit("END")