accounts = [
    {
        'accountName': 'John Doe',
        'balance': 1000.0,
        'status': 'active',
        'cardNumber': 123456,
        'pin': 7890
    },
    {
        'accountName': 'Jane Smith',
        'balance': 5000.0,
        'status': 'active',
        'cardNumber': 987654,
        'pin': 4321
    },
    {
        'accountName': 'Alice Johnson',
        'balance': 2500.0,
        'status': 'inactive',
        'cardNumber': 246813,
        'pin': 1357
    }
]

admin = [
    {
        'username': 'admin',
        'password': 'admin'
    }
]


def verify_account():
    card_number = int(input("Enter your card number: "))
    pin = int(input("Enter your PIN: "))
    for account in accounts:
        if account['cardNumber'] == card_number and account['pin'] == pin:
            return account['cardNumber'], account['status']
    print("\nInvalid card number or PIN")
    return None, None


def deposit(card_number):
    for account in accounts:
        if account['cardNumber'] == card_number:
            amount = float(input("Enter the deposit amount: "))
            account['balance'] += amount
            print("\nDeposit successful!")
            return card_number, account['balance'], amount

    print("\nInvalid card number!")
    return None, None, None


def withdraw(card_number):
    for account in accounts:
        if account['cardNumber'] == card_number:
            amount = float(input("Enter the withdrawal amount: "))
            if amount <= account['balance']:
                account['balance'] -= amount
                print("\nWithdrawal successful!")
                return card_number, account['balance'], amount

    print("\nInvalid card number!")
    return None, None, None


def check_balance():
    card_no, status = verify_account()
    if card_no is not None:
        for account in accounts:
            if account['cardNumber'] == card_no:
                return account['balance']
    return None


def find_details(cardNumber):
    for account in accounts:
        if account['cardNumber'] == cardNumber:
            print("\nAccount Name:", account['accountName'])
            print("Balance:", account['balance'])
            print("Status:", account['status'])
            print("Card Number:", account['cardNumber'])
            print()


def all_account():
    for acc in accounts:
        print("Account Name:", acc['accountName'])
        print("Balance:", acc['balance'])
        print("Status:", acc['status'])
        print("Card Number:", acc['cardNumber'])
        print()


def add_account():
    accountName = input("Enter account name: ")
    balance = float(input("Enter balance: "))
    cardNumber = int(input("Enter card number: "))
    pin = int(input("set pin: "))
    accounts.append({
        'accountName': accountName,
        'balance': balance,
        'status': "active",
        'cardNumber': cardNumber,
        'pin': pin
    })
    print("\nAccount added successfully!")


def change_pin():
    cardNumber = int(input("Enter card number: "))
    balance = float(input("Enter balance: "))
    for account in accounts:
        if account['cardNumber'] == cardNumber and account['balance'] == balance:
            pin = int(input("Enter new pin: "))
            account['pin'] = pin
            print("\nPin changed successfully!")
            break
    else:
        print("\nCant identify!")


print("\nThank you for using our service!")
