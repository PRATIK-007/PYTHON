import re

# --------------------------VARIABLES AND DATATYPES------------------
print("#--------------------------VARIABLES AND DATATYPES------------------ ")
print("hello world")
x = 20
y = 320
z = "pratik kulkarni"
k = "piyush Kulkarni"

# ------------------------SLICING AND STEP-----------------------
print("------------------------SLICING AND STEP-----------------------")
print("x : ", x, "y = ", y, " z : ", z, "\n len : ", len(z), " z[3-7]: ", z[3:7], " \nstep z: ", z[:10:2], " step z: ",
      z[::2], " step z: ", z[::-1])
print(" z+ k: ", (z[::2] + k))
print(z.upper())
print("\n split: ", z.split(), )
print(" \nsplit: ", z.split('t'))
print("\n pratik {} {} ".format('chandrakant', 'Kulkarni'))

print("\n pratik {1} {1} ".format('chandrakant', 'Kulkarni'))

print("\n pratik {c} {k} ".format(c='chandrakant', k='Kulkarni'))
r = 120000 / 3434

print("\n result is  {r:1.4f}".format(r=r))

print(f"\n pratik {'Kulkarni'}  ")

# ------------------------LIST-----------------------------
print("------------------------LIST-----------------------------")
list1 = ['one', 2, 'three']
list2 = ['1', 'two', '3']
list3 = list1 + list2
print(list3)
list3.append('five')
print(list3)
print(list3.pop())
print(list3)
print(list3.pop(2))
print(list3)

list4 = [1, 3, 4, 2, 5, 6, 7, 4, 3]
print("list4 : ", list4)
list4.sort()
print(list4)
list4.reverse()
print(type(list4), "      ", list4)

# -------------------------DICTIONARY---------------------------
print("#-------------------------DICTIONARY---------------------------")
dict1 = {'key1': 23, 1: 'value2', 'key3': ['a', 'b', 'c']}
print(dict1)
print(dict1[1], "  ", dict1['key1'], "   ", dict1['key3'], "  ", dict1['key3'][2].upper())
print(dict1)

# ---------------------TUPLE-------------------------------
print("#---------------------TUPLE-------------------------------")
tuple1 = ('one', 2, 'one')
print(tuple1)
print(tuple1.count('one'), "  ", tuple1.index(2))

# ----------------------SET---------------------------------
print("#----------------------SET---------------------------------")
set1 = {1, 2, 3}
print(set1)
set1.add(4)
print(set1)
set1.add(3)
print(set1.remove(4), "  ", set1)

print(1 > 2)

# -----------------------FILE------------------------
print("#-----------------------FILE------------------------")
file1 = open('myfile.txt', 'w+')
file1.seek(0)
contents = file1.read()
file1.seek(0)
print(file1.readlines(5))
file1.close()
print(contents)

with open('myfile.txt') as myfile:
    print(myfile.read())

# -------------------------COMPARISON-------------------
print("#-------------------------COMPARISON-------------------")
print('2' == 2)
print(3 != 3)
print(4 != 5)
print('hello' == 'Hello')

print(not 1 == 2)

# --------------------------IF ELSE--------------------
print("#--------------------------IF ELSE--------------------")
if x == 20:
    print('x : ', x)
elif y == 220:
    print('y')
else:
    print('zcxzxc')

# ----------------------FOR LOOP---------------------------
print("#----------------------FOR LOOP---------------------------")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in list1:
    if num % 2 == 0:
        print("even : ", num)
    else:
        print("odd : ", num)

string = "hello world"

for letter in string:
    print(letter)

LIST = [(1, 2), (3, 4), (5, 6), (7, 8)]

for a, b in LIST:
    print(a)
    print(b)

for num in LIST:
    print(num)

for d in dict1:
    print(" keys : ", d)

for num, values in dict1.items():
    print(num, values)

for num in range(0, 10, 2):
    print(num)

# -----------------------WHILE-----------------------------
print("#-----------------------WHILE-----------------------------")
x = 1
while x < 5:
    print(x)
    x += 1
else:
    print("x is greater than 5")

# ---------------------CONTINUE------------------------
print("#---------------------CONTINUE------------------------")
for letter in string:
    if letter == 'l':
        continue
    print(letter)

# --------------------BREAK--------------------------
print("#--------------------BREAK--------------------------")
for letter in string:
    if letter == 'l':
        break
    print(letter)

# -------------------ENUMERATE-------------------------
print("#-------------------ENUMERATE-------------------------")

word = "abcdef"

for index, letter in enumerate(word):
    print(index, letter)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

for item in zip(list1, list1):
    print(item)

print(list(zip(list1, list2)))

# --------------------------------IN-------------------------
print("#------------------------IN---------------------------")

print('a' in 'a world')

print('mykey' in {'myket': 345})
d = {'mykey': 354}
print(354 in d.values())

# --------------------------------SHUFFLE-------------------------
print("#--------------------------------SHUFFLE--------------------------")

from random import shuffle

shuffle(list1)
print(list1)

shuffle(list3)
print(list3)

# --------------------------------RANDINT-------------------------
print("#--------------------------------RANDINT--------------------------")
from random import randint

num = randint(0, 10)
print(num)

# --------------------------------INPUT-------------------------
print("#--------------------------------INPUT--------------------------")

result = input("enter a number here : ")

print(result)

