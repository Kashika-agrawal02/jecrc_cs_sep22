Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=('kashika',35,20,40,3.3,25+5j)
type(t)
<class 'tuple'>
t[1]
35
t[1]=28
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t[1]=28
TypeError: 'tuple' object does not support item assignment
t[1]==28
False
t[1]==35
True
t
('kashika', 35, 20, 40, 3.3, (25+5j))
t[20]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    t[20]
IndexError: tuple index out of range
t[2]
20
print(t)
('kashika', 35, 20, 40, 3.3, (25+5j))
t+='hello'
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    t+='hello'
TypeError: can only concatenate tuple (not "str") to tuple
a='hello'
t+=a
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t+=a
TypeError: can only concatenate tuple (not "str") to tuple
t
('kashika', 35, 20, 40, 3.3, (25+5j))
t=t+a
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t=t+a
TypeError: can only concatenate tuple (not "str") to tuple
t=t+(a,)
t
('kashika', 35, 20, 40, 3.3, (25+5j), 'hello')
b=5.55
t+=(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    t+=(b)
TypeError: can only concatenate tuple (not "float") to tuple
t+=(b,)
t
('kashika', 35, 20, 40, 3.3, (25+5j), 'hello', 5.55)
t+=('hi')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    t+=('hi')
TypeError: can only concatenate tuple (not "str") to tuple
t+=('hi',)
t
('kashika', 35, 20, 40, 3.3, (25+5j), 'hello', 5.55, 'hi')
