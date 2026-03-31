'''import random
print(random.random())
print(random.randint(1,6)'''

import random
random.seed(5)
l=['java','python','c++','html','css']
print(random.choice(l))
print(random.choices(l,k=4))


