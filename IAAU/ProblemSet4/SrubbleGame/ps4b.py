from ps4a import *
import time

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    maxScore = 0
    bestWord = None
    for word in wordList:
        if isValidWord(word,hand,wordList) == True:
            if maxScore < getWordScore(word, n):
                maxScore = getWordScore(word, n)
                bestWord = word
    return bestWord

def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    totalScore = 0
    while compChooseWord(hand, wordList, n) != None:
        score = 0
        print('Current Hand:', displayHand(hand))
        bestWord = compChooseWord(hand, wordList, n)
        score += getWordScore(bestWord, n)
        totalScore += score
        print('"%s" earned %d points. Total: %d points.' %(bestWord, score, totalScore))
        hand = updateHand(hand, bestWord)
        if compChooseWord(hand, wordList, n) == None and calculateHandlen(hand) == 0: 
            print('Total score: %d points.' %totalScore)
        print()
    if calculateHandlen(hand) > 0: 
        print('Current Hand:', displayHand(hand))
        print('Total score: %d points.' %totalScore)

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    userTurn = None
    while userTurn != 'e':
        userTurn = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if userTurn == 'e': break
        elif userTurn == 'n':
            userOrComp = input('Enter u to have yourself play, c to have the computer play: ')
            lastHand = dealHand(7)
            if userOrComp == 'u': playHand(lastHand, wordList, 7)
            elif userOrComp == 'c': compPlayHand(lastHand, wordList, 7)
            else: print('Invalid command.')
        elif userTurn == 'r':
            userOrComp = input('Enter u to have yourself play, c to have the computer play: ')
            if userOrComp == 'u': 
                try: playHand(lastHand, wordList, 7)
                except: print('You have not played a hand yet. Please play a new hand first!')
            elif userOrComp == 'c': 
                try: compPlayHand(lastHand, wordList, 7)
                except: print('You have not played a hand yet. Please play a new hand first!')
            else: print('Invalid command.')
        else: print('Invalid command.')
        print()

if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)