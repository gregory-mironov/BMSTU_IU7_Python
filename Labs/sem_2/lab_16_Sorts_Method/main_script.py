import sys

import time

from tkinter import  Tk, Label, Entry, Frame, Button, END, VERTICAL, NS
from tkinter.ttk import Treeview, Scrollbar

import matplotlib.pyplot as plt
import numpy as np

from sorts import *
from array_generator import *

def get_sorting_time(array, sort):
    start_time = time.time()

    sort(array)

    stop_time = time.time()

    return (stop_time - start_time) * 1000

def main():
    root = Tk()
    results_tbl = Frame(root)

    def sort_button_click(*args):
        try:
            a = list(map(int, AEntry.get().split()))
            shell_sort(a)
            SAEntry.delete(0, END)
            SAEntry.insert(0, a)
        except Exception:
            print("Что-то введено неправильно")

    def table_button_click(*args):
        global results_tbl

        results_tbl = Frame(root)

        tbl = Treeview(results_tbl, columns =\
                ("array", "method", "size_1", "size_2", "size_3"),
                height = 13, show = "headings"
                )

        tbl.heading("array", text = "Array type")
        tbl.column("array", width = 200, stretch = False)
        tbl.heading("method", text = "Method of sorting")
        tbl.column("method", width = 200, stretch = False)
        tbl.heading("size_1", text = "N1 = 10000")
        tbl.column("size_1", width = 150, stretch = False)
        tbl.heading("size_2", text = "N2 = 50000")
        tbl.column("size_2", width = 150, stretch=False)
        tbl.heading("size_3", text = "N3 = 100000")
        tbl.column("size_3", width=150, stretch=False)
        
        methods = [
            ("Shell sort", shell_sort),\
            ("Shell sort (Hibbard 1963)", shell_sort_hibbart_1963),\
            ("Shell sort (Stasevich 1965)", shell_sort_stasevich_1965),\
            ("Shell sort (Knuth 1973)", shell_sort_knuth_1973),\
            ("Shell sort (Sedgwick 1982)", shell_sort_sedgwick_1982),\
            ("Shell sort (Sedgwick 1986)", shell_sort_sedgwick_1986),\
            ("Shell sort (Fibonacci)", shell_sort_fib),\
            ("Shell sort (Tokuda 1992)", shell_sort_tokuda_1992),\
            ("Shell sort (5/11)", shell_sort_5_11),\
            ("Shell sort (3 pow)", shell_sort_3_pow),\
            ("Shell sort (5 pow)", shell_sort_5_pow),\
            ]
        
        arrays = [\
            get_sorted_arr(10000), \
            get_sorted_arr(50000), \
            get_sorted_arr(100000)]
        for method in methods:
            tbl.insert("", END, values = ["{:^}".format("Sorted (ASC)"), \
                format(method[0]), \
                "{:^24.6g}".format(\
                    get_sorting_time(arrays[0], method[1])), \
                "{:^24.6g}".format(\
                    get_sorting_time(arrays[1], method[1])), \
                "{:^24.6g}".format(\
                    get_sorting_time(arrays[2], method[1]))])

        arrays = [\
            get_random_arr(10000), \
            get_random_arr(50000), \
            get_random_arr(100000)]
        for method in methods:
            tbl.insert("", END, values = ["{:^}".format("Random"), \
                format(method[0]), \
                "{:^24.6g}".format(\
                    get_sorting_time(arrays[0], method[1])), \
                "{:^24.6g}".format(\
                    get_sorting_time(arrays[1], method[1])), \
                "{:^24.6g}".format(\
                    get_sorting_time(arrays[2], method[1]))])

        arrays = [\
            get_reversed_sorted_arr(10000), \
            get_reversed_sorted_arr(50000), \
            get_reversed_sorted_arr(100000)
            ]
        for method in methods:
            tbl.insert("", END, values = ["{:^}".format("Sorted (DESC)"), \
                format(method[0]), \
                "{:^24.6g}".format(\
                    get_sorting_time(arrays[0], method[1])), \
                "{:^24.6g}".format(\
                    get_sorting_time(arrays[1], method[1])), \
                "{:^24.6g}".format(\
                    get_sorting_time(arrays[2], method[1]))])

        tbl.grid(row = 0, column = 0)

        sb = Scrollbar(results_tbl, orient = VERTICAL)
        sb.grid(row = 0,column = 1, sticky = NS, padx = 8)
        tbl.configure(xscrollcommand = sb.set)
        sb.configure(command = tbl.xview)

        results_tbl.grid(row = 0, column = 1)

    def graph_button_click(*args):
        plt.clf()
        
        plt.title("Зависимость времени сортировки от размера массива")
        plt.xlabel("Size")
        plt.ylabel("Time, ms")
        plt.grid()
        
        methods = [
            ("Shell sort", shell_sort),\
            ("Shell sort (Hibbard 1963)", shell_sort_hibbart_1963),\
            ("Shell sort (Stasevich 1965)", shell_sort_stasevich_1965),\
            ("Shell sort (Knuth 1973)", shell_sort_knuth_1973),\
            ("Shell sort (Sedgwick 1982)", shell_sort_sedgwick_1982),\
            ("Shell sort (Sedgwick 1986)", shell_sort_sedgwick_1986),\
            ("Shell sort (Fibonacci)", shell_sort_fib),\
            ("Shell sort (Tokuda 1992)", shell_sort_tokuda_1992),\
            ("Shell sort (5/11)", shell_sort_5_11),\
            ("Shell sort (3 pow)", shell_sort_3_pow),\
            ("Shell sort (5 pow)", shell_sort_5_pow),\
            ]
        
        x_gr = np.arange(0, 20001, 200)
        y_gr = [[] for i in range(len(methods))]
        for i in x_gr:
            array = get_reversed_sorted_arr(i)
            for method in range(len(methods)):
                y_gr[method]\
                    .append(\
                        get_sorting_time(\
                            array, \
                            methods[method][1]))

        for i in range(len(y_gr)):
            plt.plot(x_gr, y_gr[i], label = methods[i][0])
        
        plt.legend()
        
        plt.show()

    def quit_button_click(*args):
        sys.exit()

    control = Frame(root)

    Label(control, text="Управление:").grid(row = 0, column = 0, \
    columnspan = 4, padx = 5, pady = 10)

    Label(control, text="Массив для сортировки:").grid(row = 1, column = 0)
    AEntry = Entry(control, width = 15)
    AEntry.grid(row = 1, column = 1, padx = 5, pady = 5)

    Label(control, text="Результат:").grid(row = 2, column = 0)
    SAEntry = Entry(control, width = 15)
    SAEntry.grid(row = 2, column = 1, padx = 5, pady = 5)

    Button(control, text='Сортировать', command=sort_button_click).\
    grid(row = 3, column = 0, pady = 10)

    Button(control, text='График', command=graph_button_click).\
    grid(row = 4, column = 0, pady = 10)

    Button(control, text='Таблица', command=table_button_click).\
    grid(row = 5, column = 0, pady = 10)

    Button(control, text='Выход', command=quit_button_click).\
    grid(row = 6, column = 0, pady = 10)

    control.grid(row = 0, column = 0)
    root.mainloop()

if __name__ == "__main__":
    main()