# --------------------------------CAST-------------------------
print("#--------------------------------CAST--------------------------")

x = '32'
print("type of x is: ", type(x))

print("type of x is: ", int(x))

# --------------------------------LIST COMPREHENSION-------------------------
print("#--------------------------------LIST COMPREHENSION--------------------------")

word = "abcdefghijklmnopqrstuvwxyz"

list1 = [letter for letter in word]

print(list1)

celcius = [1, 2, 3, 4, 233, 323, 332, 111]

fahrenit = [((9 / 5) * temp + 32) for temp in celcius]

print(fahrenit)

result = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]

print(result)


def fun(name):
    return 'hello ' + name


result = fun("pratik")
print(result)

# --------------------------------FUNCTION-------------------------
print("#--------------------------------FUNCTION--------------------------")


def dog_check(mystring):
    if 'dog' in mystring.lower():
        return True
    else:
        return False


result = dog_check('Dog ran away')
print(result)


#  the above function indicates that it is return by an begginner in
#  python  as here " 'dog' in  mystring.lower():" is already returning an
#  boolean ,so writing it in if else is no use
#  instead it can be writen as

def dog_check1(mystring):
    return 'dog' in mystring


result = dog_check1('dog ran away')
print(result)


def pig_latin(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word


print(pig_latin("aksfd"))

# ----------------------multiple arguments------------------
print("#----------------------multiple arguments------------------")


def myfun(*args):  # here args is tuple
    print(args)


myfun(43, 45, 32, 56, 78, 67, 4, 8, 12, 676, 98, 76, 35, 22)


def myfun2(**args):  # here args is dictionary
    print(args)
    if 'fruit' in args:
        print("fruit choice is: {}".format(args['fruit']))
    else:
        print('I did not find any fruit here')


myfun2(fruit='apple', veggie='palak')

# ---------------------- MAP------------------
print("#---------------------- MAP------------------")


def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]

print(map(square, my_nums))

for item in map(square, my_nums):
    print(item)

# ----------------------LAMBDA------------------
print("#----------------------LAMBDA------------------")

# lambda is a different way to write functions
lambda num: num ** 2

print(square(5))
list6 = list(map(lambda num: num ** 2, my_nums))
print(list6)

# ----------------------DECORATORS------------------
print("#----------------------DECORATORS------------------")


def function4():
    return "hello"


print(function4, "    ", function4())
greet = function4

print(greet())

del function4

print(greet())


def hello():
    print("hello ")

    def greet():
        return "\t greet inside hello"

    print(greet())


hello()
print("\n\n\n")


def hello1():
    print("hello 1")

    def greet1():
        return "\t greet inside hello 1"

    print("end of hello")
    return greet1


new_func = hello1()
print("aaaaaa")
print(hello1, "    ", hello1())
print(new_func, "    ", new_func())

# ----------------------COLLECTIONS------------------
print("#----------------------COLLECTIONS------------------")

from collections import Counter

lst = [1, 2, 2, 2, 2, 3, 3, 3, 1, 2, 1, 12, 3, 2, 32, 1, 21, 1, 223, 1]

print(Counter(lst))

# ----------------------REGX------------------
print("#----------------------REGX------------------")

text = "hello i am Pratik and ny phone no is +91-38456-78915"
ser = "Pratik"

print(re.search(ser, text))
print(re.search(r'\W\d\d-\d\d\d\d\d-\d\d\d\d\d', text))

phone = re.compile(r'(\W\d\d)-(\d{5})-(\d{5})')
result2 = re.search(phone, text)

print(result2.group())
print(result2.group(1))

text = " I have a cat and a dog as pet "

phone = re.findall(r'.at', text)
print(phone)

phone = re.findall(r'...at', text)
print(phone)

phone = re.findall(r'^\d', "2 is a number")
print(phone)

phone = re.findall(r'^\d', "this  is a number 2")
print(phone)

phone = re.findall(r'\d$', "this  is a number 2")
print(phone)

pattern = r'[^\d]'
print(re.findall(pattern, "this  is a number 2"))

pattern = r'[^\d]+'
print(re.findall(pattern, "this  is a number 2"))

clean = re.findall(pattern, "this  is 3 45 sd a number 2")
print(''.join(clean))

# ----------------------ZIPPING AND UNZIPPING------------------
print("#----------------------ZIPPING AND UNZIPPING------------------")

import zipfile

comp_file = zipfile.ZipFile('compile.zip', 'w')
comp_file.write('myfile.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

extract = zipfile.ZipFile('compile.zip', 'r')
extract.extractall('extracted content')

import shutil

dir_to_zip = r"E:\PYTHON_3\Projects\udemy\extracted_content"

output_file = "example"

shutil.make_archive(output_file, "zip", dir_to_zip)
"""
#----------------------WEB SCRAPING------------------
print("#----------------------WEB SCRAPING------------------")

import requests

req = requests.get("https://en.wikipedia.org/wiki/One-Punch_Man")
print(type(req))
print(req.text)

import bs4

soup = bs4.BeautifulSoup(req.text,"lxml")

print(soup.select('title'))
"""
# ----------------------IMAGES------------------
print("#----------------------IMAGES------------------")

from PIL import Image

img = Image.open(r"E:\PYTHON_3\Projects\udemy\wed.png")
type(img)
img.show()
img.crop((100, 100, 500, 500))
img.show()