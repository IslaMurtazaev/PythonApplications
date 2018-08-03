import string

# Recursion

def mult(a, b):
    if b == 1: # BASE CASE
        return a
    return mult(a, b-1) + a

def factorial(n):
    if n == 1:
        return n
    return factorial(n-1) * n

# NOTE use induction method to prove that your algorithm works properly

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2) # two function calls at a time 

def palindrome(w):
    def isChar(w):
        w, result = w.lower(), ''
        for l in w:
            if l in string.ascii_lowercase: result += l 
        return result

    def isPal(result):
        if len(result) <= 1:
            return True
        return result[0] == result[-1] and isPal(result[1:-1])
    return isPal(isChar(w))

# def palindrome(result):
#     if len(result) == 1 or len(result) == 2 and result[0] == result[-1]:
#         return True
#     elif result[0] != result[-1]:
#         return  False
#     return palindrome(result[1:len(result)-1])

# Dictionaries

def check(word):
    if len(word) == 0: return word
    else: return check(word[:-1]) + word[-1] if word[-1].lower() in string.ascii_lowercase else check(word[:-1])

def lyricsToFrequencies(lyrics):
    lyricsDict, lyrics = {}, lyrics.split()
    for word in lyrics:
        if check(word) in lyricsDict: lyricsDict[word] += 1
        else: lyricsDict[check(word)] = 1
    return lyricsDict

def mostCommonWords(freqs):
    ordFreqs, values, best = [], freqs.values(), max(freqs.values())
    for k in freqs:
        if freqs[k] == best:
            ordFreqs.append(k)
    return (ordFreqs, best)

def fibEfficient(n, d):
    if n in d:
        return d[n]
    else:
        d[n] = fibEfficient(n-1, d) + fibEfficient(n-2, d)
        # d[n] = ans
        return d[n]
d = {1:1, 2:2}
print(fibEfficient(100, d))
# print(fibonacci(100))