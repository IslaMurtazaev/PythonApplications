# OOP

import random

class Coordinates(object):
    def __init__(self, x, y): # self is like a name of instance (e.g. origin)
        self.x = x
        self.y = y
    def distance(self, other):
        xDiffSq = (self.x - other.x)**2
        yDiffSq = (self.x - other.x)**2
        return (xDiffSq + yDiffSq)**0.5
    def __str__(self): # makes print() much more informative, shows both parameters of instance
        return '<'+str(self.x)+','+str(self.y)+'>'

# c = Coordinates(3,4)
# origin = Coordinates(0,0)
# print(c.x)
# print(origin.y)
# print(c.distance(origin)) # conventional way
# print(Coordinates.distance(c,origin)) # second way that is equavalent
# print(c)
# print(type(c))
# print(isinstance(c, Coordinates)) # check if it's an instance of the class

# SPECIAL OPERATORS
# __add__(self, other) 'self + other'
# __sub__(self, other) 'self - other'
# __eq__(self, other) 'self == other' 
# __lt__(self, other) 'self < other'
# __len__(self) 'len(self)'
# __str__(self) 'print(self)' 
# and other...

class Fraction(object):
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
        assert type(self.num) == int and type(self.denom) == int

    def __str__(self):
        return str(self.num)+'/'+str(self.denom)

    def __add__(self, other):
        top = self.num * other.denom + self.denom * other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)

    def __sub__(self, other):
        top = self.num * other.denom - self.denom * other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)

    def __float__(self):
        return self.num/self.denom

    def inverse(self):
        return Fraction(self.denom, self.num)

a = Fraction(1,4)
b = Fraction(3,4)
c = a + b
print(float(c))
print(c)
# print(Fraction.__float__(c)) # exactly same result 
# print(float(b.inverse()))

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    # Getters are used in classes to return data attributes of instances
    def getAge(self):
        return self.age
    def getName(self):
        return self.name

    # Setters are used to set new data attributes to instances
    def setAge(self, newAge):
        self.age = newAge
    def setName(self, newName):
        self.name = newName

    # NOTE: Getters and Setters are used to prevent bugs in future

    def __str__(self):
        return self.name+' is '+str(self.age)+' years old' if self.name != None\
     else 'Animal is '+str(self.age)+' years old'

# dog = Animal(5)
# dog.setName('Rocky')
# print(dog)
# print(dog.age)
# print(dog.getAge())

'''
NOTE: We there are Parent classes(super classes) and Child classes(subclasses)
      Child classes inherit data and behaviors of their parent classes
      Child classes also can add more info, add more behavior, override behavior
'''

class Cat(Animal):
    def speak(self):
        print('meow')
    
    def __str__(self):
        return self.name+' is '+str(self.age)+' years old' if self.name != None\
     else 'Cat is '+str(self.age)+' years old'

# cat = Cat(2)
# cat.setName('Kisko')
# cat.setAge(3)
# print(cat)

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.setName(name)
        self.friends = []

    def getFriends(self):
        return self.friends

    def addFriend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print('Hello!')

    def ageDiff(self, other):
        return str(abs(self.age - other.age))+' year difference'

    def __str__(self):
        return self.name+' is '+str(self.age)+' years old' if self.age > 1\
     else self.name+' is '+str(self.age)+' year old'

# p1 = Person('Islam', 18)
# p1.addFriend('Nurti')
# p1.addFriend('Shaba')
# p1.addFriend('Dany')
# print(p1)
# print(p1.getFriends())
# p2 = Person('Nuri', 18)
# print(p2.ageDiff(p1))

class Student(Person):
    def __init__(self, name, age, major = None):
        Person.__init__(self, name, age)
        self.major = major

    def changeMajor(self, newMajor):
        self.major = newMajor

    def speak(self):
        r = random.random()
        if r < 0.25: print('I have homework')
        elif r < 0.5: print('I need sleep')
        elif r < 0.75: print('I should eat')
        else: print('I have to finish python')

    def __str__(self):
        return self.name+' is '+str(self.age)+' years old' if self.major == None\
     else self.name+' is '+str(self.age)+' years old, '+'studies '+self.major

student = Student('Islam', 18, 'CS')
student2 = Student('Iskhak', 20)
# print(student)
# print(student2)
print(student.getName(), 'says:', end=' ')
student.speak()
print(student2.getName(), 'says:', end=' ')
student2.speak()

# Class variables

class Rabbit(Animal):
    tag = 1 # Unique ID
    def __init__(self, age, parent1 = None, parent2 = None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag+=1
    
    def getRid(self):
        return str(self.rid).zfill(3)
    def getParent1(self):   
        return self.parent1
    def getParent2(self):
        return self.parent2

    def __add__(self, other):
        return Rabbit(0, self, other)

    def __eq__(self, other):
        parentsSame = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid
        parentsOpposite = self.parent1.rid == other.parent2.rid and self.parent2.rid == other.parent1.rid
        return parentsSame or parentsOpposite
r1 = Rabbit(1)
r2 = Rabbit(1)
r3 = r1+r2
r4 = r1+r2
r5 = r1+r3
# print(r1.getRid()) 
# print(r2.getRid())   
# print(r3)   
# print(r3.getRid())  
# print(r3==r4)
# print(r3==r5)