def areaOf():
    figure = input('Area of (C)ircle or area of R(ectangle)? ').upper()
    if figure == 'C':
        r = int(input('Enter a radius: '))
        area = 3.14*r**2
        return 'Area of circle is ' + str(area)
    elif figure == 'R':
        w = int(input('Enter a width: '))
        h = int(input('Enter a hight: '))
        area = w * h
        return 'Area of rectangle is ' + str(area)

def rootOf():
    '''
    int OR float
    int OR float
    int OR float -> int OR float and int OR float
    that calculates the roots of quadratic equation
    '''
    try:
        a = int(input())
        b = int(input())
        c = int(input())
    except:
        return "It's not quadratic equation."
    delta = b ** 2 - 4 * a * c
    x1 = (b + (b**2 - delta)**.5)/2
    x2 = (b - (b**2 - delta)**.5)/2
    return round(x1, 2), round(x2, 2)

def factorial():
    '''
    returns a factorial of a given number
    '''
    result = 1
    try:
        n = int(input())
    except:
        return 'error'
    if n < 0:
        return 'error'
    else:
        for i in range(n):
            result *= (i+1)
        return result

def fibo(n, fiboList = [1,1]):
    '''
    int -> list
    returns a list of fibbonachi number till the given number
    '''
    fib = 0
    for i in range(n-2):
        fib = fiboList[i] + fiboList[i+1]
        fiboList.append(fib)
    return fiboList

def powerSeries(stopNum):
    '''
    int -> int
    returns a power series of "(-1)**(i+1)/(2*i-1)" till a given number
    '''
    sum = 0
    for i in range(1,stopNum):
        sum += (-1)**(i+1)/(2*i-1)
    return sum*4

