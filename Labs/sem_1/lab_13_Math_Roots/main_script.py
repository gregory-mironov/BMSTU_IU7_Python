from time import perf_counter
from scipy.optimize import brentq#root_scalar

from math import fabs, sin
from sys import float_info

meps = float_info.epsilon
xtol = 1e-8
max_iter = 100
dx = 1e-2

def printMenu():
    print("\n  1. Вычислить корни функции\n  \
2. Изменить шаг\n  3. Изменить максимальное количество итераций\n  \
4. Изменить точность\n  0. Выход")

def printErrValues():
    print("  Расшифровка ошибок:\n    0. Нет ошибок\n\
    1. Превышено максимальное число итераций")

def printRes(num, method, a, b, x, fx, iterations, dt, err, showNum = True):
    if err == 0:
        print("  " + (" {:^7d} ".format(num) if showNum == True else " "*9) + \
        method + \
        "{:^9.3g}".format(a) + "{:^9.3g}".format(b) + \
        "{:^14f}".format(x) +  "{:^17e}".format(fx) + \
        "{:^12d}".format(iterations) + \
        "   {:^10f} ms".format(dt*1e3) + \
        "{:^14d}".format(0) + "\n")
    else:
        print("  " + (" {:^7d} ".format(num) if showNum == True else " "*9) + \
        method + \
        " {:^7.2g} ".format(a) + "{:^9.2g}".format(b) + \
        " "*59 + "{:^14d}".format(err) + "\n")

def resetH():
    global dx
    try:
        newdX = float(input("\n  Введите новый шаг:\n\n    "))
        if newdX > 0:
            dx = newdX
        else:
            print("\n  Ошибка ввода! Число должно быть положительным")
    except ValueError:
        print("\n  Ошибка ввода! Нужно вводить числа")

def resetXTol():
    global xtol
    try:
        newEps = float(input("\n  Введите новую точность \
нахождения корня:\n\n    "))
        if newEps > 0:
            xtol = newEps
        else:
            print("\n  Ошибка ввода! Число должно быть положительным")
    except ValueError:
        print("\n  Ошибка ввода! Нужно вводить числа")

def resetMaxIter():
    global max_iter
    try:
        newIter = float(input("\n  Введите новое количество итераций:\n\n    "))
        if newIter > 0:
            max_iter = int(newIter)
        else:
            print("\n  Ошибка ввода! Число должно быть положительным")
    except ValueError:
        print("\n  Ошибка ввода! Нужно вводить числа")

def test_func(x):
    return sin(x)#(x - 2)*(x + 4)*(x - 5)

def brent_dekker_method(func, init_x1, init_x2, max_iter):
    global xtol
    a = init_x1
    b = init_x2
    fa = func(a)
    fb = func(b)

    if fa == 0.:
        return [init_x1, fa, 1, 0]
    if fb == 0.:
        return [init_x2, fb, 1, 0]

    c = a
    fc = func(c)

    if fabs(fc) < fabs(fb):
        a = b
        b = c
        c = a

        fa = fb
        fb = fc
        fc = fa

    n_iter = 1
    while fabs(fa - fb) > xtol:
        if n_iter > max_iter:
            break
        delta = 0.5*xtol + 2.*meps*fabs(b)

        interval_hdist = (c - b)/2
        improve_dist = b - a

        if fb == 0. or fabs(interval_hdist) < delta:
            break

        if (fabs(improve_dist) > delta) & (fabs(fb) < fabs(fa)):
            if a == c:
                #Secant method
                s = b - fb*(b - a)/(fb - fa)
            else:
                #Inv_Quad_Interpolation
                d_pre = (fa - fb) / (a - b)
                d_blk = (fc - fb) / (c - b)
                s = b - fb * (fc * d_blk - fa * d_pre) / (d_blk * d_pre * (fc - fa))

            tmp_iprove_dist = s - b

            if not 2.*fabs(tmp_iprove_dist) < \
            min(fabs(improve_dist), 3.*fabs(interval_hdist) - delta):
            #Bisection method
                s = (b + c)/2

        else:
            #Bisection method
            s = (b + c)/2

        a = b
        fa = fb
        if fabs(tmp_iprove_dist) > delta:
            b = s
        else:
            b += tmp_iprove_dist if delta >= 0 else -tmp_iprove_dist
        fb = func(b)

        if fa*fb<0.:
            c = a
            fc = fa

        if fabs(fc) < fabs(fb):
            a = b
            b = c
            c = a

            fa = fb
            fb = fc
            fc = fa

        n_iter += 1

    return [b, fb, n_iter, 0 if n_iter <= max_iter else 1]

def CompareMethods():
    global dx, max_iter, meps
    try:
        isFounded = False
        solN = 1
        A, B = map(float, list(input('\n  Введите границы отрезка \
через пробел:\n\n    ').split()))
        xLeft = A
        while xLeft < B + meps:
            xRight = xLeft + min(dx, B - xLeft)
            if test_func(xLeft)*test_func(xLeft + dx) <= 0:
                if not isFounded:
                    print("\n  " + "№ корня  " + "  Метод  " + \
                    "    A    " + "    B    " + \
                    "  Значение X  " + "  Значение F(X)  " + \
                    "  Итераций  " + "  Время работы  " +\
                    "  Код ошибки  \n")
                    isFounded = True

                start = perf_counter()
                sol = brent_dekker_method(test_func, xLeft, xRight, max_iter)
                stop = perf_counter()

                printRes(solN, "  Брент  ", xLeft, xRight, sol[0], \
                sol[1], sol[2], stop - start, sol[3])

                start = perf_counter()
                sol = brentq(test_func, xLeft, xRight, xtol = xtol, \
                full_output = True, disp=False)[1]
                stop = perf_counter()
                printRes(solN, "  brentq ", xLeft, xRight, sol.root, \
                test_func(sol.root), sol.iterations, stop - start, \
                0 if sol.iterations <= max_iter else 1, False)

                solN += 1
            xLeft += dx

        if not isFounded:
            print("\n  На данном отрезке корни не найдены\n")
        else:
            printErrValues()
    except ValueError:
        print("\n  Ошибка ввода! Нужно вводить числа\n")

while True:
    printMenu()

    try:
        command = int(input("\n  Введите команду:  "))
        if command == 1: CompareMethods()
        elif command == 2: resetH()
        elif command == 3: resetMaxIter()
        elif command == 4: resetEps()
        elif command == 0:
            break
        else: raise ValueError

    except (KeyboardInterrupt, ValueError):
        print("\n  Неверная комманда")
