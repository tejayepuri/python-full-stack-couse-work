Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> min_balance=5000
>>> cur_balance=2000
>>> if cur_balance<min_balance:
...     print("send messgae and cut some amount")
... 
...     
send messgae and cut some amount
>>> 
>>> min_chaege=20
>>> cur_charge=100
>>> if cur_charge<min_charge:
...     print("send alert message to charge the phone")
... 
...     
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    if cur_charge<min_charge:
NameError: name 'min_charge' is not defined. Did you mean: 'min_chaege'?
>>> min_chaege=20
... cur_charge=15
... if cur_charge<min_charge:
...     print("send alert message to charge the phone")
...     
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> '''min_chaege=20
... cur_charge=15
... if cur_charge<min_charge:
...     print("send alert message to charge the phone")'''
'min_chaege=20\ncur_charge=15\nif cur_charge<min_charge:\n    print("send alert message to charge the phone")'
>>> 
>>> data= ('user@gmail.com',)
>>> data= ('user@gmail.com','user@123')
>>> mail=input("enter the email:")
enter the email:user@gmail.com
>>> password=input("user@123:")
user@123:
>>> 
>>> if data == (mail,password):
...     print("login successful")
... else:
...     print("invalid login")
... 
...     
invalid login
fruits= ["mango","apple","banana","papaya"]
search_item=input("search here:")
search here:mango

if search_item in fruis:
    print(f"{search_item} found! buy now")
else:
    print(f"(search_item) is out of stack, we will notify when it is available")

    
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    if search_item in fruis:
NameError: name 'fruis' is not defined. Did you mean: 'fruits'?
fruits= ["mango","apple","banana","papaya"]
search_item=input("search here:")
search here:mango

if search_item in fruits:
    print(f"{search_item} found! buy now")
else:
    print(f"(search_item) is out of stack, we will notify when it is available")
    
SyntaxError: multiple statements found while compiling a single statement
fruits= ["mango","apple","banana","papaya"]
search_item=input("search here:")

if search_item in fruits:
    print(f"{search_item} found! buy now")
else:
    print(f"(search_item) is out of stack, we will notify when it is available")
    
SyntaxError: multiple statements found while compiling a single statement
search_item=input("search here:")

if search_item in fruits:
    print(f"{search_item} found! buy now")
else:
    print(f"(search_item) is out of stack, we will notify when it is available")
    
SyntaxError: multiple statements found while compiling a single statement

if 0<=time<=6:
    print("bus2\nbus7\nbus10\nbus6")
elif 7<=time<=18:
    print("bus5\nbus17\nbus18")
elif:
    
SyntaxError: incomplete input
if 0<=time<=6:
    print("bus2\nbus7\nbus10\nbus6")
elif 7<=time<=18:
    print("bus5\nbus17\nbus18")
elif 18<=time<=24:
    print("bus90\nbus80\nbus70")
else:
    print("enter the time in given range")

    
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    if 0<=time<=6:
NameError: name 'time' is not defined
