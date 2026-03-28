'''
a=[]
for i in range(1,10):
    if i%2==0:
        a.append(i)
print(a)

l=[i for i in range(1,100) if i%2==0]
print(l)

l=[i for i in range(1,100,3)]
print(l)


l=[i*2 for i in range(1,100)]
print(l)
'''

'''
s='python programming'
vol='aeiouAEIOU'

l=[i for i in s if i in vol]
print(l)


l=['*' if i in vol else i for i in s]
print(l)
'''

'''
l=[3,4,2,1,7,6,5,4,8,9,3,6,2]
rl=[0 if i%2==0 else i for i in l]
print(rl)
'''

'''
l=[2,5,4,7,6,2,3,7,1,7,1,5,4,8]
rl={i: l.count(i) for i in l}
print(rl)
'''
'''
def reels():
    r=['1..100','101..200','201..300','301..400','401..500','501..600']
    for i in r:
        yield i

scroll=reels()

print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
'''

def display():
    yield "pfs-50"
    yield "pfs-49"
    yield "pfs-48"
    yield "pfs-47"
    yield "pfs-46"
    yield "pfs-45"
    yield "pfs-44"
leave=display()

for i in range(7):
    print(next(leave))

    
