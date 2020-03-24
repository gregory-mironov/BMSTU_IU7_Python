from time import perf_counter
import sys

from math import *

from tkinter import *
from tkinter.ttk import Scrollbar, Treeview
import matplotlib.pyplot as plt

import numpy as np
from scipy.optimize import brentq
from scipy.misc import derivative

roots_tbl = None
fn = "sin(x) + 0.5"

def test_func(x):
    return eval(fn)

def test_func_ddx(x):
    return derivative(test_func, x, 1e-6, 2)

def brent_dekker_method(func, init_x1, init_x2, xtol, max_iter, meps):
    a = init_x1
    b = init_x2
    fa = func(a)
    fb = func(b)

    if fa == 0.:
        return [init_x1, 1]
    if fb == 0.:
        return [init_x2, 1]

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

    return [b, n_iter]

def getSolutions(function, A, B, dx, xtol, max_iter, meps):
    solutions1 = []
    solutions2 = []

    xLeft = A
    i = 1
    while xLeft < B + meps:
        xRight = xLeft + min(dx, B - xLeft)
        if function(xLeft)*function(xLeft + dx) <= 0:

            start = perf_counter()
            sol = brent_dekker_method(function, xLeft, xRight, xtol, max_iter, meps)
            stop = perf_counter()

            solutions1.append([i, "Брент", xLeft, xRight, sol[0], function(sol[0]),\
            sol[1], stop - start, 0 if sol[1] <= max_iter else 1])

            start = perf_counter()
            sol = brentq(function, xLeft, xRight, xtol = xtol, \
            full_output = True, disp=False)[1]
            stop = perf_counter()

            solutions2.append([i, "brentq", xLeft, xRight, sol.root, \
            function(sol.root), sol.iterations, stop - start, \
            0 if sol.iterations <= max_iter else 1])
            i += 1 
        xLeft += dx
    return [solutions1, solutions2]

def getInflectionPoints(function, A, B, dx, xtol, max_iter, meps):
    if all(function(i) == 0 for i in np.arange(A,B, dx)):
        return []

    points = []
    xLeft = A
    while xLeft < B + meps:
        xRight = xLeft + min(dx, B - xLeft)
        if function(xLeft)*function(xLeft + dx) < 0:
            sol = brentq(function, xLeft, xRight, xtol = xtol, \
            full_output = True, disp=False)[1]
            points.append(sol.root)
        xLeft += dx
    return points

