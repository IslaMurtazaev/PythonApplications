# for n in range(0,1000):
#     if n % 2 == 0:
#         print(n, end = " ") # end " " == spaces between numbers


# for n in range(2,60,4): # start, stop, divisor(every fourth number)
#     print(n)
# for n in range(1,20,2): # start, stop, divisor(every second number)
#     print(n)


# for n in range(4,1,-1): # backwards (start, stop, substractor)
#     print(n)


# for letter in "hello":
#     print(letter, end = "")
# s = "hello"
# for index in range(len("hello")): # to get every odd letter 
#     if index % 2 ==0:
#         print(s[index], end = "")


# numbers = []
# sum = 0
# for n in range(1, 101):
#     sum += n
#     numbers.append(n)
# print(sum / len(numbers))

# for i in range(100):
#     if i % 3 == 0: # skippes every number that is divisible by three
#         continue
#     else:
#         print(i)

# continue # skip the this one and go on
# pass # doesn't do anything
# break # exit
# for b in range(10):
#     for i in range (10):
#         for k in range(10):
#             print(k, end = ' ')
#         print()
#     print()



# number = int(input("Your number: "))
# divisible = []
# for numb in range(number + 1):
#     if number < 1:
#         print("Incorrect input!")
#     elif numb % 5 == 0 or numb % 7 == 0:
#         if numb == 0:
#             continue
#         else:
#             divisible.append(str(numb))
# print(",".join(divisible))
# print("There are "+ str(len(divisible)) +" numbers divisible by 5 or 7.")



# userLetter = input("Your letter is: ").lower()
# helloWorld = "helloworld!"
# for letter in range(len(helloWorld)):
#     if helloWorld[letter] == userLetter:
#         print("Hello")
#         break
# else: 
#     print("Bye")



userNumber = int(input("Your number is: "))
counter = 1
number = 1
squaredNumbers = []
if userNumber < 0:
    userNumber *= (-1)
elif userNumber == 0:
    squaredNumbers.append(0)
while userNumber >= counter:
    squaredNumbers.append(number ** 2)
    counter += 1
    number += 1
print(squaredNumbers)
