# webster = {
#   "Aardvark" : "A star of a popular children's cartoon show.",
#   "Baa" : "The sound a goat makes.",
#   "Carpet": "Goes on the floor.",
#   "Dab": "A small amount."
# }
# for key in webster:# looping through dictionaries
#   print(webster[key])



# def fizz_count(x): # looping through lists
#   fizzCount = 0
#   NonFizzCount = 0
#   for item in x:
#     if str(item).isalpha() == True:
#       pass
#       if item.lower() == "fizz":
#         fizzCount += 1
#       else:
#         NonFizzCount += 1
#     else:
#       NonFizzCount += 1
#   print('The list\'ve got ' +str(fizzCount)+ ' fizzs')
#   print('And '+str(NonFizzCount)+' non fizzs')

# fizzList = ['fizz', 7, 'Fizz', 12.5, 'fix', 'FIZZ', 'fidz', 1]

# fizz_count(fizzList)



# price = {"banana": 4,
# "apple": 2,
# "orange": 1.5,
# "pear": 3}

# stock = {"banana": 6,
# "apple": 0,
# "orange": 32,
# "pear": 15}

#  # looping through dictionaries
# for fruit in price:
#   print(fruit)
#   print("price: %s" % price[fruit])
#   print("stock: %s" % stock[fruit])




# prices = {
#   "banana" : 4,
#   "apple"  : 2,
#   "orange" : 1.5,
#   "pear"   : 3,
# }
# stock = {
#   "banana" : 6,
#   "apple"  : 0,
#   "orange" : 32,
#   "pear"   : 15,
# }

# for key in prices:
#   print( key)
#   print( "price: %s" % prices[key])
#   print( "stock: %s" % stock[key])
  
# total = 0
# for fruit in prices:
#   money = prices[fruit] * stock[fruit]
#   print("benefit from "+ str(fruit)+ " will be "+ str(money))
#   total += money
# print("Total outcome is %.2f" %total)

# def compute_bill(food):
#   total = 0
#   for item in food:
#     if stock[item] > 0:
#       total += prices[item]
#       stock[item] = stock[item] - 1
#   print(total)

# compute_bill(prices)




# import random
# print "Lucky Numbers! 3 numbers will be generated."
# print "If one of them is a '5', you lose!"

# count = 0
# while count < 3:
#   num = random.randint(1, 6)
#   print num
#   if num == 5:
#     print "Sorry, you lose!"
#     break
#   count += 1
# else:
#   print "You win!"



# from random import randint
# # Generates a number from 1 through 10 inclusive
# random_number = randint(1, 10)
# guesses_left = 3
# while guesses_left > 0:
#   guess = int(input("Your guess: "))
#   if guess == random_number:
#     print("You win!")
#     break
#   guesses_left -= 1
# else:
#   print("You lose.")



# hobbies = []
# for hobby in range(3):
#   hobby = input("What is your hobby? ")
#   hobbies.append(hobby)
# print(", ".join(hobbies))



# phrase = "A bird in the hand..."
# # Add your for loop
# for char in phrase:
#   if char == 'A' or char == 'a':
#     print("X", end = "")
#   else:
#   	print(char, end = "")



# d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'} # looping through a dictionary
# for key in d:
#   # Your code here!
#   print(key,)
#   print(d[key])



# choices = ['pizza', 'pasta', 'salad', 'nachos']
# print('Your choices are:')
# for index, item in enumerate(choices):  # shows an index of an item 
#   print(index +1, item)



# list_a = [3, 9, 17, 15, 19]
# list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
# for a, b in zip(list_a, list_b): # built-in-function to compare several lists
#   if a > b:
#     print(a)
#   elif b > a:
#     print(b)



# guests = ['Atai', 'Argen', 'Kylymbek', 'Aktan']
# for guest in guests:
#   if guest == 'Islam':
#     print("Hey Islam!")
# else:
#   print("Where is Islam?")



# userNumber = int(input("Your number: "))
# counter = 0
# exponent = 0
# number = 2
# result = 0
# while userNumber >= counter:
#     number = 2 ** exponent
#     counter += 1
#     exponent += 1
#     result += number 
# print("The sum is " + str(result) + ".")