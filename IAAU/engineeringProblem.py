# alphabet = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',\
# 13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}



# userInput = input('Enter a string: ').lower()
# vowels = ['a', 'e', 'i', 'o', 'u']
# counter = 0
# for letter in userInput:
#     for vowel in vowels:
#         if vowel == letter:
#             counter += 1
# print('Number of vowels: ' + str(counter))


'''
counts unique string in a big string
bc'''
# userInput = input('Enter a string: ').lower() 
# counter = 0 
# for index in range(len(userInput)):
#      if index+3 > len(userInput):
#          break
#      if userInput[index] == 'b':
#          if userInput[index+1] == 'o':
#              if userInput[index+2] == 'b':
#                  counter += 1
# print('Number of times "bob" occurs is: ' + str(counter))



##userStr = input('Enter your string: ')
##subStr = ''
##longStr = ''
##for i in range(len(userStr)):
##    if i +1 >= len(userStr):
##        break
##    elif userStr[i] <= userStr[i+1]:
##        subStr += userStr[i]
##    else:
##        if userStr[i-1] <= userStr[i]:
##            subStr += userStr[i]
##        if len(longStr) < len(subStr):
##            longStr = subStr
##        subStr = ''
##print('Longest substring in alphabetical order is: '+longStr)
##    


print(sum([x for x in range(1,10)]))