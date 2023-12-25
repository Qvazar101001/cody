max = int(input())
num = 1
for i in range(2,11):
    x = int(input())
    if x > max:
        max = x
        num = i
print('максимальная скорость ', max)
print('номер ', num)
