import random

def greetings():
    print('Let’s play a game called “Odds and Evens”')
    userName = input('What is your name? ')
    return userName

def userMode():
    mode = input('Hi %s, which do you choose? (O)dds or (E)vens? ' %userName).lower()
    while mode != 'o' and mode != 'e':
        print('Invalid input')
        mode = input('Which do you choose? (O)dds or (E)vens? ').lower()
    if mode == 'o': print('%s has picked odds! The computer will be evens.' %userName)
    elif mode == 'e': print('%s has picked evens! The computer will be odds.' %userName)
    print('-------------------------------------')
    return mode

def gameBody():
    userNum = int(input('How many “fingers” do you put out? '))
    compNum = random.randint(0,5)
    print('The computer plays %d “fingers”.' %compNum)
    print('-------------------------------------')
    summ = userNum + compNum
    print('%d + %d = %d' %(userNum, compNum, summ))
    if summ % 2 == 0: oddOrEven = 'even'
    else: oddOrEven = 'odd'
    print('%d is ...%s' %(summ, oddOrEven))
    print('-------------------------------------')
    return oddOrEven

def whoWon():
    if mode == 'o':
        if oddOrEven == 'odd': print('That means %s wins! :)' %userName)
        else: print('That means %s loses :(' %userName)
    elif mode == 'e':
        if oddOrEven == 'even': print('That means %s wins! :)' %userName)
        else: print('That means %s loses :(' %userName)
    print('-------------------------------------')

if __name__ == '__main__':
    userName = greetings()
    mode = userMode()
    oddOrEven = gameBody()
    whoWon()