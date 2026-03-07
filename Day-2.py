Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name=input("enter then name):0
           
SyntaxError: incomplete input
age=int(input()):
           
SyntaxError: incomplete input
age=int(input("enter the age:'))
              
SyntaxError: incomplete input
age=int(input("enter the age:"))
              
enter the age:25
age
              
25
25
              
25
25
              
25
age
              
25
price=float(input("enter the price:"))
              
enter the price:44.5
price
              
44.5
type
              
<class 'type'>
type(price)
              
<class 'float'>
names=input("enter the name:").split()
              
enter the name:tejs,venu,vignesh

names=input("enter the name:").split()
              
enter the name:tejs venu vignesh
split()
              
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    split()
NameError: name 'split' is not defined
names
              
['tejs', 'venu', 'vignesh']
numbers=map(int(input("enter the numbers:").split())

            names
            
SyntaxError: incomplete input
n
            
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    n
NameError: name 'n' is not defined
numbers=tuple(map(float,input("enter the numbers:").split()))
            
enter the numbers:3287893278
numbers
            
(3287893278.0,)
numbers=set(map(float,input("enter the numbers:").split()))
            
enter the numbers:87479823989
numbers
            
{87479823989.0}
numbers=set(map(int,input("enter the numbers:").split()))
            
enter the numbers:948993

numbers
            
{948993}
a,b,c=set(map(int,input("enter the numbers:").split()))
            
enter the numbers:
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a,b,c=set(map(int,input("enter the numbers:").split()))
ValueError: not enough values to unpack (expected 3, got 0)
a,b,c=set(map(int,input("enter the numbers:").split()))
            
enter the numbers:789
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a,b,c=set(map(int,input("enter the numbers:").split()))
ValueError: not enough values to unpack (expected 3, got 1)
a,b,c=set(map(int,input("enter the numbers:").split()))
            
enter the numbers:7,8,9
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a,b,c=set(map(int,input("enter the numbers:").split()))
ValueError: invalid literal for int() with base 10: '7,8,9'
a
            
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a
NameError: name 'a' is not defined
a,b,c=set(map(int,input("enter the numbers:").split()))
            
enter the numbers:6 7 8
a
            
8
>>> b
...             
6
>>> c
...             
7
>>> a
...             
8
>>> a,b,c=set(map(int,input("enter the numbers:").split()))
...             
enter the numbers:7 4 3
>>> c
...             
7
>>> numbers=set(map(float,input("enter the numbers:").split()))
...             
enter the numbers:9379379
>>> numbers
...             
{9379379.0}
>>> numbers=set(map(int,input("enter the numbers:").split()))
...             
enter the numbers:w498943
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    numbers=set(map(int,input("enter the numbers:").split()))
ValueError: invalid literal for int() with base 10: 'w498943'
>>> 98479794
...             
98479794
>>> names=set(map(input("enter the numbers:").split()))
...             
enter the numbers:
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    names=set(map(input("enter the numbers:").split()))
TypeError: map() must have at least two arguments.
>>> age=int(input())
...             
age=int(input())
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    age=int(input())
ValueError: invalid literal for int() with base 10: 'age=int(input())'
