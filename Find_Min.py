import random

n = int(input('Nhap so phan tu : '))
arrray = []
for item in range(n):
    a = float(random.uniform(1,99))
    arrray.append(a)
print('Arrray = ',arrray)
min = arrray[0]
for item in arrray:
    if item < min :
        min = item
print('Min la :',min)