def mainMenu():
    def graphRender():
        global fn

        plt.clf()

        plt.title("График f(x) = " + fn)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()

        a = float(ASpinbox.get())
        b = float(BSpinbox.get())
        h = float(HSpinbox.get())
        fn = FEntry.get()

        x_gr = np.arange(a, b, h)
        y_gr = [test_func(i) for i in x_gr]

        plt.plot(x_gr, y_gr)
        plt.plot([a,b],[0,0])

        sols = getSolutions(test_func, a, b, h, \
        float(ESpinbox.get()), int(MaxIterSpinbox.get()), sys.float_info.epsilon)

        x = []
        y = []
        for i in range(len(sols[0])):
            if sols[0][i][8] == 0:
                x.append(sols[0][i][4])
                y.append(sols[0][i][5])
            elif sols[1][i][8] == 0:
                x.append(sols[1][i][4])
                y.append(sols[1][i][5])

        infPoints = getInflectionPoints(test_func_ddx, a, b, h,\
        float(ESpinbox.get()), int(MaxIterSpinbox.get()), sys.float_info.epsilon)

        plt.plot(infPoints, [test_func(i) for i in infPoints], "hk", x, y, 'xk')

        plt.show()

    def graph_butt(*args):
        graphRender()

    def tbl_butt(*args):
        global roots_tbl
        global fn

        fn = FEntry.get()

        roots_tbl = None
        roots_tbl = Frame(root)

        tbl = Treeview(roots_tbl, columns =\
            ("number", "method", "a", "b", "root",\
            "func", "iter", "time", "err"),
            show = "headings"
            )

        tbl.heading("number", text="№")
        tbl.column("number", width=50, stretch=False)
        tbl.heading("method", text="Метод")
        tbl.column("method", width=60, stretch=False)
        tbl.heading("a", text="A")
        tbl.column("a", width=70, stretch=False)
        tbl.heading("b", text="B")
        tbl.column("b", width=70, stretch=False)
        tbl.heading("root", text="x")
        tbl.column("root", width=80, stretch=False)
        tbl.heading("func", text="f(x)")
        tbl.column("func", width=80, stretch=False)
        tbl.heading("iter", text="Итерации")
        tbl.column("iter", width=100, stretch=False)
        tbl.heading("time", text="Время")
        tbl.column("time", width=80, stretch=False)
        tbl.heading("err", text="Ошибка")
        tbl.column("err", width=70, stretch=False)

        tbl.grid(row=0, column = 0)
    
        sb = Scrollbar(roots_tbl, orient=VERTICAL)
        sb.grid(row=0,column=1, sticky=NS, padx=8)
        tbl.configure(xscrollcommand=sb.set)
        sb.configure(command=tbl.xview)

        roots = getSolutions(test_func, \
        float(ASpinbox.get()), float(BSpinbox.get()), \
        float(HSpinbox.get()), float(ESpinbox.get()), \
        int(MaxIterSpinbox.get()), sys.float_info.epsilon)
        
        for i in range(2, 2*len(roots[0])+1, 2):
            tbl.insert("", END, values=\
                tuple("{:^7.4g}".format(roots[0][i//2-1][j]) \
                if j not in [0, 1, 6, 8] else \
                "{:^15}".format(roots[0][i//2-1][j]) if j > 1 else
                roots[0][i//2-1][j] for j in range(len(roots[0][i//2-1]))))

            tbl.insert("", END, values=\
                tuple("{:^7.4g}".format(roots[1][i//2-1][j]) \
                if j not in [0, 1, 6, 8] else \
                "{:^15}".format(roots[1][i//2-1][j]) if j > 1 else
                roots[1][i//2-1][j] for j in range(len(roots[1][i//2-1]))))
        
        roots_tbl.grid(row=0, column=1) 
    
    def quit_butt(*args):
        sys.exit()

    root = Tk()

    control = Frame(root)

    Label(control, text="Параметры графика:").grid(row=0, column=0, \
    columnspan=5, padx=5, pady=10)

    Label(control, text="Начало отрезка:").grid(row=1, column=0)
    ASpinbox = Spinbox(control, width=10, from_=0, to=25)
    ASpinbox.grid(row=1, column=1, padx=5, pady=5)

    Label(control, text="Конец отрезка:").grid(row=1, column=3)
    BSpinbox = Spinbox(control, width=10, from_=1, to=25)
    BSpinbox.grid(row=1, column=4, padx=5, pady=5)

    Label(control, text="Шаг разбиения:").grid(row=2, column=0)
    HSpinbox = Spinbox(control, width=10, from_=1, to=25)
    HSpinbox.grid(row=2, column=1, padx=5, pady=5)

    Label(control, text="Функция f(x):").grid(row=2, column=3)
    FEntry = Entry(control, width=15)
    FEntry.insert(0, fn)
    FEntry.grid(row=2, column=4, padx=5, pady=5)

    Label(control, text="Параметры корней:").grid(row=3, column=0, \
    columnspan=5, padx=5, pady=10)

    Label(control, text="Точность:").grid(row=4, column=0)
    ESpinbox = Spinbox(control, width=10, from_=1, to=25)
    ESpinbox.grid(row=4, column=1, padx=5, pady=5)

    Label(control, text="Итерации:").grid(row=4, column=3)
    MaxIterSpinbox = Spinbox(control, width=10, from_=100, to=200)
    MaxIterSpinbox.grid(row=4, column=4, padx=5, pady=5)

    Button(control, text='График', command=graph_butt).\
    grid(row=5, column=2, pady=10)

    Button(control, text='Таблица', command=tbl_butt).\
    grid(row=5, column=3, pady=10)

    Button(control, text='Выход', command=quit_butt).\
    grid(row=5, column=4, pady=10)

    control.grid(row=0,column=0)
    root.mainloop()

if __name__ == "__main__":
    mainMenu()
