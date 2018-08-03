# class Coordinates(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __str__(self, x, y):
#         return '<' + str(self.x) + '+' + str(self.y) + '>'
# point1 = Coordinates(5,5)
# point2 = Coordinates(6,6)
# origin = Coordinates(0,0)
# print(origin)



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printName(self):
        print(self.name)

    def bark(self):
        print('Get the hack out of here! Or you will deal with ' + str(self.name))

rocky = Dog('Rocky', 4)
rocky.printName()
rocky.bark()
