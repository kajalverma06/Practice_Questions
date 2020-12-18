#Q-1 Write a Python program to display the first and last colors from the following list.
color_list = ["Pink","Purple","White" ,"Black"]
print(color_list[0] + ', ' + color_list[-1])

#Q-2 Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
print("%i/%i/%i" %exam_st_date)

#Q-3 Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
while True:
    word = input().split()
    if len(word)==0:
        break
    for i in word:
        if word.count(i) > 1:
           word.remove(i)
           word.sort()
    print(' '.join(word))
    
#Q-4 Write a Python program that accepts an integer (n) and computes the value of m+mm+mmm.
m = int(input('Enter the value of n.. '))
m1 = int('%i' %m)
m2 = int('%i%i' %(m,m))
m3 = int('%i%i%i' %(m,m,m))
print(m1+m2+m3)

#Q-5 Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s)
print(abs.__doc__)

#Q-6 Write a Python program to print the calendar of a given month and year.
import calendar
m = int(input("Enter the no. of month.. "))
y = int(input("Enter the year.. "))
print(calendar.month(y,m))

#Q-7 Write a Python program to calculate number of days between two dates.
from datetime import date
first_date = date(2014,9,8)
last_date = date(2014,9,17)
diff_day = last_date-first_date
print(diff_day.days)

#Q-8 Write a Python program to get the volume of a sphere with radius 6.
from math import pi
r=6
volume = (4/3)*pi*(r**3)
print(volume)

#Q-9 Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
num = int(input('Enter the value for num '))
if num>17:
    difference = 2*(num-17)
else:
    difference = 17-num
print(difference)

#Q-10 Write a Python program to test whether a number is within 100 of 1000 or 2000
def near_thousand(n):
    return (abs(1000-n)<=100 or abs(2000-n)<=100)
print(near_thousand(600))
