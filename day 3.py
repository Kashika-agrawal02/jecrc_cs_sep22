Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a='kashika'
b="kashika"
c='''kashika'''
c='''kshfkdhfal
dkfladksa
ljaklfjf'''
print(c)
kshfkdhfal
dkfladksa
ljaklfjf
a=[4]
print(a)
[4]

a='hello world'
print(a)
hello world
print(a[0])
h
print(a[-1])
d
print(a[5])
 
print(a[-11])
h
print(a[-1,-2])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(a[-1,-2])
TypeError: string indices must be integers
print(a[0],a[1])
h e
print(a[0][1])
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(a[0][1])
IndexError: string index out of range
a[11]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a[11]
IndexError: string index out of range
a[-1]
'd'
a[10]
'd'
a[0]a[1]
SyntaxError: invalid syntax
a[0],a[1]
('h', 'e')
a[-11]
'h'
a[6]
'w'
a[6,7]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a[6,7]
TypeError: string indices must be integers
a[-4]
'o'
a[0/1]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a[0/1]
TypeError: string indices must be integers
a='Hello'
a[0:1:1]
'H'
a[0:2:1]
'He'
a[0:2]
'He'
a[:2]
'He'
a[:2:3]
'H'
a[-1]
'o'
a[:-1:]
'Hell'
a[:-1]
'Hell'
a[:-2:1]
'Hel'
a[:1:1]
'H'
a[:-3:-1]
'ol'
a[:-3:-2]
'o'
a[:10:2]
'Hlo'
a='hello world'
a[:10:2]
'hlowr'
a[6:11]
'world'
a[-1:-6]
''
a[-5:]
'world'
a[6:]
'world'
a[-1:]
'd'
a[-1:-1]
''
a[-5: :-1]
'w olleh'
a[-1: :-1]
'dlrow olleh'
a[::-1]
'dlrow olleh'
a[-1::-1]
'dlrow olleh'
a[:-5:-1]
'dlro'
a[:-6:-1]
'dlrow'
a[-5:]
'world'
a[-5::-1]
'w olleh'
a[-5::-2]
'wolh'
a[-1:-9:-1]
'dlrow ol'
a[-2:-6:-1]
'lrow'
a[-7:-6:-1]
''
a[-7:-9]
''
a[-10:-6]
'ello'
a[-8:-6]
'lo'
a[-8:-5]
'lo '
a='hello world'
a.capitalize()
'Hello world'
a='kashika'
a.capitalie
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a.capitalie
AttributeError: 'str' object has no attribute 'capitalie'. Did you mean: 'capitalize'?
a.capitalize()
'Kashika'
a
'kashika'
a=a.capitalize()
a
'Kashika'
a='hello world'
a.title()
'Hello World'
a=a.title()
a
'Hello World'
a.center(50)
'                   Hello World                    '
a.center(50,'*')
'*******************Hello World********************'
a.count('l')
3
a=a.center(50)
a
'                   Hello World                    '
a.lstrip()
'Hello World                    '
a.rstrip()
'                   Hello World'
a.strip()
'Hello World'
a.count('W')
1
a.count('o')
2
a.isupper()
False
a.islower()
False
a=a.strip()
a
'Hello World'
a.islower()
False
a.isupper()
False
a=a.upper()
a
'HELLO WORLD'
a.isupper()
True
a.upper()
'HELLO WORLD'
a.startswith('he')
False
a.startswith('HE')
True
a.endswith('d')
False
lem(a)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    lem(a)
NameError: name 'lem' is not defined. Did you mean: 'len'?
len(a)
11
a
'HELLO WORLD'
a[0]='M'
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    a[0]='M'
TypeError: 'str' object does not support item assignment
del a[0]
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    del a[0]
TypeError: 'str' object doesn't support item deletion
b='agrawalkashika5@gmail.com'
b.split()
['agrawalkashika5@gmail.com']
b.split('@')
['agrawalkashika5', 'gmail.com']
b=b.split('@')
b
['agrawalkashika5', 'gmail.com']
'@'.join(b)
'agrawalkashika5@gmail.com'
#################################################3
m=[12,'hi',2.3,500]
type(m)
<class 'list'>
m[0]
12
m[1:3]
['hi', 2.3]
m[-1]
500
m[-1:-3]
[]
m[-1:-3:-1]
[500, 2.3]
'hi' in m
True
'k' in m
False
'h' in m
False
'hi' not in m
False
'ka' not in m
True
2*m
[12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500]
2*a
'HELLO WORLDHELLO WORLD'
'hello'.join(m)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    'hello'.join(m)
TypeError: sequence item 0: expected str instance, int found
m+=['new value']
m
[12, 'hi', 2.3, 500, 'new value']
m.append('abc')
m
[12, 'hi', 2.3, 500, 'new value', 'abc']
m.append('kas','shika')
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    m.append('kas','shika')
TypeError: list.append() takes exactly one argument (2 given)
m+=['k','j']
m
[12, 'hi', 2.3, 500, 'new value', 'abc', 'k', 'j']
m.extend(['x','y','anything'])
m
[12, 'hi', 2.3, 500, 'new value', 'abc', 'k', 'j', 'x', 'y', 'anything']
m.insert('helli',2)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    m.insert('helli',2)
TypeError: 'str' object cannot be interpreted as an integer
m.insert(2,'hello')
m
[12, 'hi', 'hello', 2.3, 500, 'new value', 'abc', 'k', 'j', 'x', 'y', 'anything']
m.pop('hi')
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    m.pop('hi')
TypeError: 'str' object cannot be interpreted as an integer
m.pop(1)
'hi'
m.pop()
'anything'
m
[12, 'hello', 2.3, 500, 'new value', 'abc', 'k', 'j', 'x', 'y']
mp=m.pop()
mp
'y'
mp(2)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    mp(2)
TypeError: 'str' object is not callable
mp.pop(2)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    mp.pop(2)
AttributeError: 'str' object has no attribute 'pop'
m.pop(2)
2.3
m
[12, 'hello', 500, 'new value', 'abc', 'k', 'j', 'x']
m.clear()
m
[]
n=[12,53,26,900]
n.reverse()
n
[900, 26, 53, 12]
n.sort()
n
[12, 26, 53, 900]
max9n0
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    max9n0
NameError: name 'max9n0' is not defined
max(n)
900
min(n)
12
m=[2,'hi',2.3,500,'new value']
m
[2, 'hi', 2.3, 500, 'new value']
m.index('hi')
1
m.split(2)
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    m.split(2)
AttributeError: 'list' object has no attribute 'split'
m[1][0]
'h'
m[1]
'hi'
######################################################
t=43,23,'abc',5+3j
type(t)
<class 'tuple'>
len(t)
4
t.index('abc')
2
t[0]
43
t[:2]
(43, 23)
t[0][1]
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    t[0][1]
TypeError: 'int' object is not subscriptable
t[0]=t[1]
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    t[0]=t[1]
TypeError: 'tuple' object does not support item assignment
t[0]=42
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    t[0]=42
TypeError: 'tuple' object does not support item assignment
del t[1]
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    del t[1]
TypeError: 'tuple' object doesn't support item deletion
t
(43, 23, 'abc', (5+3j))
k=(12,32,19,(5,'abc,5.5'),100)
type(k)
<class 'tuple'>
k[3:4:]
((5, 'abc,5.5'),)
k[3]
(5, 'abc,5.5')
k[3][1]
'abc,5.5'
k[3][1][1]
'b'
k=(12,32,19,(5,'abc',5.5),100)
k[3]
(5, 'abc', 5.5)
t
(43, 23, 'abc', (5+3j))
###################################
s={1,2,4,1,5,3,}
type(s)
<class 'set'>
print(s)
{1, 2, 3, 4, 5}
s[0]
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
s[0:3]
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    s[0:3]
TypeError: 'set' object is not subscriptable
ts
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    ts
NameError: name 'ts' is not defined. Did you mean: 't'?
s
{1, 2, 3, 4, 5}
s2={23,41,'kj'}
type(s2)
<class 'set'>
s2={32,43,1,4}
s.ontesection(s2)
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    s.ontesection(s2)
AttributeError: 'set' object has no attribute 'ontesection'. Did you mean: 'intersection'?
s.intersection(s2)
{1, 4}
s.union(s2)
{32, 1, 2, 3, 4, 5, 43}
s.inersection(s2)
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    s.inersection(s2)
AttributeError: 'set' object has no attribute 'inersection'. Did you mean: 'intersection'?
s2={32,43,1,4}
s.add(100)
s
{1, 2, 3, 4, 5, 100}
s.discard(100)
s
{1, 2, 3, 4, 5}
s.remove(3)
s
{1, 2, 4, 5}
s.pop(4)
Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    s.pop(4)
TypeError: set.pop() takes no arguments (1 given)
s1={44,22,33}
s.update(s1)
s
{1, 2, 33, 4, 5, 22, 44}
s.clear()
s
set()
#max ,min,len

