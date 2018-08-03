# meal_cost = float(input("What is your total meal cost? "))

# def tax(bill):
#   """Adds 8% tax to a restaurant bill."""
#   bill *= 1.08
#   print("With tax: %.2f" % bill)
#   return bill

# def tip(bill):
#   """Adds 15% tip to a restaurant bill."""
#   bill *= 1.15
#   print("With tip: %.2f" % bill)
#   return bill
  
# meal_with_tax = tax(meal_cost)
# meal_with_tip = tip(meal_with_tax)



# def square(n):
#   """Returns the square of a number."""
#   squared = n ** 2
#   print("%d squared is %d." % (n, squared))
#   return squared
  
# # Call the square function on line 10! Make sure to
# # include the number 10 between the parentheses.
# square(10)



# import math
# print(math.sqrt(25))
# # or
# # from module import function 
# # function
# # or 
# # from module import *
# # both will not need to write "math.bla bla bla"
# from math import sqrt 
# sqrt(12)



# def hotel_cost(nights):
#     return 140 * nights

# def plane_ride_cost(city):
#     if city == "Charlotte":
#         return 183
#     elif city == "Tampa":
#         return 220
#     elif city == "Pittsburgh":
#         return 222
#     elif city == "Los Angeles":
#         return 475
  
# def rental_car_cost(days):
#     cost = days * 40
#     if days >= 7:
#         cost -= 50
#     elif days >=3:
#       cost -= 20
#     return cost

# def trip_cost(city, nights, days):
#     print("Your total trip cost is $" + str(plane_ride_cost(city) + rental_car_cost(nights) +\
#  hotel_cost(days)))

# def main():
#     nights = int(input("How many nights you are gonna stay at the hotel? "))
#     city = input("Which city you are gonna fly? ")
#     days = int(input("How many days you are gonna rent the car? "))
#     hotel_cost(nights)
#     plane_ride_cost(city)
#     rental_car_cost(days)
#     trip_cost(city, nights, days)

# main()



# def fizz_count(x): # x is a list
#   count = 0
#   for item in x:
#     if item == "fizz":
#       count += 1
#   return count




# def censor(text, word):
#   censor = ''
#   for step in range(len(word)):
#     censor += '*'
#   text = text.replace(word, censor)
#   return text  
# print(censor('hello bitches!', 'bitch'))



# def censor(text, word):
#   text = list(text)
#   for index in range(len(text)):
#     if text[index:(index+4)] == list(word):
#       text[index:len(word)] = '*' *len(word)
#   return ''.join(text)
# print(censor('hello my dear friend', 'hell'))



# def median(listt):
#   listt = sorted(listt)
#   if len(listt) == 1:
#     median = listt[0]
#   else:
#     median = (listt[0] + listt[len(listt) - 1])/ 2
#   return median
# print(median([4, 5, 5, 4]))



grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance / len(scores)
print(grades_variance(grades))

def grades_std_deviation(variance):
  return variance ** 0.5
variance = grades_variance(grades)
print(grades_std_deviation(variance))