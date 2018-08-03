n = 1
pos = []
neg = []
try:
    while n is not float:
        n = int(input())
        if n == 0:
            pass
        elif n > 0:
            pos.append(n)
        elif n < 0:
            neg.append(n)
except:
    print('There are '+str(len(pos))+' positive and '+str(len(neg))+' negative numbers entered.')


def prime(n):
    '''
    int -> str
    checks if the given number is prime
    '''
    c = 0
    isPrime = 'Not prime'
    if n <= 1:
        return isPrime
    for i in range(1,n):
        if n % i == 0:
            c+=1
    if c <=1:
        isPrime = 'Prime'
    return isPrime



def powerRec(b,e, i =1, result =0):
    if result < b:
        result = b
    if i >= e or e <= 1:
        return result
    return powerRec(b,e, i+1, result*b)
print(powerRec(1,5))
