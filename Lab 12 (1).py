account_info = []

def getBalances():
    print()
    print("Checking: $" + account_info[2])
    print("Savings: $" + account_info[3])

def deposit(depAmount):
    print("c. Checking")
    print("s. Savings")
    userChoice = input("Make A Depsoit Into Which Account?: ")

    if userChoice == "c":
        currBalance = int(account_info[2])
        newBalance = currBalance + depAmount
        account_info[2] = str(newBalance)
        print(depAmount, "dollars were deposited into Checking.")
    elif userChoice == "s":
        currBalance = int(account_info[3])
        newBalance = currBalance + depAmount
        account_info[3] = str(newBalance)
        print(depAmount, "dollars were deposited into Savings.")
    else:
        print("Select a Deposit Account.")
        deposit(depAmount)

def withdraw(wAmount):
    print("c. Checking")
    print("s. Savings")
    userChoice = input("Which Account Would You Like to Withdraw From: ")

    if userChoice == "c":
        currBalance = int(account_info[2])
        if currBalance >= wAmount:
            newBalance = currBalance - wAmount
            account_info[2] = str(newBalance)
            print(wAmount, "dollars were withdrawn from Checking.")
        else:
            print("Insufficient Funds")
    elif userChoice == "s":
        currBalance = int(account_info[3])
        if currBalance >= wAmount:
            newBalance = currBalance - wAmount
            account_info[3] = str(newBalance)
            print(wAmount, "dollars were withdrawn from Savings.")
        else:
            print("Insufficient Funds")
    else:
        print("Which Account Would You Like to Withdraw From.")
        withdraw(wAmount)

def transfer(transferAmount):
    print("c. Checking")
    print("s. Savings")
    userChoice = input("Which Account Would You Like To Transfer Money TO: ")

    if userChoice == "c":
        currBalance = int(account_info[2])
        if currBalance >= transferAmount:
            newBalance = currBalance - transferAmount
            account_info[2] = str(newBalance)
            sBalance = int(account_info[3]) + transferAmount
            account_info[3] = str(sBalance)
            print(transferAmount, "dollars has been transferred from Checking to Savings.")
        else:
            print("Insufficient funds.")
    elif userChoice == "s":
        currBalance = int(account_info[3])
        if currBalance >= transferAmount:
            newBalance = currBalance - transferAmount
            account_info[3] = str(newBalance)
            cBalance = int(account_info[2]) + transferAmount
            account_info[2] = str(cBalance)
            print(transferAmount, "dollars were transferred from Savings to Checking.")
        else:
            print("Insufficient funds.")

def atmMenu():
    userChoice = "0"
    while(userChoice != "5"):
        print()
        print("Main Menu")
        print("1. Balance Inquiry")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Exit")
        userChoice = input("Choose from the above options: ")

        if userChoice == "1":
            getBalances()
        elif userChoice == "2":
            try:
                depAmount = int(input("Enter Deposit Amount: "))
                deposit(depAmount)
            except ValueError:
                print("You must enter an amount to deposit.")
        elif userChoice == "3":
            try:
                wAmount = int(input("Enter Withdrawl Amount: "))
                withdraw(wAmount)
            except ValueError:
                print("Enter Withdrawl Amount.")
        elif userChoice == "4":
            try:
                transferAmount = int(input("Enter Transfer Amount: "))
                transfer(transferAmount)
            except ValueError:
                print("Enter Transfer Amount.")
        elif userChoice == "5":
            print("Thank you!")
        else:
            print("Choose a Number Between 1 and 5.")
    
def main():
    inData = "account.txt"
    inFile = open(inData, 'r')
    inText = inFile.read()
    inLines = inText.split('\n')
    inFile.close()

    for line in inLines:
        if ':' in line:
            line_details = line.split(": ")
            line_detail = line_details[1]
            account_info.append(line_detail)

    print("Enter your username and pin number.")
    userID = input("\nUsername: ")
    userPin = input("Pin: ")

    if userID == account_info[0] and userPin == account_info[1]:
        print("Successful Login")

        atmMenu()

        new_account = "ID: " + account_info[0] + "\n"
        new_account = new_account + "Pin: " + account_info[1] + "\n"
        new_account = new_account + "\n"
        new_account = new_account + "Checking: " + account_info[2] + "\n"
        new_account = new_account + "Savings: " + account_info[3]

        outFile = open(inData, 'w')
        outFile.write(new_account)
        outFile.close()
    else:
        print("Incorrect Username or Pin.")

main()
