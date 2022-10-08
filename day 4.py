Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d1=
SyntaxError: invalid syntax
d1=
SyntaxError: invalid syntax
d1={'name':['kashika','abc','def'],'Age':[10,10,10]}
type(d1)
<class 'dict'>
len(d1)
2
d1[0]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    d1[0]
KeyError: 0
d1['name']
['kashika', 'abc', 'def']
d1['name'][0]
'kashika'
d1['name'][-1]
'def'
d1['name'][:2:]
['kashika', 'abc']
d1
{'name': ['kashika', 'abc', 'def'], 'Age': [10, 10, 10]}
d1.keys()
dict_keys(['name', 'Age'])
d1.values()
dict_values([['kashika', 'abc', 'def'], [10, 10, 10]])
d1.values[0]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d1.values[0]
TypeError: 'builtin_function_or_method' object is not subscriptable
d1.items()
dict_items([('name', ['kashika', 'abc', 'def']), ('Age', [10, 10, 10])])
d1.items()[0]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d1.items()[0]
TypeError: 'dict_items' object is not subscriptable

d1['Age'][2]
10
print(d1)
{'name': ['kashika', 'abc', 'def'], 'Age': [10, 10, 10]}
d1['phone']=[2222222222,4444,866666666]
d1
{'name': ['kashika', 'abc', 'def'], 'Age': [10, 10, 10], 'phone': [2222222222, 4444, 866666666]}
d1['name'][0]
'kashika'
d1['name'][-1:-8:-1]
['def', 'abc', 'kashika']
d1['name'][0][-1:-8:-1]
'akihsak'
d1['name'][0][-1]
'a'
d1['name'][0][0]
'k'
d1['name']=['akash']
d1
{'name': ['akash'], 'Age': [10, 10, 10], 'phone': [2222222222, 4444, 866666666]}
d1['name']=['kashika','abc','def']
d1
{'name': ['kashika', 'abc', 'def'], 'Age': [10, 10, 10], 'phone': [2222222222, 4444, 866666666]}
d1['name'][0]=['kanika']
d1
{'name': [['kanika'], 'abc', 'def'], 'Age': [10, 10, 10], 'phone': [2222222222, 4444, 866666666]}
d1['name'][0]='kanika'
d1
{'name': ['kanika', 'abc', 'def'], 'Age': [10, 10, 10], 'phone': [2222222222, 4444, 866666666]}
d1['name'][3]='kashika'
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    d1['name'][3]='kashika'
IndexError: list assignment index out of range
d1['name'][]='kashika'
SyntaxError: invalid syntax
d1['phone']=[]
d1
{'name': ['kanika', 'abc', 'def'], 'Age': [10, 10, 10], 'phone': []}
del d1['phone']
d1
{'name': ['kanika', 'abc', 'def'], 'Age': [10, 10, 10]}
d1='upper'
d1
'upper'
d1={'name':['kashika','abc','def'],'Age':[10,10,10]}
d1
{'name': ['kashika', 'abc', 'def'], 'Age': [10, 10, 10]}
add()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    add()
NameError: name 'add' is not defined
d1.get('email')
d1
{'name': ['kashika', 'abc', 'def'], 'Age': [10, 10, 10]}
d1.get('name')
['kashika', 'abc', 'def']
a=20
b='ML'
print(a,b)
20 ML
print(a,,b)
SyntaxError: invalid syntax
print(a,b,sep='  , ')
20  , ML
print(a,b,sep='')
20ML
print(a,b,sep='@')
20@ML
print(a)
20
print(b)
ML

= RESTART: C:/Users/91759/Desktop/ML Trainig/day4editor.py
20
ML

= RESTART: C:/Users/91759/Desktop/ML Trainig/day4editor.py
20###ML

= RESTART: C:/Users/91759/Desktop/ML Trainig/day4editor.py
20
ML

= RESTART: C:/Users/91759/Desktop/ML Trainig/day4editor.py
20###

= RESTART: C:/Users/91759/Desktop/ML Trainig/day4editor.py
20###ML
import a
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    import a
ModuleNotFoundError: No module named 'a'
a=input('enter you Name:')
enter you Name:kashika
a
'kashika'
a[0]
'k'
b=input('enter two no.x:')
enter two no.x:3
c=input('y:')
y:5
add=b+c
add
'35'
a=int(input('enter 1st np x:'))
enter 1st np x:5
b=int(input('enter 2st np y:'))
enter 2st np y:7
add=a+b
add
12

= RESTART: C:/Users/91759/Desktop/ML Trainig/day4editor.py
20###ML
age:45
Traceback (most recent call last):
  File "C:/Users/91759/Desktop/ML Trainig/day4editor.py", line 6, in <module>
    if age <18:
NameError: name 'age' is not defined


= RESTART: C:/Users/91759/Desktop/ML Trainig/day4editor.py
20###ML
age:45
koin gift nahi hai


= RESTART: C:/Users/91759/Desktop/ML Trainig/day4editor.py
20###ML
age:18
a gift
a task

= RESTART: C:/Users/91759/Desktop/ML Trainig/day4editor.py
20###ML
age:18
a gift
a task

= RESTART: C:/Users/91759/Desktop/ML Trainig/day4editor.py
20###ML
age:20
a gift
a task

= RESTART: C:/Users/91759/Desktop/ML Trainig/day4editor.py
20###ML
age:sick
Traceback (most recent call last):
  File "C:/Users/91759/Desktop/ML Trainig/day4editor.py", line 5, in <module>
    age=int (input('age:'))
ValueError: invalid literal for int() with base 10: 'sick'

= RESTART: C:/Users/91759/Desktop/ML Trainig/day4editor.py
Traceback (most recent call last):
  File "C:/Users/91759/Desktop/ML Trainig/day4editor.py", line 2, in <module>
    if today=='saturday':
NameError: name 'today' is not defined

= RESTART: C:/Users/91759/Desktop/ML Trainig/day4editor.py
day:sunday
Traceback (most recent call last):
  File "C:/Users/91759/Desktop/ML Trainig/day4editor.py", line 5, in <module>
    if condition=='sick':
NameError: name 'condition' is not defined

= RESTART: C:/Users/91759/Desktop/ML Trainig/day4editor.py
day:sunday
dsick
Task Rest


= RESTART: C:/Users/91759/Desktop/ML Trainig/day4editor.py
today:saturday
cond:sick
Traceback (most recent call last):
  File "C:/Users/91759/Desktop/ML Trainig/day4editor.py", line 3, in <module>
    if today=='saturday':
NameError: name 'today' is not defined

= RESTART: C:/Users/91759/Desktop/ML Trainig/day4editor.py
today:saturday
cond:sick
half day work

= RESTART: C:/Users/91759/Desktop/ML Trainig/day4editor.py
today:saturday
half day work

= RESTART: C:/Users/91759/Desktop/ML Trainig/day4editor.py
today:sunday
cond:take rest
party

= RESTART: C:/Users/91759/Desktop/ML Trainig/day4editor.py
today:sunday
cond:sick
Task Rest
range(0,11)
range(0, 11)
list(range(0,11))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(11))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(0,11,2))
[0, 2, 4, 6, 8, 10]
list(range(2,100,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
list(range(2,101,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
