#1
numbers = []
for i in range(5):
    number = int(input('Введіть число: '))
    numbers.append(number)
print(numbers)
#2
A = [1, 2, 3, 4, 5]
A.pop()
print(A)
#3
A = []
for i in range(10):
    number = int(input('Введіть число: '))
    A.append(number)
N = int(input('Введіть число N: '))
count = A.count(N)
print(f'Кількість повторень числа {N} у списку A: {count}')
#4
N = int(input('Введіть число N: '))
A = []
for i in range(N):
    num = int(input(f'Введіть число {i+1}: '))
    A.append(num)
A.reverse()
print(A)
#5
A = []
C = []
for i in range(5):
    num = int(input('Введіть число: '))
    A.append(num)
    if num > 5:
        C.append(num)
print('Список A:', A)
print('Список C:', C)
#6
N = int(input('Введіть число N: '))
A = []
for i in range(N):
    num = int(input(f'Введіть число {i+1}: '))
    A.append(num)
min_num = A[0]
max_num = A[0]
for num in A:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
print('Мінімальне число: ', min_num)
print('Максимальне число: ', max_num)
#7
text = input('Введіть текст: ')
count = 0
for char in text:
    if char.isdigit():
        count += 1
print('Кількість цифр у тексті: ', count)