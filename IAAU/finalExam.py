# def sumN(n):
#     '''
#     Recursive function that sums up all numbers untill the given one
#     n: int
#     returns -> int
#     '''
#     if n == 0:
#         return n
#     return sumN(n-1) + n
# n = int(input('Enter your number: '))
# print(sumN(n))

with open('dictionary.txt','r') as words: words = words.read()
words = words.split('\n')
print(words)
for word in range(len(words)):
    words[word] = words[word].split(':')
dictionary = {}
try:
    for pair in words:
        dictionary[pair[0]] = pair[1]
except: print(dictionary)
userWord = input('Your word? ')
for englishWord in dictionary:
    if userWord == englishWord: print(dictionary[englishWord])
    elif userWord == dictionary[englishWord]: print(englishWord)

# userNum = int(input())
# def fromZeroTo(n):
#     '''
#     Recursive function that gives you all numbers from 0 to given
#     n: int
#     returns -> tuple
#     '''
#     if n == 0:
#         return (n,)
#     return fromZeroTo(n-1) + (n,)
# userInput = int(input('Your number: '))
# print(fromZeroTo(userInput))
# nums = []
# userNum = int(input())
# def fromZeroTo(n):
#     if n == userNum:
#         return nums
#     return fromZeroTo(n+1) nums.append(n-5)
# print(fromZeroTo(userNum))
