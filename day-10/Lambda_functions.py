'''
def wish(name):
    return f'hello{name}, Welcome To Python'
wishl= lambda name: f'hello{name}, Welcome To Python'
print(wish("teja"))
print(wish("anil"))
'''


'''
def add(a,b,c):
    return (a+b+c)/3
add1=lambda a,b,c: (a+b+c)/3

print(add(1,2,3))
print(add1(6,7,8))

'''


'''
def iseven(n):
    if n%2==0:
        return "Even"
    else:
        return "odd"

iseven1=lambda n: "Even" if n%2==0 else "odd"
print(iseven(19))
print(iseven1(18))
'''


'''
def greater(a,b):
    if a>b:
        return a
    else:
        return b

greater1=lambda a,b: a if a>b else b
print(greater(4,2))
print(greater1(2,6))
'''

'''
def isvowel(a):
    if a in vol:
        return "vol"
    else:
        return "con"
isvowel1=lambda a: "vol"  if a in vol else "con"
vol="aeifknc"
print(isvowel('a'))
print(isvowel1('k'))
'''

'''
def fun(l):
    for i in range(len(l)):
        l[i]=l[i].title()
    return l
l=['teja','anil','kumar','varun','sanju']
res=list(map(lambda i:i.title(),l))

print(fun(l))
print(res)
'''

'''
def fun(l):
    res=[]
    for i in range(len(l)):
        if l[i]%3==0:
            res.append(l[i])
    return res

l=[10,20,30,40,50,60,70,80,90,100]
res=list(filter(lambda i:i%3==0, l))

print(fun(l))
print(res)
'''
'''
l={'laptop':True,
   'iphone':False,
   'mouse':True,
   'tablet':False,
   'charger':True
}

res=list(filter(lambda i:l[i],l))

print(res)

[1,0,2,3,5,7,4,5,3,6,8,7,9,6,2]
'''

'''
from functools import reduce

l=[1,3,4,2,5,67,8,9,3,6,2,8]

res=reduce(lambda a,b:a*b,l)

print(res)
'''


'''
from functools import reduce

l=['python','java','c','c++','reactjs']

res=reduce(lambda a,b:a+'   '+b,l)

print(res)
'''

'''
d={'apple':30,
    'banana':50,
    'papaya':40,
    'mango':60,
    'graps':70}
print(dict(sorted(d.items())))

print(dict(sorted(d.items(),key=lambda i:i[1])))

print(dict(sorted(d.items(),reverse=True)))

print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))
'''
