'''import sys
print(sys.argv)
print(sys.path)
print(sys.version)

print('start')
print(sys.exit())
print('end')'''


'''import platform
print(platform.system())
print(platform.release())
print(platform.processor())'''

'''import math
print(math.pi)
print(math.e)

print(math.sqrt(36))
print(math.pow(3,4))
print(math.ceil(12.000001))
print(math.floor(12.999999))
print(round(12.999))
print(abs(-12))
print(math.fabs(-12))
print(math.factorial(5))
print(math.gcd(12,8))
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))'''

'''import random
l=[9,2,3,4,5,6]
random.shuffle(l)
print(l)'''

'''import collections
s='python programming'
l=[1,2,3,12,34,1,1,2,3,4,2,3]
r='this is that that is this'.split()
res=collections.Counter(s)
res1=collections.Counter(l)
res2=collections.Counter(r)
print(res)
print(res1)
print(res2)'''

'''s='python programming'
res={}
for i in s:
    if i in res:
        res[i]+=1
    else:
        res[i]=1

print(res)'''

'''import collections
s='python programming'
res=collections.defaultdict(int)
for i in s:
    res[i]=res[i]+1
print(res)'''

'''import collections
q=collections.deque([])
q.append(20)
q.append(30)
q.append(40)
q.append(50)
q.append(60)
q.popleft()
q.popleft()
q.popleft()
q.append(10)
q.append(90)
print(q)'''

'''import collections
q=collections.deque([])
q.appendleft(20)
q.appendleft(30)
q.appendleft(40)
q.appendleft(50)
q.appendleft(60)
q.pop()
q.pop()
q.pop()
q.appendleft(10)
q.appendleft(90)
print(q)'''

'''from itertools import combinations,permutations
s='abc'
print(list(combinations(s,3)))
print(list(permutations(s,3)))'''

