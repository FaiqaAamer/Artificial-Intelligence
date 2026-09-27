#Q1.
for i in range(1500, 2700):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

#Q2.
c = float(input("Enter temperature in celcius: "))
f = (c * 9 / 5) + 32
print(c, "c is ", round(f), " in fahrenheit.")

f = float(input("Enter temperature in fahrenheit: "))
c = (f - 32) * 5 / 9
print(f, "f is ", round(c), " in celsius.")

#Q3
import random
number = random.randint(1, 9)
while True:
    guess = int(input("Guess a number from 1 to 9: "))
    if guess == number:
        print("Well guessed.")
        break
    else: 
        print("Wrong guess, Try again")

#Q4
for i in range(1, 6):
    for j in range(i):
        print("*", end = "")
    print()
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end = "")
    print()

#Q5
word = input("Enter a word: ")
print("Reversed word: ", word[::-1])

#Q6
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for number in numbers:
    if number % 2 == 0:
        even += 1
    else: 
        odd += 1
print("Count of even:", even)
print("Count of odd:", odd)

#Q7
datalist = [1245, 11.3, 1+3j, False, 'Hello World', (0, -1), (5, 12), {"class": "V", "section": "A"}]
for data in datalist:
    print("Type of", data, "is", type(data))

#Q8
for number in range(7):
    if number == 3 or number == 6:
        continue
    print(number)

#Q9
a = 0
b = 1
while b <= 50:
    print(b, end = "")
    print()
    a, b = b, a + b

#Q10
row = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))
array = []
for i in range(row):
    row = []
    for j in range(column):
        row.append(i * j)
    array.append(row)
print(array)

#Q11
print("Enter lines (blank line to terminate):")
while True:
    line = input()
    if line == "":
        break
    print(line.lower())

#Q12
data = input("Enter 4 digit binary numbers separated by commas: ")
numbers = data.split(",")
result = []
for binary in numbers:
    if int(binary, 2) % 5 == 0:
        result.append(binary)
print("Binary numbers divisible by 5:", ",".join(result))

#Q13
text = input("Enter a string: ")
letters = 0
digits = 0
for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
print("Letters:", letters)
print("Digits:", digits)

#Q14
password = input("Enter a password: ")
has_lower = any(char.islower() for char in password)
has_upper = any(char.isupper() for char in password)    
has_digit = any(char.isdigit() for char in password)
has_special = any(char in '@#$' for char in password)

if(6 <= len(password) <= 16 and has_lower and has_upper and has_digit and has_special):
    print("Valid password")
else:
    print("Invalid password")