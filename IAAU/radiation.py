import math

def f(x): 
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExp(start, stop, step):
    sum = 0
    for i in range(int((stop-start)/step)): 
        sum += f(start+i*step)
        print((start+i*step))
    return sum
print(radiationExp(0, 11, 1))

# def radiationExp(start, stop, step):
#     sum = 0
#     for i in range(start,stop,int(step)):
#         i*=step
#         sum+=f(i)
#     return sum
# print(radiationExp(40, 100, 1.5))