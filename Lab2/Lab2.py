###LOOPS
###1. While loop
count = 0
while (count < 3):
    count = count + 1
    print("World")

###2. Infinite Loop
# count = 0
# while (count == 0):
#     print("Hello")

###3. List iteration with for loop
print("List iteration")
I = ["Red", "Pink", "Blue"]
for i in I:
    print(i)

###4. Tuple iteration with for loop
print("\nTuple iteration:")
t = ("Pizza", "Soup", "Cake")
for i in t:
    print(t)

###5. String iteration with for loop
print("\nString iteration:")
t = "Faiqa"
for i in t:
    print(t)

###6. Iterating by index of sequence
list = ["Horse", "Sunflower", "Bottle Green"]
for index in range(len(list)):
    print(list[index])

###7. Continue Statement
for letter in 'geeksforgeeks':
    if letter =='e' or letter == 's':
        continue
    print ('Current letter: ', letter)

###8. Break Statement
for letter in 'geeksforgeeks':
    if letter =='e' or letter == 's':
        break
print ('Current letter: ', letter)

###FUNCTIONS
###9.Creating a function
def fun1():
    print("This is a function")
fun1() #Calling a function

###10. Function with Parameters
def fun2(Dep):
    print("This is " + Dep + " Department")
fun2("Law")
fun2("English")
fun2("IT")

###11. Function with default Parameter
def fun3(city = "Gujranwala"):
    print("I live in " + city)
fun3("Lahore")
fun3()
fun3("Karachi")

###12. Passing a list as Parameter
def fun4(num):
    for i in num:
        print(i)

numbers = ["One", "Two", "Three"]
fun4(numbers)

###13. Return values
def fun5(x):
    return 5 * x
print(fun5(3))
print(fun5(7))
print(fun5(2))

###14. Keyword Arguments
def fun6(x, y, z):
    print("This number is " + x)
fun6(y = "4", z = "3", x = "6")

###15. Classes in python
class C1:
    x = 5
c1 = C1()
print(c1.x)

###16. _init_() Function
class Person():
    def __init__ (self, name, age): #Default Constructor
        self.name = name
        self.age = age
p1 = Person("Faiqa", 18)
print(p1.name)
print(p1.age)

###17. Object methods
class Person():
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def myFun(self):
        print("Hello, My name is " + self.name)

p1 = Person("Faiqa", 18)
p1.myFun()
