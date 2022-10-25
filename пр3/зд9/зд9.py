n = int(input())
m = int(input())
k = int(input())
x = n*m
y = x - k
z = k/n
if z == (x - y):
    print ('Да')
else:
    print('Нет')