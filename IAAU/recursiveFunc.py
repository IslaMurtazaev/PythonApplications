# def print_recur(n=0):
#     if n == 5: # stop word
#         return 0
#     else:
#         print(n,end = ', ')
#         return print_recur(n+1)
# print_recur()




# def factorial_recur(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * factorial_recur(n-1)
# print(factorial_recur(5))




# def fibo_iter(n):
#     fiboList = [0, 1]
#     for i in range(2,n):
#         fiboList.append(fiboList[i-1] + fiboList[i-2])
#     return fiboList
# print(fibo_iter(10))




# def fiboRecur(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fiboRecur(n-1) + fiboRecur(n-2)
# print(fiboRecur(10))



# def power_rec(x, y):
#     if y == 1:
#         return 1
#     else:
#         return x * power_rec(x, y-1)
# print(power_rec(2,2))



# def sumList(ls):  # Prints sum of the list
#     if not ls:
#         return 0
#     return ls[0] + sumList(ls[1:])
# print(sumList([1,2,3,4,5,6,7,8,9,10]))



# def listSum(ls, result = 0):
#     if not ls:
#         return result
#     return listSum(ls[1:], result + ls[0])
# print(listSum([1, 3, 4, 5, 6]))



# def largestIter(userList):
#     maxN = 0
#     for i in userList:
#         if i > maxN:
#             maxN = i
#     print(maxN)
# largestIter([1,2,3,4,5,6,7,6,7])



# def sumDigits(n):
#     sum = 0
#     n = str(n)
#     n = list(n)
#     print(n)
#     for i in n:
#         sum += int(i)
#     print(sum)
# sumDigits(1234567)



# def sum_digits(n):
#     if n < 10:
#         return n
#     else:
#         all_but_last, last = n // 10, n % 10
#         return sum_digits(all_but_last) + last
# print(sum_digits(123456789))



# def listSum(ls, index=0, result=0):
#     # Base condition
#     if index == len(ls):
#         return result
#     # Call with next index and add the current element to result
#     return listSum(ls, index + 1, result + ls[index])
# print(listSum([1, 3, 4, 5, 6]))



# def largest(userList, result = 0):
#     if len(userList) <= 0:
#         print(result)
#         return 0 
#     else:
#         b = userList[0]
#         userList.remove(b)
#         if (result < b):
#             result = b
#         largest(userList, result)
# userList = input()
# largest()



# def greatestNum(ls, index = 0, result = 0):
#     if index == len(ls):
#         print(result)
#         return 
#     elif ls[index] > result:
#         result = ls[index]
#     return greatestNum(ls, index + 1, result)
# greatestNum([1, 3, 4, 5, 6])



# def reverseRec(ls, i = 0):
#     '''
#     list -> list
#     takes a list and returns its reversed version
#     '''
#     if i == len(ls):
#         print(ls)
#         return
#     else:
#         ls.insert(i, ls[len(ls) - 1])
#         del(ls[len(ls) - 1])
#     return reverseRec(ls, i + 1)
# reverseRec([1,2,3,4,5,6,7,8,9,10])



# def checkRec(ls, x, i = 0, result = False):
#     if i >= len(ls) or result == True:
#         return result
#     else:
#         if ls[i] == x:
#             result = True
#     return checkRec(ls, x, i + 1, result)
# print(checkRec(ls = list(input()), x = input()))



# def oddRec(ls, i = 0, result = []):
#     '''
#     list -> list
#     takes a list and returns a list of its items in odd positions
#     '''
#     if i >= len(ls):
#         return result
#     elif i % 2 == 0:
#         result.append(ls[i])
#     return oddRec(ls, i + 1, result)
# print(oddRec([1,2,3,4,5,6,7,8,9]))



# def totalRec(ls, i = 0, result = 0):
#     if i >= len(ls):
#         return result
#     else:
#         result += ls[i]
#     return totalRec(ls, i +1, result)
# print(totalRec([1,2,3,4,5,6,7,8,9]))



# def palindromeRec(word, i = 0, reversed = '', result = False):
#     '''
#     str -> boolean
#     tests whether a string is a palindrome
#     '''
#     length = len(word) // 2
#     if i >= length:
#         return result
#     elif word[i] == word[-(i+1)]:
#         reversed += word[i]
#     if word[:length:1] == reversed:
#         result = True
#     return palindromeRec(word, i +1, reversed, result)
# print(palindromeRec(word = input()))



def concatenateRec(ls, ls2, i=0):
    '''
    list
    list -> list
    concantenates two lists
    '''
    if i >= len(ls2):
        return ls.sort()
    else:
        ls.append(ls2[i])
    return concatenateRec(ls, ls2, i+1)
print(concatenateRec(ls = list(input()), ls2 = list(input())))



# def concatenateRec(ls, ls2, i=0):
#     '''
#     list
#     list -> list
#     concantenates two lists
#     '''
#     if i >= len(ls2):
#         return ls
#     else:
#         ls.append(ls2[i])
#     return concatenateRec(ls, ls2, i+1)
# print(concatenateRec(ls = sorted(['a','b','c']), ls2 = [1,2,3]))  



# def onAll(ls, i = 0, result = []):
#     if i >= len(ls) or len(result) > 19:
#         return result
#     elif (ls[i]**.5) % 1 == 0:
#         result.append(ls[i])
#     return onAll(ls, i+1, result)
# print(onAll([1,2,3,4,56,7,8,25,9,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,9,25,4,4,4,4]))



# def sum_digits(n, digList = []):
#     '''
#     int -> int
#     takes a number and returns sum of its digits
#     '''
#     if n < 10:
#         return digList
#     else:
#         all_but_last, last = n // 10, n % 10
#         digList.append(all_but_last)
#         return sum_digits(all_but_last, digList) + last
# print(sum_digits(n = int(input())))



# def rotateRec(ls, k, i = 0):
#     for i in range


# def listDigits(n):
    '''
    int -> int
    takes a number and returns a list of its digits
    '''
n = 12345
if list(n) == n:
    print(n)
    # return n
n = str(n)
print(list(n))
# return listDigits(n = list(n))
# x = str(152342)
# x = list(x)
# print(x)
# print(listDigits(12345)