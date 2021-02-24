import curses
import json

file = 'D:\cfrbackup-LLGBPKSV\Whitehatjr\Python Classes\C-100-Project/CardandPin.json'


def input_(message, number):
    try:
        stdscr = curses.initscr()
        stdscr.clear()
        stdscr.addstr(message)
        amt = stdscr.getstr(1, 0, number)
    except:
        raise
    finally:
        curses.endwin()
    return amt


def details():
    card = 0
    pin = 0

    while True:
        try:
            card = int(input_('Enter your card number: ', 16))
            break
        except:
            print('Enter your card number without any spaces.')
            continue
    while True:
        try:
            pin = int(input_('Enter the pin to your card: ', 4))
            break
        except:
            print('Enter your pin number')
            continue

    return (card, pin)


def login():
    Details = details()
    file1 = open(file, 'r')
    data = str(json.load(file1))
    if str(Details[0]) in data:
        return (True, Details[0], Details[1])
    else:
        print('User does not exist')
        exit()


def signUp():
    Details = details()
    name = input('Enter your name: ')
    file1 = open(file, 'r+')
    data = json.load(file1)
    if str(Details[0]) in data:
        print('User already exist.')
        exit()
    else:
        appendData = {name: {"card": Details[0], "pin": Details[1]}}
        data.update(appendData)
        file1.seek(0)
        json.dump(data, file1)
        return (True, Details[0], Details[1])


def show():
    # print('For Card Details press `1`\nFor Balance Enquiry press `2`\nFor Cash Withdrawl press `3`\nPress `4` to exit')
    userInput = input(
        'For Card Details press `1`\nFor Balance Enquiry press `2`\nFor Cash Withdrawl press `3`\nPress `4` to exit\n')
    return userInput


class ATM():
    def __init__(self):

        loginOrSignUp = input('For sign up press `1`. For login press `2`: ')
        true = ''
        if loginOrSignUp == '2':
            login1 = login()
            true = login1[0]
            self.card = login1[1]
            self.pin = login1[2]
        elif loginOrSignUp == '1':
            signUp1 = signUp()
            true = signUp1[0]
            self.card = signUp1[1]
            self.pin = signUp1[2]
        else:
            print('Enter number 1 or 2.')
            exit()

        if true == True:
            show1 = show()
            while True:
                if show1 == '1':
                    print(f'Card Number: {self.card}\nCard Pin: {self.pin}')
                    show1 = show()
                elif show1 == '2':
                    print('You requested for Balance Enquiry')
                    show1 = show()
                elif show1 == '3':
                    print('You requested for Cash Withdrawl')
                    show1 = show()
                elif show1 == '4':
                    exit()
                else:
                    print('Enter Numbers 1 to 4')
                    show1 = show()


atm = ATM()
