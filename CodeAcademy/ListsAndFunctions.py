# n = [3, 5, 7]

# for i in range(0, len(n)):
#   n[i] = n[i] * 2
 
# def double_list(x):
#   for i in range(len(x)):
#   	x[i] = x[i] * 2
#   return x
# print(double_list(n))

# range(6) # => [0, 1, 2, 3, 4, 5]
# range(1, 6) # => [1, 2, 3, 4, 5]
# range(1, 6, 3) # => [1, 4]
# The range function has three different versions:
# range(stop)
# range(start, stop)
# range(start, stop, step)

# # Method 1 - for item in list: # for looping through a list, but not changing it
# for item in list:
#   print item


# # Method 2 - iterate through indexes: # looping through a list using indexes, to modify it
# for i in range(len(list)):
#   print list[i]


# n = [3, 5, 7]   # getting total of numbers in a list
# def total(numbers):
#   result = 0
#   for i in range(len(numbers)):
#     result += numbers[i] 
#   return result
# print(total(n))



# n = ["Michael", "Lieberman"] # joining strings from a list
# def join_strings(words):
#   result = ""
#   for word in range(len(words)):
#     result += words[word]
#     result += " "
#   return result
# print(join_strings(n))



# m = [1, 2, 3] # adding two lists together
# n = [4, 5, 6]
# def join_lists(x, y):
#   return x + y
# print join_lists(m, n)



# n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]  
# def flatten(lists): # concatenate all sublists in list to a single one
#   results = []
#   for numbers in lists:
#     for number in numbers:
#       results.append(number)
#   return results
# print(flatten(n))


# def reverse(text): # gives us a reverse of a string
#   result = text[::-1]
#   return result
# print(reverse("abcd"))



# def reverse(text): # gives us a reverse of a string
#   result = ""
#   counter = 1
#   for letter in text:
#     result += text[len(text) - counter]
#     counter += 1
#   return result
# print(reverse("abcd"))



# def anti_vowel(text): # removes all vowels from string
#   result = ""
#   for letter in text:
#     if letter.lower() == "a" or letter.lower() == "e" or letter.lower() == "i" or\
#      letter.lower() == "o" or letter.lower() == "u":
#       continue
#     else:
#       result += letter
#   return result
# print(anti_vowel("My name is Islam)"))