#Q-1 Write a Python program that will accept the base and height of a triangle and compute the area.
def area(h,b):
    area = (1/2)*(h*b)
    print(area)
area(4,5)

#Q-2 Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
def sum_3(x,y,z):
    if (x==y) or (y==z) or (x==z):
        print('sum is zero')
    else:
        print(x+y+z)
sum_3(3,3,5)

#Q-3 Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
def sum_2(x,y):
    sum = x+y
    if 15<sum>20:
        print('ans is 20')
    else:
        print(sum)
sum_2(15,7)

#Q-4 Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
def return_true(x,y):
    sum = x+y
    diff = x-y
    if (x==y) or (sum == 5) or (diff ==5):
        return True
    else:
        return False
ans = return_true(3,2)
print(ans)

#Q-5 Write a Python program to add two objects if both objects are an integer type.
def add_obj(x,y):
    if type(x) == int and type(y) == int:
        sum = x + y
        print(sum)
    else:
        print('entered object are not integer type')
add_obj('2','4')

#Q-6 Write a Python program to display your details like name, age, address in three different lines
print('Enter your details:')
name = input('Enter your name..: ')
age = input('enter your age..: ')
add = input('enter your address.. ')
print('Entered details are : ' + '\n' + name + '\n' + age + '\n' + add)

#Q-7 Write a Python program to solve (x + y) * (x + y).
def solve_exp(x,y):
    exp = (x+y)*(x+y)
    print(exp)
solve_exp(4,3)

#Q-8) Write a Python program to find the factors of the given numbers
def factors(x):
    for i in range(1,x+1):
        if x%i ==0:
            print(i)
factors(100)

#Q-9) Write a Python program to parse a string to Float or Integer.
n = input('Enter a number ')
print(type(n))
print(float(n))
print(int(float(n)))

#Q-10) Write a Python program to print without newline or space
for i in range(0, 10):
    print('#', end="")
