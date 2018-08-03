import string
import random

# NOTE this program uses words.txt 

def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if i not in lettersGuessed: return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    secretWord = list(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed: secretWord[i] = '_ '
    return ''.join(secretWord)

def getAvailableLetters(lettersGuessed):
    availableLetters = ''
    for i in string.ascii_lowercase:
        if i not in lettersGuessed: availableLetters +=i
    return availableLetters

def start():
    print('Loading word list from file...')
    with open('words.txt', 'r+') as words:
        secretWord = random.choice(words.read().split(' '))
    with open('words.txt', 'r') as words:
        print(str(len(words.read().split(' ')))+' words loaded.')
    return secretWord

def hangman(secretWord):
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is %d letters long.' %len(secretWord))
    guesses = 8
    lettersGuessed = ''
    while guesses != 0:
        print('-------------')
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('Congratulations, you won!')
            break
        print('You have %d guesses left.' %guesses)
        print('Available letters: '+getAvailableLetters(lettersGuessed))
        userGuess = input('Please guess a letter: ')
        if userGuess in lettersGuessed:
            print("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed))
        elif userGuess in secretWord:
            lettersGuessed += userGuess
            print('Good guess! '+getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += userGuess
            print('Oops! That letter is not in my word: '+getGuessedWord(secretWord, lettersGuessed))
            guesses -= 1
    print('-------------')
    if guesses == 0:
        print('Sorry, you ran out of guesses. The word was %s.' %secretWord)
hangman(start())