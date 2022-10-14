n = int(input('Введите размерность массива: '))
arr = []
for i in range(n):
    arr.append(float(input('Введите элемент массива: ')))
kmax = 0
imax = 0
for i in range(n):
    if arr[i] >= kmax:
        kmax = arr[i]
        imax = i
for i in range(n):
    if i > imax:
        arr[i] = 0
print('Исходный массива: ', arr)