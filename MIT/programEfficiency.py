''' NOTE: How to evaluate efficiancy of programs
        * Measure with time
        * Count operations
        * abstract notion of Order of Growth
'''
# Timing program

import time

d = {1:1, 2:2}
def fibEfficient(n, d = d):
    if n in d:
        return d[n]
    else:
        d[n] = fibEfficient(n-1, d) + fibEfficient(n-2, d)
        return d[n]

# t0 = time.clock()
# fibEfficient(100)
# tl = time.clock() - t0
# print('t = %f s' %tl)

# Counting operations

def factIter(n): # -> 3n + 2 
    '''assume n is an int >= 0'''
    answer = 1 # +1 oper
    while n > 1: # +1n oper
        answer *= n # +2n oper
        n -= 1 # +2n oper
    return answer # +1 oper

# ORDER OF GROWTH (the best way of measuring efficiency)

# We represent worst case asymprtoic by big "O" notation
# def factIter(n): # -> O(n)
#     '''assume n is an int >= 0'''
#     answer = 1 
#     while n > 1: 
#         answer *= n 
#         n -= 1 
#     return answer 

# Drop constants and multiplicative factors 
# Focus on dominant terms
''' NOTE Simplification examples: (Law of addition)
    n^2 + 2n + 2                => O(n^2)
    n^2 + 100n + 3^10000        => O(n^2)
    log(n) + n + 4              => O(n)
    0.001 * n * log(n) + 300n   => O(n log n )
    2n^30 + 3^n                 => O(3^n)
'''

''' NOTE Complexity classes:
    O(1) denotes constant running time 
    O(log n) denotes logarithmic running time
    O(n) denotes linear running time
    O(n log n) denotes log-linear running time
    O(n^c) denotes polynomial running time ("c" is a constant)
    O(c^n) denotes exponential running time("c" is const raised to a power based on size of input)
'''
# complexity => O(n) not O(log n) because we have to copy a list and call fnc again
def bisecSearch1(L, e):
    if len(L) == 0: return False
    elif len(L) == 1: return L[0] == e
    else: 
        half = len(L) // 2
        if L[half] == e: return True
        elif L[half] > e: return bisecSearch1(L[:half], e)
        elif L[half] < e: return bisecSearch1(L[half:], e) 

# complexity => O(log n)
def bisecSearch2(L, e):
    def bisecSearchHelper(L, e, low, high):
        if high == low: return L[0] == e
        mid = (high+low)//2
        if L[mid] == e: return True
        elif L[mid] > e:
            if low == mid: return L[0] == e
            else: return bisecSearchHelper(L, e, low, mid-1)
        else: return bisecSearchHelper(L, e, mid+1, high)
    if len(L) == 0: return False
    else: return bisecSearchHelper(L, e, 0, len(L))

# print(bisecSearch2([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], 9))

# O(log(i))
def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i //= 10
    return result
# print(intToStr(1234567890))

# exponential complexity (usually when fnc has two or more recursion calls)
def genSubsets(L):
    if len(L) == 0: return [[]]
    smaller = genSubsets(L[:-1]) # all subsets without the last element
    extra = genSubsets(L[-1:]) # creates a list with just of last element
    new = []
    for small in smaller:
        new.append(small+extra) # for all smaller solution, add one with last element
    return new # combine those with last element and those without
# print(genSubsets([1]))

def fibIter(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        fibI = 0
        fibII = 1
        for i in range(n+1):
            tmp = fibI
            fibI = fibII
            fibII = tmp + fibI
        return fibII


''' NOTE Complexity of common functions in python:
                LISTS:                        DICTS:
         index         O(1)                Worst case:                          
         store         O(1)         index              O(n)
         length        O(1)         store              O(n)
         append        O(1)         length             O(n) 
         ==            O(n)         delete             O(n) 
         remove        O(n)         iteration          O(n)      
         copy          O(n)               Average case:
         reverse       O(n)         index              O(1)            
         iteration     O(n)         store              O(1)
         in list       O(n)         length             O(1)   
                                    delete             O(1)                      
                                    iteration          O(1)   
'''