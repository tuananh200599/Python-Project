import  random
n = int(input('Nhap so phan tu : '))
array = random.sample(range(1,99),n)
max = 0
for item in array:
    if max < item:
        max = item
        print(array)
print('Max la: ', max)