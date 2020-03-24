'''
Лабораторная работа № 2
Нахождение основных параметров треугольника по заданным координатам вершин

Данная программа:
    1. Находит длины сторон треугольника
    2. Находит длину высоты, проведенной из меньшего угла треугольника
    3. Проверяет, является ли треугольник прямоугольным
    4. Проверяет, находится ли задаваемая пользователем точка внутри треугольника
       и находит расстояние до ближайшей прямой, содержащей сторону треугольника,
       если точка внутри треугольника

Используемые переменные:
    xA, yA, xB, yB, xC, yC - координаты, соответственно, точек A, B и C
    (вершин треугольника)
    SideAB, SideBC, SideAC - Длина сторон AB, BC и AC, соответственно

    lenAB2, lenAC2, leBC2 - квадраты длин сторон AB, AC и BC, соответсвенно

    halfPerimetr - полупериметр треугольника
    triangleSquare - площадь треугольника
    triangleHeight - высота треугольника

    isRectangular - является ли треугольник прямоугольным

    is_inside_AB, is_inside_AC, is_inside_BC - Полуплоскость в которой лежит
    точка, относительно AB, AC и BC

    x0, y0 - координаты точки, которую следует проверить
    dAB, dBC, dAC - расстояние от точки до прямых AB, BC и AC, соответственно
    kAB, kBC, kAC - углы наклона прямых AB, BC и AC, соответственно
    bAB, bBC, bAC - коэффициенты b прямых AB, BC и AC, соответственно

Тестовый пример:
  X1, Y1: 0 0
  X2, Y2: 4 0
  X3, Y3: 0 3
Длины сторон треугольника : 4.00000 5.00000 3.00000

Высота равна 4.00000
Это прямоугольный треугольник

Координаты точки:
  X, Y: 1 1
Точка лежит внутри треугольника
Расстояние до ближайшей стороны равно: 1.00000
'''

from math import sqrt

print('Введите координаты вершин треугольника:');
xA, yA = map(int, input('  Xa, Ya:\n    ').split());
xB, yB = map(int, input('  Xb, Yb:\n    ').split());
xC, yC = map(int, input('  Xc, Yc:\n    ').split());

#Вычисление длин сторон треугольника
sideAB = sqrt((xA-xB)**2 + (yA-yB)**2);
sideBC = sqrt((xB-xC)**2 + (yB-yC)**2);
sideAC = sqrt((xA-xC)**2 + (yA-yC)**2);
if(sideAB < sideBC + sideAC and sideBC < sideAB + sideAC and
sideAC < sideAB + sideBC):
    print('Длины сторон треугольника равны :\n' +
    'AB : {:.5f}\nBC : {:.5f}\nAC : {:.5f}\n'.format(sideAB, sideBC, sideAC));

    #Нахождение высоты треугольника

    halfPerimetr = (sideAB + sideAC + sideBC) / 2;
    triangleSquare = sqrt(halfPerimetr * (halfPerimetr - sideAB) *
                     (halfPerimetr - sideAC) * (halfPerimetr - sideBC))

    if(sideBC <= sideAB and sideBC <= sideAC):
        triangleHeight = 2 * triangleSquare / sideBC;
    elif(sideAC <= sideAB and sideAC <= sideBC):
        triangleHeight = 2 * triangleSquare / sideAC
    else:
        triangleHeight = 2 * triangleSquare / sideAB

    print("Высота, проведенная из вершины с" +
          " меньшим углом равна {:.5f}\n".format(triangleHeight))

    #Проверка, что треугольник прямоугольный
    lenAB2 = (xA-xB)**2 + (yA-yB)**2
    lenBC2 = (xB-xC)**2 + (yB-yC)**2
    lenAC2 = (xA-xC)**2 + (yA-yC)**2

    isRectangular = ((lenAB2 + lenBC2 - lenAC2) *
                    (lenAB2 + lenAC2 - lenBC2) *
                    (lenBC2 + lenAC2 - lenAB2) == 0)

    if (isRectangular):
        print("Это прямоугольный треугольник\n")
    else:
        print("Это не прямоугольный треугольник\n")

    #Проверка точки с заданными координатами
    print('Введите координаты точки:');
    x0, y0 = map(int, input('  X, Y:\n    ').split());

    is_inside_AB = (xA - x0) * (yB - yA) - (xB - xA) * (yA - y0)
    is_inside_BC = (xB - x0) * (yC - yB) - (xC - xB) * (yB - y0)
    is_inside_AC = (xC - x0) * (yA - yC) - (xA - xC) * (yC - y0)

    if((is_inside_AB <= 0 and is_inside_BC <= 0 and is_inside_AC <=0) or
    (is_inside_AB >= 0 and is_inside_BC >= 0 and is_inside_AC >=0)):
        print('Точка лежит внутри треугольника');

        if(xB - xA == 0):
            dAB = abs(x0 - xA)
        else:
            kAB = (yB - yA) / (xB - xA)
            bAB = (yA * xB - xA * yB) / (xB - xA)
            dAB = abs(kAB * x0 - y0 + bAB) / sqrt(kAB**2 + 1)

        if(xC - xB == 0):
            dBC = abs(x0 - xC)
        else:
            kBC = (yC - yB) / (xC - xB)
            bBC = (yB * xC - xB * yC) / (xC - xB)
            dBC = abs(kBC * x0 - y0 + bBC) / sqrt(kBC**2 + 1)

        if(xC - xA == 0):
            dAC = abs(x0 - xA)
        else:
            kAC = (yC - yA) / (xC - xA)
            bAC = (yA * xC - xA * yC) / (xC - xA)
            dAC = abs(kAC * x0 - y0 + bAC) / sqrt(kAC**2 + 1)
        print('Расстояние до ближайшей стороны' +
        ' равно: {:.5f}'.format(min(dAB, dBC, dAC)))

    else:
        print('Точка лежит вне треугольника');
else:
    print("Эти точки не образуют треугольника!")
