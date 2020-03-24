'''
Лабораторная работа №7-1 - Матрицы

Данная программа создает вектор из ненулевых элементов матрицы при обходе
по столбцам и заменяет третий отрицательный элемент вектора суммой предыдущих
элементов или оповещает об отсутствии такого элемента

Переменные
    R - Искомый вектор
    Z - Входная матрица
    n, m - количество строк и столбцов в матрице, соответственно
    i, j - счетчики
    otrElemCount - количество отрицательных элементов
    sumBeforeThirdOtrElem - сумма элементов, удовлетворяющая условию

'''

R = []
Z = []

n, m = map(int, input('Введите размеры исходной матрицы N и M:\n    ').split())

print('Введите  исходную матрицу Z(N, M) построчно:')

for i in range(n):
    Z.append(list(map(int, input('    ').split())))

otrElemCount = 0
sumBeforeThirdOtrElem = 0
for i in range(m):
    for j in range(n):
        if Z[j][i] != 0:
            R.append(Z[j][i])
            if otrElemCount < 3:
                if otrElemCount != 2 or Z[j][i] > 0:
                    sumBeforeThirdOtrElem += Z[j][i]
                if Z[j][i] < 0:
                    otrElemCount += 1
            if Z[j][i] < 0 and otrElemCount == 3:
                otrElemCount += 1
                R[len(R)-1] = sumBeforeThirdOtrElem

if otrElemCount < 3:
    print('\nВ векторе R, составленном из ненулевых элементов \
матрицы, выбранных\nв порядке обхода по столбцам, \
менее\n 3-х отрицательных элементов!',end='\n\n')
else:
    print('\nВ векторе R, составленном из ненулевых элементов \
матрицы, выбранных\nв порядке обхода по столбцам, \
3 отрицательный элемент заменен \
суммой\nпредыдущих элементов',end='\n\n')
print('Созданный вектор R:', end='\n    ')

for i in R:
    print(i, end=' ')
print(end = '\n\n')

print('Исходная матрица:', end = '\n    ')
for i in Z:
    for j in i:
        print(j, end = ' ')
    print('\n    ', end ='')
