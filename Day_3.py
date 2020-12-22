#Q-1) Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum
f_num = int(input('Enter first num  '))
s_num = int(input('Enter second num  '))
t_num = int(input('Enter third num  '))
if (f_num == s_num) and (s_num == t_num):
    result = 3*(f_num+s_num+t_num)
else:
    result = f_num+s_num+t_num
print(result)

#Q-2) Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string 
#unchanged.
user_input = input('enter a string.. ').split()
if user_input[0] == 'is':
    print(str(user_input))
else:
    user_input.insert(0,'is')
    print(str(user_input))
# OR
def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str
print(new_string("Array"))
print(new_string("IsEmpty"))

#Q-3) Write a Python program to get a string which is n (non-negative integer) copies of a given string.
def copy_str(str,n):
    result = ''
    for i in range(n):
        result = result + str
    return result
print(copy_str('happy',4))

#Q-4) Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user
user_input = int(input('Enter a num  '))
if user_input%2 == 0:
    print('Input num is even')
else:
    print('Input num is odd')

#Q-5) Write a Python program to count the number 4 in a given list.
user_input = input('Enter a series of num  ').split(',')
count = 0
for i in user_input:
    if int(i) == 4:
        count = count + 1
print(count)

#Q-6) Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length 
#is less than 2.
def copy_str(str,n):
    result = ''
    for num in range(n):
        result = result + num
        
#Q-7) Write a Python program to test whether a passed letter is a vowel or not.
def is_vowel(x):
    vowel = ['a','e','i','o','u']
    if x in vowel:
        print('entered letter is vowel')
    else:
        print('entered letter is consonant')
is_vowel('a')

#Q-8) Write a Python program to check whether a specified value is contained in a group of values.
def check_values(x):
    values = [1,2,3,5,6,8,9]
    if x in values:
        print('entered num is contained in a group')
    else:
        print('entered num is contained in a group')
check_values(0)

#Q-9) Write a Python program to concatenate all elements in a list into a string and return it.
def concate_elements(*x):
    str_x = str(*x)
    print(type(str_x))
concate_elements([1,2,3,4,5])

#Q-10)  Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
numbers = [
    486, 362, 57, 418, 907, 344, 236, 375, 823, 506, 597, 978, 322, 625, 953, 345,
    369, 262, 658, 212, 918, 287, 442, 666, 806, 248, 862, 920, 626, 49, 687, 217,
    815, 67, 102, 58, 12, 24, 822, 294, 767, 53, 81, 379, 843, 81, 445, 742, 717,
    958,743, 527
    ]
even_num = []
while numbers:
    for num in numbers:
        if (num % 2 ==0) and (num<237):
            even_num.append(num)
    print(even_num)
    break    
