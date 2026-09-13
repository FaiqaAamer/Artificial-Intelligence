###1. Programming Syntax
print("Hello World!")

###2. Comments in Python
a = 1
#Initial value of a is 1
if a > 0:
    print("This is a proper comment in Python") #Print a string

###3. Input/Output
# txt = input("This is input in python: ")
# print(txt) #This is output in python

###4. Multiple statements on single line
print("This is first.")
print("This is second.")
print("Statement1"); print("Statement2") #Ypu can write 2 statements in 1 line like this

a = 1; b = 2; print(a + b)

###5. Indentation
a = 1
b = 2
c = 3
#Tab indentation
if a > 0:
#print("Hello") If you writ like this without tab space it give error as it act like the bracket
    print("Tab indentation")

#Single space indentation
if b > 0:
 print("Single space indentation")

#Single space and Tab indentation
if c > 0:
     print("Single space and Tab indentation")

###6. Datatypes in Python
#Integer 
a = 1234
b = -1234
print(type(a))
print(type(b))

#Float
a = 12.0034
b = -12.3004
c = 1.34e-10
d =5E234
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Complex
a = complex(2 , 4)
b = 1 - 9j
c = 4 - 6J
print(type(a))
print(type(b))
print(type(c))

#Boolean
a = 3 > 7
b = 4 > -1
c = True
d = False
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#String
a = "Python"
print(type(a))

###7. Strings
#Strings are Immutable
s1 = "String with double quote"
s2 = 'String with singlt quote'
#s3 = "String starting with double quote and ending with single quote' #Error: Wrong way to write string
#s4 = 'String starting with single quote and ending with double quote" #Error: Wrong way to write string
s5 = "String with single'quote in double quote"
s6 = 'String with double"quote in single quote'
print(s1)
print(s2)
print(s5)
print(s6)

###8. Special Characters in String
print("This is backslash (\\).") #\\
print("This is tab \t key.") #\t
print("These are \'Single quotes\'.") #\'
print("These are \"Single quotes\".") #\"
print("This is for new line. \nNew Line.") #\n

###9. String Indices and Accessing String Elements 

#Positive Indexing i.e. 0,1,2,3 for accessing from left
#Negative Indexing i.e. -4,-3,-2,-1 for accessing from right

#  F  A  I  Q  A
#  0  1  2  3  4
# -5 -4 -3 -2 -1

#Positive Indexing
str1 = "I love Horses"
print(str1[3])
print(str1[10])
print(str1[7])

#Negative Indexing
str1 = "Go for a walk"
print(str1[-9])
print(str1[-12])
print(str1[-6])

###10. String Slicing
#n:m, It displays character from n to m-1 the last one is not included
f = "Faiqa"
print(f[1:3])

###11. Lists
#A list is a container which holds comma-separated values (items or elements) between square brackets where Items or elements need not all have the same type. 
li1 = ["Circle", "Square", "Rectangle", "Triangle"] #Contain strings
li2 = [4, 7, 10, 11, 27, 28] #Contain integers
li3 = [0.4, 0.7, 1.0, 1.1, 2.7, 2.8] #Contain floats
li4 = ["Circle", 1.0, 11] #Contain strings
print(li1)
print(li2)
print(li3)
print(li4)

###12. List indeces
li = ["Circle", "Square", "Rectangle", "Triangle"]
#0 and -4 will be same
print(li[0])
print(li[-4])

#2 and -2 will be same
print(li[2])
print(li[-2])

###13. List Slice
#Lists can be sliced like strings and other sequences. The syntax of list slices is easy
li = ['Green', 'Pink', 'Black', 'Red', 'Yellow', 'Blue', 'Lavender', 'Brown']
print(li[4:6]) #Last one e.g. 6 not included
print(li[0:-7]) #Start from 0 and on opposite side it will cpunt till -7 and print Green

###14. Conditional Statements Python supports the usual logical conditions from mathematics 
# a == b 
# a != b 
# a < b 
# a <= b 
# a > b 
# a >= b 

# == 
print("For ==")
a = int(input("a : "))
b = int(input("b : "))
if a == b:
    print(a, "is Equal to", b)
else:
    print(a, "is NOT Equal to", b)

# != 
print("For !=")
a = int(input("a : "))
b = int(input("b : "))
if a != b:
    print(a, "is Not Equal to", b)
else:
    print(a, "is Equal to", b)

# < 
print("For <")
a = int(input("a : "))
b = int(input("b : "))
if a < b:
    print(a, "is Less than", b)
else:
    print(a, "is NOT Less than", b)

# <= 
print("For <=")
a = int(input("a : "))
b = int(input("b : "))
if a <= b:
    print(a, "is Less than or Equal to", b)
else:
    print(a, "is Greater than", b)

# > 
print("For >")
a = int(input("a : "))
b = int(input("b : "))
if a > b:
    print(a, "is Greater than", b)
else:
    print(a, "is NOT Greater than", b)

# >= 
print("For >=")
a = int(input("a : "))
b = int(input("b : "))
if a >= b:
    print(a, "is Greater than or Equal to", b)
else:
    print(a, "is Less than", b)
