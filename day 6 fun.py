Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=print('hi how r u?')
hi how r u?
a
print(a)
None
def myfun():
    print('this is first fun')

    
myfun()
this is first fun
##no i/p no o/p
a=myfun()
this is first fun
print(a)
None
##no i/p no o/p
#no i/p but o/p
def second()
SyntaxError: expected ':'
def second():
    return 'abc'

second()
'abc'
b=second()
b
'abc'
print(b)
abc
def second():
    return 1

second()
1
#i/p but no o/p
def third(x):
    print('hello')

    
third('x')
hello
#i/p and o/p
def fourth(x)
SyntaxError: expected ':'
def fourth(x):
    return x*10

fourth('abc')
'abcabcabcabcabcabcabcabcabcabc'
fourth(3)
30
KeyboardInterrupt
def fourth(x):
    return x*10

def fourth(x):
    print('hi')
    print('hello')
    print('hw r u?')
    return x*10

fourth('x')
hi
hello
hw r u?
'xxxxxxxxxx'
fourth(2)
hi
hello
hw r u?
20
def fourth(x):
    print('hi')
    return x**2
    print('hello')

    
fourth(2)
hi
4
fourth(3)
hi
9
def five(x,y,z):
    return x+y+z

five(2,4,3)
9
def six(x,y)
SyntaxError: expected ':'
def six(x,y):
    return x+y,x*y

six(3,4)
(7, 12)
def six(x,y):
    return x+y
    return x*y

six(2,3)
5
def six(x,y):
    return x+y,x*y

six(3,4)
SyntaxError: invalid syntax

def six(x,y):
    return x+y,x*y

six(3,5)
(8, 15)
KeyboardInterrupt
#return multiple output

def six(x,y,z):
    return x+y+z

six(x=5y=4,z=2)
SyntaxError: invalid decimal literal
six(x=5,y=4,z=2)
11
six(y=5x=4,z=2)
SyntaxError: invalid decimal literal
six(y=5,x=4,z=2)
11
#keyword arguments

def six(x,y,z):
    return x+y+z

six(3,4)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    six(3,4)
TypeError: six() missing 1 required positional argument: 'z'
def seven(x,y,z=1):
    return x+y+z

seven(2,8,7)
17
seven(4,8)
13
def seven(x=1,y,z=1):
    return x+y+z
SyntaxError: non-default argument follows default argument
def seven(x,y=4,z=1):
    return x+y+z

seven(2)
7
def seven(x,y=2,z):
    return x+y+z
SyntaxError: non-default argument follows default argument
##default values

def eight(*x):
    return x

eight()
()
eight(4)
(4,)
eight(2,3,4)
(2, 3, 4)
def nine(**x):
    return x

eight()
()
eight(3)
(3,)
eight(3,4,5)
(3, 4, 5)
def nine(**x):
    return x

nine()
{}
nine(name='kashika',phone=234454)
{'name': 'kashika', 'phone': 234454}
nine(n1=0,n2=[1,32,21],n3=['abc','xyz'])
{'n1': 0, 'n2': [1, 32, 21], 'n3': ['abc', 'xyz']}
##############
def ten(a)
SyntaxError: expected ':'
def ten(name):
    print('happybirthday to u')
    return name

ten('kashika')
happybirthday to u
'kashika'
ten('kanika')
happybirthday to u
'kanika'
def ten(name):
    print('happybirthday to u'end='\n')
    print('may god bless u'end='\n')
    print('bar bar din ye aae'end='\n')
    return name
SyntaxError: invalid syntax. Perhaps you forgot a comma?
def ten(name):
    print(sep='happybirthday to u 'end='\n')
    print(sep='may god bless u'end='\n')
    print(sep='bar bar din ye aae'end='\n')
    return name
SyntaxError: invalid syntax. Perhaps you forgot a comma?
def ten(name):
    print(sep='happybirthday to u ',end='\n',sep='may god vless u',end='\n')
    
    return name
