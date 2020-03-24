from math import sqrt

def f(x):
    return x*x

def F(x):
    return x**3 / 3

a,b = map(int, input('Введите диапазон интегрирования:\n    ').split())
n = list(map(int, input('Введите количество интервалов\n    ').split()))

print('          Метод         │', end = '')
for n1 in n:
    print('{:^13d}│'.format(n1), end = '')
print()

print(' Средние прямоугольники │', end = '')
for n1 in n:
    h = (b - a) / n1
    I = f(a + 0.5 * h)
    for k in range(1, n1):
        I += f(a + 0.5*h + k*h)
    I *= h
    print('{:^13f}│'.format(I), end = '')
print()

print('          Буля          │',end = '')
for n1 in n:
    I = 0
    h = (b - a) / n1
    for i in range(n1//4):
        I += 7 * f(a + 4*i*h) +\
        32 * f(a + 4*i*h + h) +\
        12 * f(a + 4*i*h + 2*h) +\
        32 * f(a + 4*i*h + 3*h) +\
        7 * f(a + 4*i*h + 4*h)
    I *= 2 * h / 45
    print('{:^13f}│'.format(I), end = '')
print()

eps = float(input('Введите точность вычисления интеграла функции\
 методом средних прямоугольников:\n    '))

I = 0
t = (b - a) * (b - a)
n = 1
while abs(t - I) > eps:
    n *= 2
    h = (b - a) / n
    I = t
    t = f(a + 0.5 * h)
    for k in range(1, n):
        t += f(a + 0.5*h + k*h)
    t *= h
print()

dt = F(b) - F(a)
print('Вычисленное значение интеграла указанным методом:\n    {:^7f}\
\nВычислено при кол-ве интервалов равном:\n    {:^6d}\
'.format(t , n))
print('Истинное значение интеграла равно:\n    {:^7f}'.format(dt))
print('Абсолютная погрешность: {:^7f}'.format( abs(dt - t) ))
print('Относительная погрешность: {:^7f}'.format( abs((dt - t) / dt)))
