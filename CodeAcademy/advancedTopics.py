# my_dict = {'name':'Facebook', 'price':1000}
# print(my_dict.keys())
# print(my_dict.values())
# for key in my_dict:
#     print(key,my_dict[key],sep = '->')
#     print(key,my_dict[key],end = '->')



# odds_to50 = [i for i in range(51) if i % 2 ==1]
# print(odds_to50)
# doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
# print(doubles_by_3)
# even_squares = [(i**2) for i in range(1,12) if (i**2) % 2 == 0]
# print(even_squares)
# cubes_by_four = [(i**3) for i in range(1,11) if (i**3) % 2 == 0]
# print(cubes_by_four)
# evenList = [i for i in range(2,51,2)]
# print(evenList)

# to_21 = [i for i in range(1,22)]
# odds = to_21[::2]
# middleList = ((len(to_21))//2-1)
# middle_third = to_21[middleList-1:middleList+2]
# print(middle_third)

# number = 123456789
# digitsList = [int(i) for i in str(number)]
# print(sum(digitsList))

# my_list = range(50)
# odds = list(filter(lambda i: i % 2==1, my_list))
# evens = list(filter(lambda i: i % 2 ==0, my_list)) 

# squares = [(x**2) for x in range(1,11)]
# print(list(filter(lambda x: x >= 30 and x <= 70, squares)))

# C = [39.2, 36.5, 37.3, 38, 37.8] 
# F = list(map(lambda x: (float(9)/5)*x + 32, C))
# print(F)
# C = list(map(lambda x: (float(5)/9)*(x-32), F))
# print(C)

# movies = {
#   "Monty Python and the Holy Grail": "Great",
#   "Monty Python's Life of Brian": "Good",
#   "Monty Python's Meaning of Life": "Okay"
# }
# print(movies.keys())
# print(movies.values())
# print(movies.items())

# threes_and_fives = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, [x for x in range(1,16)]))
# print(threes_and_fives)
import random
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = ''.join(filter(lambda x: x != 'X', garbled))

# def enigma(st):
#     st = list(st)
#     length = len(st)
#     xTime = random.randint(1,5)
#     for i in length:
#         st.insert((random.randint(0, length), ('X'*xTime))
#     return st
# print(enigma('AUCA sucks my dick hard everyday!'))
st = 'AUCA sucks my dick hard everyday!'
st = list(st)
length = len(st)
xTime = random.randint(1,3)
for i in range(length):
    st.insert(random.randint(xTime, length), ('X'*xTime))
st = (''.join(st))
print(st)
message = ''.join(filter(lambda x: x != 'X', st))
print(message)