SyntaxError: keyword argument repeated: sep
def ten(name):
    print('happybirthday to u ')
    print('may god bless u')
    print(f'bar bar din ye aae{name}')
    return name

ten('kashika')
happybirthday to u 
may god bless u
bar bar din ye aaekashika
'kashika'
def ten(name):
    print('happybirthday to u ')
    print('may god bless u')
    print(f'bar bar din ye aae{name}')

    
ten('kashika')
happybirthday to u 
may god bless u
bar bar din ye aaekashika
###########################
def myfun(x,y,z):
    return x+y+z

myfun(2,3,3)
8

myadd=lambda x,y,z: x+y+z
myadd(5,3,4)
12
import math
math.pi
3.141592653589793
math.sqrt(81)
9.0
math.sqrt(92)
9.591663046625438
math.pow(2,3)
8.0
math.sqr(4)
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    math.sqr(4)
AttributeError: module 'math' has no attribute 'sqr'. Did you mean: 'sqrt'?
math.factorial(5)
120
math.pow(92,2)
8464.0
import math as m
m.pi
3.141592653589793
m.sqrt(16)
4.0
from math import sqrt
sqrt(91)
9.539392014169456
import datetime as dt
dt.date.today
<built-in method today of type object at 0x00007FFA0B1B8960>

aj_ki_date=dt.date.today()
print(aj)
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    print(aj)
NameError: name 'aj' is not defined. Did you mean: 'a'?
-aj_ki_date=dt.date.today()
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
aj_ki_date=dt.date.today()
print(aj_ki_date)
2022-09-19
import calendar
print(calendar.calendar(2022))
                                  2022

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6          1  2  3  4  5  6
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       7  8  9 10 11 12 13
10 11 12 13 14 15 16      14 15 16 17 18 19 20      14 15 16 17 18 19 20
17 18 19 20 21 22 23      21 22 23 24 25 26 27      21 22 23 24 25 26 27
24 25 26 27 28 29 30      28                        28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3                         1             1  2  3  4  5
 4  5  6  7  8  9 10       2  3  4  5  6  7  8       6  7  8  9 10 11 12
11 12 13 14 15 16 17       9 10 11 12 13 14 15      13 14 15 16 17 18 19
18 19 20 21 22 23 24      16 17 18 19 20 21 22      20 21 22 23 24 25 26
25 26 27 28 29 30         23 24 25 26 27 28 29      27 28 29 30
                          30 31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7                1  2  3  4
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       5  6  7  8  9 10 11
11 12 13 14 15 16 17      15 16 17 18 19 20 21      12 13 14 15 16 17 18
18 19 20 21 22 23 24      22 23 24 25 26 27 28      19 20 21 22 23 24 25
25 26 27 28 29 30 31      29 30 31                  26 27 28 29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                1  2  3  4
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31
31

print(calender.month(2004,3))
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    print(calender.month(2004,3))
NameError: name 'calender' is not defined. Did you mean: 'calendar'?
print(calendar.month(2004,3))
     March 2004
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31

KeyboardInterrupt
print(calendar.week(2004,3,1))
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    print(calendar.week(2004,3,1))
TypeError: TextCalendar.formatweek() takes 3 positional arguments but 4 were given
print(calendar.Week(2004,3,1))
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    print(calendar.Week(2004,3,1))
AttributeError: module 'calendar' has no attribute 'Week'. Did you mean: 'week'?
print(calendar.week(2004,3))
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    print(calendar.week(2004,3))
  File "C:\Users\91759\AppData\Local\Programs\Python\Python310\lib\calendar.py", line 321, in formatweek
    return ' '.join(self.formatday(d, wd, width) for (d, wd) in theweek)
TypeError: 'int' object is not iterable
def six(x,y)
SyntaxError: expected ':'
def six(x,y):
    return x+y,x*y

a,b=six(4,3)
print(a)
7
print(b)
12
