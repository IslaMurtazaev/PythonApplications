# lloyd = {
#   "name": "Lloyd",
#   "homework": [90.0, 97.0, 75.0, 92.0],
#   "quizzes": [88.0, 40.0, 94.0],
#   "tests": [75.0, 90.0]
# }
# alice = {
#   "name": "Alice",
#   "homework": [100.0, 92.0, 98.0, 100.0],
#   "quizzes": [82.0, 83.0, 91.0],
#   "tests": [89.0, 97.0]
# }
# tyler = {
#   "name": "Tyler",
#   "homework": [0.0, 87.0, 75.0, 22.0],
#   "quizzes": [0.0, 75.0, 78.0],
#   "tests": [100.0, 100.0]
# }

# students = [lloyd, alice, tyler]
# # for student in students:
# #   print(student['name'])
# #   print(student['homework'])
# #   print(student['quizzes'])
# #   print(student['tests'])



# def average(numbers):
#   quantity = len(numbers)
#   total = sum(numbers)
#   result = float(total) / quantity
#   return result
# average(alice["tests"])



# def get_average(student):
#   homework = average(student['homework'])
#   quizzes = average(student['quizzes'])
#   tests = average(student['tests'])
#   homework *= 0.1
#   quizzes *= 0.3
#   tests *= 0.6
#   result = homework + quizzes + tests
#   return result
# # get_average(alice)



# def get_letter_grade(score):
#   if score >= 90:
#     return 'A'
#   elif score >= 80:
#     return 'B'
#   elif score >= 70:
#     return 'C'
#   elif score >= 60:
#     return 'D'
#   else:
#     return 'F'



# def get_class_average(class_list):
#   results = []
#   for student in class_list:
#   	results.append(get_average(student))
#   return average(results)
# print(get_class_average(students))
# print(get_letter_grade(get_class_average(students)))




# score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
#          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
#          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
#          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
#          "x": 8, "z": 10}
# def scrabble_score(word = input().lower()):
#   totalScore = 0
#   for str1 in word:
#     for letter in score:
#       if str1 == letter:
#         totalScore += score[letter]
#   return totalScore
# print(scrabble_score())




def censor(text, word):
  text = list(text)
  
censor('Hey you sun of a freak!', 'freak')
        




