import msvcrt
import string
import os

# Lists of users, their PINs, and bank statements
users = ['user', 'user2', 'user3']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]
count = 0

# While loop checks existence of the entered username
while True:
    user = input('\nENTER USER NAME: ').lower()
    if user in users:
        n = users.index(user)
        break
    else:
        print('INVALID USERNAME')

# Comparing PIN
while count < 3:
    print('PLEASE ENTER PIN: ', end='', flush=True)
    pin = ''
    while True:
        key = msvcrt.getch()
        if key == b'\r':
            break
        elif key == b'\x08':
            if len(pin) > 0:
                pin = pin[:-1]
                print('\b \b', end='', flush=True)
        else:
            pin += key.decode('utf-8')
            print('*', end='', flush=True)

    if user == 'user':
        index = 0
    elif user == 'user2':
        index = 1
    else:
        index = 2

    if pin == pins[index]:
        break
    else:
        count += 1
        print('\nINVALID PIN')

# In case of three unsuccessful PIN attempts, exiting
if count == 3:
    print('3 UNSUCCESSFUL PIN ATTEMPTS, EXITING')
    print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
    exit()


print('LOGIN SUCCESSFUL, CONTINUE')
 
print()
 
print(str.capitalize(users[n]), 'welcome to ATM')
 
print('----------ATM SYSTEM-----------')

# Main menu and the rest of the code remains unchanged
# Main menu
while True:
 
    response = input('\nSELECT FROM FOLLOWING OPTIONS: \nBalanceStatement__(B) \nWithdraw___(W) \nDeposit__(D)  \nChange PIN_(P)  \nQuit_______(Q) \n: ').lower()
 

    if response == 'b':
        print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n],'RUPEE ON YOUR ACCOUNT.')
 
        
    elif response == 'w':
 
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
 
        if cash_out % 10 != 0:
 
            print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 RUPEE')
 
        elif cash_out > amounts[n]:
 
            print('YOU HAVE INSUFFICIENT BALANCE')
 
        else:
            amounts[n] = amounts[n] - cash_out
 
            print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEE')
 
            
    elif response == 'd':
        print()
 
        cash_in = int(input('ENTER AMOUNT YOU WANT TO DEPOSIT: '))
 
        print()
        if cash_in % 10 != 0:
 
            print('AMOUNT YOU WANT TO DEPOSIT MUST TO MATCH 10 RUPEE')
 
        else:
            amounts[n] = amounts[n] + cash_in
 
            print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEE')
 
            
    elif response == 'p':
 
        new_pin = input('ENTER A NEW PIN: ')
 
        if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
 
            new_ppin = input('CONFIRM NEW PIN: ')
 
            if new_ppin != new_pin:
 
                print('PIN MISMATCH')
 
            else:
                pins[n] = new_pin
                print('NEW PIN SAVED')
        else:
 
            print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
 
            
    elif response == 'q':
        exit()
    else:
 
        print('RESPONSE NOT VALID')
 
 
