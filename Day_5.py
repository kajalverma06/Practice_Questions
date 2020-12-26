#Q-1)    Write a program that calculate and prints the value according to the given formula:
#         Q = square root of[(2*C*D)/H]
#         Following are the fixed values of C and H: C= 50; H=30
#         D is the variable whose value be input to your program in a comma separated sequence.

from math import sqrt
C,H = 50,30
def cal(D):
    return sqrt((2*C*D)/H)
D = input().split()
D = [str(round(cal(int(i)))) for i in D]
print(D)

#Q-2) Write a program which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The number obtained should be
# printed a comma-separated sequence on a single line.
lst =[]
for i in range(1000,3001):
    flag = 1
    for j in str(i):
        if ord(j)%2 !=0:
            flag = 0
    if flag ==1:
        lst.append(str(i))
print(','.join(lst))

#Q-3) Write a program that accepts a sentence and calculate the number of letters and digits.
inp = input().split()
digit,num = 0,0
for i in inp:
    for j in i:
      if j.isdigit():
         digit = digit+1
      elif j.isalpha():
         num = num+1
print(digit)
print(num)

#Q-4) Write a program that accepts a sentence and calculate the number of uppercase letters and lowercase letters.
inp = input().split()
Uppercase, Lowercase = 0,0
for i in inp:
    for j in i:
        if j.isupper():
            Uppercase +=1
        elif j.islower():
            Lowercase +=1
print(Uppercase)
print(Lowercase)

#Q-5) Use a list comprehension to square each odd num in a list. The list is input by a sequence of comma separated numbers.
a = input().split()
li =[]
for i in a:
    for j in i:
       if ord(i)%2!=0:
         i=int(i)**2
         li.append(i)
print(li)

#Q-6) Write a program that computes the net amount of a bank account based a transaction log. The transaction log format is shown as following:
#         D = 100; W = 200 (where D= deposit and W = Withdrawal
while True:
    D = input('enter deposit value  ').split()
    if str(input())==0:
        break
    W = input('enter withdrawal value  ').split()
    if str(input())==0:
        break
    break
w_tot=0
d_tot=0
while True:
    for i in W:
        w_tot += int(i)
    break
while True:
    for j in D:
        d_tot += int(j)
    break
total= d_tot-w_tot
print(f'Net account balance is ', total)

#Q-7)You are required to write a program to sort the(name,age,score)tuples by ascending order where name is string,age and score are numbers. The tuples are input by console. 
# The sort criteria is Sort based on name; Then sort based on age; Then sort by score The priority is that name>age>score.
lst = []
while True:
    x = input().split(',')
    if not x[0]:
        break
    lst.append(tuple(x))
print(lst)
lst.sort(key = lambda y:(y[0],int(y[1]),int(y[2])))
print(lst)

#Q-8) Write a program to compute the frequency of the words from the input. The output should given after sorting the key alphanumerically.
x = input().split()
y = sorted(set(x))
for i in x:
    print('{0}:{1}'.format(i,x.count(i)))
    
#Q-9) Write a method which can calculate square value of number.
x= input()
def cal(y):
    for i in y:
        return int(i)**2
print(cal(x))

#Q-10) Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
lst = []
while True:
    x = input()
    if len(x)==0:
        break
    lst.append(x.upper())
for i in lst:
    print(i)
