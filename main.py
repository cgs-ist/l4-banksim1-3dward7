accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'

while True:
    print('\nPress b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account details')
    print('Press q to quit\n')
    
    action = input("What do you want to do? ").lower()[0]
    
    if action == 'b':
        print('Get Balance:')
        userPassword = input('Please enter your password: ')
        if userPassword != accountPassword:
            print('Incorrect Password')
        else:
            print('Your balance is: ', accountBalance)
    
    elif action == 'd':
        print('Make Deposit:')
        userPassword = input('Please enter your password: ')
        if userPassword == accountPassword:
            amount = float(input('Enter the amount to deposit: '))
            if amount > 0:
                accountBalance += amount
                print(f'{amount} has been deposited. New balance is: {accountBalance}')
            else:
                print('Invalid amount, deposit failed.')
        else:
            print('Incorrect Password')
    
    elif action == 'w':
        print('Make Withdrawal:')
        userPassword = input('Please enter your password: ')
        if userPassword == accountPassword:
            amount = float(input('Enter the amount to withdraw: '))
            if 0 < amount <= accountBalance:
                accountBalance -= amount
                print(f'{amount} has been withdrawn. New balance is: {accountBalance}')
            else:
                print('Invalid amount or insufficient funds, withdrawal failed.')
        else:
            print('Incorrect Password')
    
    elif action == 's':
        print('Show Account Details:')
        userPassword = input('Please enter your password: ')
        if userPassword == accountPassword:
            print(f'Account Name: {accountName}')
            print(f'Account Balance: {accountBalance}')
        else:
            print('Incorrect Password')
    
    elif action == 'q':
        print('Exiting...')
        break  # Exit the while loop, ending the program
    
    else:
        print('Invalid action. Please select another option.')
