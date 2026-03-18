
'''
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
'''
'''
if '+' in exp:
    a,b=exp.split('+')
    print((add(int(a),int(b))
elif '-' in exp:
    a,b=exp.split('-')
    print((add(int(a),int(b))
elif '*' in exp:
    a,b=exp.split('*')
    print((add(int(a),int(b))
elif '/' in exp:
    a,b=exp.split('/')
    print((add(int(a),int(b))
elif '%' in exp:
    a,b=exp.split('%')
    print((add(int(a),int(b))                     
'''

l=[1,2.4,'djklf',[1,2,3],(1,2,3),{2,3},{"k1":"v1"}]

l=[]
l=list()
a=[1,2,3]
b=[2,3,4]

names=['teja','naga','anil','kumar']


a,b,c=[10,20,30]

a,b,c,d=names

names.append('varun')

id(names)

names.extend(["bhanu","aravind","kiran","bhavana"])

names.insert(1, "prasana")

names.pop()

names.pop(2)

names.remove('bhanu')

del names[3]

names.clear()

id(names)


products=(['laptops',56000],
          ['airpods',30000],
          ['mouse',700])

def view_products():
    print('Product Name' .ljust(15,''),'prices')
    for i in products:
        print(i[0].ljust(15,''),i[1])
