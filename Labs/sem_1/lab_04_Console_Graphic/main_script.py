'''
Лабораторная работа № 4
Построение графиков функций

Данная программа строит график функции
Переменные:
    y1, y2, y, dy - диапазон, текущее значение и шаг аргумента
    linesNum - количество засечек
    z_min, z_max - наим и наиб значение функций на отрезке
    z - текущ значения функций
    delta - расстояние между засечками
    numsPerPoint - связь между числами и ячейками
    axisValues - значения над засечками
    isYAxisNeeded - попала ли ось Y в диапазон значений функций
    curSectStr, outStr - строка пи текущем значении и строка, подлежащая выводу
    FuncPointNum - Положение точки функции при текущем Y на экране
'''

from math import sqrt

graphicFieldSize = 80

y1, y2, dy = map(float, input("Введите диапазон значений\
 аргумента и его шаг:\n    ").split())
linesNum = int(input('Введите количество засечек:\n    ')) - 1

if linesNum == 6:
    graphicFieldSize = 78
elif linesNum == 7:
    graphicFieldSize = 77

y = y1
z_min = z_max = False
while y <= y2+0.01:
    z = 2 * y**3 + 3 * y**2 - 6 * y + 1.5
    if z_max == False or z > z_max:
        z_max = z
    if z_min == False or z < z_min:
        z_min = z
    y += dy
delta = graphicFieldSize/(linesNum)-1
numsPerPoint = (z_max - z_min)/graphicFieldSize
outStr = '     z2   '
axisValues = z_min
for i in range(linesNum+1):
    if abs(axisValues) >= 100:
        curSectStr = '{: <2.1e}'.format(axisValues)
    elif abs(axisValues) < 10:
        curSectStr = '{: <2.1f}'.format(axisValues)
    else:
        curSectStr = '{: <2d}'.format(int(axisValues))
    outStr += curSectStr + ' '*int(delta+1 - len(curSectStr))
    axisValues += numsPerPoint*(delta+2)
print(outStr)

isYAxisNeeded = z_min <= 0 and z_max >= 0
outStr = '    y     '
if isYAxisNeeded:
    curSectStr = ('┴'+'─'*int(delta))*(linesNum) + '┴'
    axisPointN = int(abs(z_min)/(numsPerPoint))
    if curSectStr[axisPointN] == '┴':
        outStr += curSectStr[:axisPointN] + '┼' + curSectStr[axisPointN+1:]
    else:
        outStr += curSectStr[:axisPointN] + '┬' + curSectStr[axisPointN+1:]
else:
    outStr += ('┴'+'─'*int(delta))*(linesNum) + '┴'
print(outStr)

y = y1
while y <= y2 + 0.01:
    outStr = '{: ^9.2f}'.format(y)
    outStr += ' '*(10-len(outStr))
    z = 2 * y**3 + 3 * y**2 - 6 * y + 1.5

    curSectStr = ' '*graphicFieldSize

    FuncPointNum = int(abs(z - z_min)/(numsPerPoint))
    curSectStr = curSectStr[:FuncPointNum] + '*' + curSectStr[FuncPointNum+1:]
    if isYAxisNeeded:
        axisPointN = int(abs(z_min)/(numsPerPoint))
        if curSectStr[axisPointN] != ' ':
            outStr += curSectStr[:axisPointN] + 'x' + curSectStr[axisPointN+1:]
        else:
            outStr += curSectStr[:axisPointN] + '│' + curSectStr[axisPointN+1:]
    else:
        outStr += curSectStr
    print(outStr)
    y += dy
