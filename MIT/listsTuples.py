# TUPLES

# tup1 = ('MIT is the best!', 1, [], 'Yo!', 3)
# NOTE they are immutable (can't change elements' values)
# print(tup1)
# print(tup1[0])
# print(tup1[0:1])
# tup2 = ((1,'one'), (2, 'two'), (3, 'three'), (2, 'two'))
# def get_data(aTuple):
#     nums = ()
#     words = ()
#     for t in aTuple:
#         nums += (t[0],)
#         if t[1] not in words:
#             words += (t[1],)
#     minNum = min(nums)
#     maxNum = max(nums)
#     uniqueWords = len(words)
#     # NOTE you can return many objects using tuples
#     return (minNum, maxNum, uniqueWords)
# (minNum, maxNum, uniqueWords) = get_data(tup2)
# print('Your tuple\'s minimal and maximal numbers are',minNum,'and '+str(maxNum)+', also it has',\
# uniqueWords,'unique words')


# LISTS

# ls1 = [0,1]
# ls2 = [3,4]
# ls3 = ls1+ls2
# ls1.extend([2])
# print(ls1,ls2,ls3)
# ls3.append(2)
# print(ls3)
# sorted Doesn't mutate
# sort Mutates

# ALIASES

# warm = ['orange', 'red', 'yellow']
# hot = warm
# hot.append('pink')
# print(hot)
# print(warm)
# # NOTE side effect -> if you change one list the other one will change too
# if you don't want a side effect you should clone a list
# hot = warm[:]
# hot.append('pink')
# print(hot)
# print(warm)

def removeDups(ls1, ls2):
    for i in ls1.copy():
        if i in ls2:
            ls1.remove(i)
    return sorted(ls1+ls2)
print(removeDups([1,2,3,4,5,6,7,8], [1,2,3,4]))