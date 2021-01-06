import random

print('1. Tao snguyen random')
n = random.randrange(50,1000)
print('n = ' , n)
print('2. Sinh random 1list Snguyen')
list_int = random.sample(range(-1000,1000),n)
print('List-int = ',list_int)
print('3. Sinh random 1list sthuc')
list_float =[]
for item in range(n):
    a = float(random.uniform(-1000,1000))
    list_float.append(a)
print('List-float = ',list_float)