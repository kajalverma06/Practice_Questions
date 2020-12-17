#Q-1) Write a Python program to get the Python version you are using.
import sys
print(sys.version)

#Q-2) Write a Python program to display the current date and time.
import datetime
today = datetime.datetime.now()
print(today.strftime('%Y-%m-%d \n%H-%M-%S'))

#Q-3) Write a program which can compute the factorial of a given numbers. The results should be printed in a comma separated sequence on a single line.
x= int(input('Enter a number   '))
a=1
for i in range(1,x+1):
    a= a*i
print(a)

#Q-4) With a given integral num n, write a program to generate a dictionary that contains (i,i*i) such that is an integral number between 1 & n (both included) and then the program
# should print the dictionary.
x= int(input('enter a num   '))
d = {}
for i in range(1,x+1):
    d[i]=i*i
print(d)

#Q-5) Write a program that accepts a sequence of comma-separated num from console and generate a list and a Tuple which contains every num.
lst = input().split()
tpl = tuple(lst)
print(lst)
print(tpl)

#Q-6) Write a Python program which accepts the radius of a circle from the user and compute the area.
R = input('Enter the radius of the circle.. ')
from math import pi
Area = pi*int((R))**2
print('Area = ' + str(Area))

#Q-7) Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
f_name = input('Enter your first name.. ')
l_name = input('Enter your last name.. ')
print(l_name.title() + ' ' + f_name.title())

#Q-8) Write a program that accepts a comma separated of words as input and prints the word in a comma separated sequence after sorting them alphabetically.
items = input().split()
items.sort()
print(items)

#Q-9) Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
lst = []
while True:
    x = input()
    if len(x)==0:
        break
    lst.append(x.upper())
for i in lst:
    print(i)

#Q-10) Write a Python program to accept a filename from the user and print the extension of that.
user_input = input('Enter filename with extension.. ').split(".")
print(user_input[-1])    
