Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d1={'name':['kashika','abc','def'],'Age':[10,5,2]}
type(d1)
<class 'dict'>
d1.get('name')
['kashika', 'abc', 'def']
d1.get('name')=[1]
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
d1[1]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d1[1]
KeyError: 1
d1['name']=[1]
d1
{'name': [1], 'Age': [10, 5, 2]}
d1
{'name': [1], 'Age': [10, 5, 2]}
d1={'name':['kashika','abc','def'],'Age':[10,5,2]}
d1
{'name': ['kashika', 'abc', 'def'], 'Age': [10, 5, 2]}
d1['name'][0]
'kashika'
d1['name'][0][2]
's'
d1['name']=='hello'
False
d2={'name':['hello']}
d1{'name'}=d1{'name'},d2{'name'}
SyntaxError: invalid syntax
d1['name']=d1['name'],d2['name']
d1
{'name': (['kashika', 'abc', 'def'], ['hello']), 'Age': [10, 5, 2]}
d2={'name':'hello'}
d1['name']=d1['name'],d2['name']
d1
{'name': ((['kashika', 'abc', 'def'], ['hello']), 'hello'), 'Age': [10, 5, 2]}
d1['name']=d1['name'],d2['name']
d1
{'name': (((['kashika', 'abc', 'def'], ['hello']), 'hello'), 'hello'), 'Age': [10, 5, 2]}
d2={'name':'hello'}
d1['name']=d1['name'],d2['name']
print(d1)
{'name': ((((['kashika', 'abc', 'def'], ['hello']), 'hello'), 'hello'), 'hello'), 'Age': [10, 5, 2]}
d1={'name':['kashika','abc','def'],'Age':[10,5,2]}
d1
{'name': ['kashika', 'abc', 'def'], 'Age': [10, 5, 2]}
d2={'name':'hi'}
d1['name']=d1['name'],d2['name']
d1
{'name': (['kashika', 'abc', 'def'], 'hi'), 'Age': [10, 5, 2]}
d1.pop('name','hi')
(['kashika', 'abc', 'def'], 'hi')
d1.pop('name',none)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    d1.pop('name',none)
NameError: name 'none' is not defined. Did you mean: 'None'?
d1.pop('name','none')
'none'
d1.pop('name','def')
'def'
d1.pop('name','hi')
'hi'
d1
{'Age': [10, 5, 2]}
d1.pop('Age','5')
[10, 5, 2]
KeyboardInterrupt
d1.pop('Age',5)
5
d1
{}
d1={'name':['kashika','abc','def'],'Age':[10,5,2]}
dict.pop('name','def')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    dict.pop('name','def')
TypeError: descriptor 'pop' for 'dict' objects doesn't apply to a 'str' object
dict.pop('name',abc)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    dict.pop('name',abc)
NameError: name 'abc' is not defined. Did you mean: 'abs'?
dict.pop('name',def)
SyntaxError: invalid syntax
d1['name']=d1['Name']
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    d1['name']=d1['Name']
KeyError: 'Name'
d1['name']=d1['Name']
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    d1['name']=d1['Name']
KeyError: 'Name'
d1['name']=d1['Name']
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    d1['name']=d1['Name']
KeyError: 'Name'
d1
{'name': ['kashika', 'abc', 'def'], 'Age': [10, 5, 2]}
d1['name']=d1['Name']
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    d1['name']=d1['Name']
KeyError: 'Name'
d1['Name']=d1['name']
d1
{'name': ['kashika', 'abc', 'def'], 'Age': [10, 5, 2], 'Name': ['kashika', 'abc', 'def']}
d1
{'name': ['kashika', 'abc', 'def'], 'Age': [10, 5, 2], 'Name': ['kashika', 'abc', 'def']}
del d1['name']
d1
{'Age': [10, 5, 2], 'Name': ['kashika', 'abc', 'def']}
