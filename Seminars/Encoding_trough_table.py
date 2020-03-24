from collections import namedtuple
from random import randint
from math import sqrt

Point = namedtuple('Point', ['x', 'y'])

def printMenu():
    print("\n  1. Создать случайную таблицу\n  2. Закодировать сообщение\n\
  3. Закодировать сообщение в случайную таблицу\n\
  4. Декодировать сообщение\n  5. Выход", end='\n\n')

def createTable(n):
    a = []
    for i in range((n//2)**2):
        a.append(Point(i % (n//2), i // (n//2)))
        for j in range(randint(0, 3)):
            a[i] = Point(n - a[i].y - 1, a[i].x)
    return sorted(a, key = lambda s : Point(s.y, s.x))

def printTable(table):
    tsize = 2*int(sqrt(len(table)))
    sum = []
    for y in range(tsize):
        sum.append(0)
        print("  ",end='')
        for x in range(tsize):
            if Point(x, y) in table:
                print("[ ]", end="")
                sum[y] += int(2**(tsize - x - 1))
            else:
                print(" # ", end="")
        print(" "*4, "{:^11,d}".format(sum[y]).replace(",", " "))

def encodeMsg(msg, t):
    size = 2*int(sqrt(len(t)))
    def rotate90(tab):
        for i in range(len(tab)):
            tab[i] = Point(size - tab[i].y - 1, tab[i].x)
        return sorted(tab, key = lambda s : Point(s.y, s.x))

    partSize = len(t)
    res = ["*" for i in range(len(t)*4)]

    j = 0
    for i in msg:
        res[t[j].x + t[j].y*size] = i
        j += 1
        if j == len(t):
            j = 0
            t = rotate90(t)

    for i in range(4*len(t) - len(msg)):
        res[t[j].x + t[j].y*size] = msg[randint(0, len(msg)-1)]
        j += 1
        if j == len(t):
            j = 0
            t = rotate90(t)
    return res

def printMsg(t, size):
    for i in range(size):
        print("  ", end = "")
        for j in range(size):
            print(t[i*size + j], end="")
        print()

def tableCreation():
    global table
    n = int(input("  Введите размер таблицы:  "))
    print()
    table = createTable(n)
    printTable(table)

def justEncode():
    global table
    if type(table) == list:
        msg = ''.join(list(input("\n  Введите ваше сообщение:\n  ").split()))
        size = round(sqrt(len(msg)))

        if size**2 < len(msg): size += 1
        if size%2 == 1: size += 1

        if size > len(table) * 4:
            print("  Сообщение слишком большое для данной таблицы")
            print("  Нужно создать таблицу размера {:^4d}".format(size))
        else:
            print("\n  Таблица:")
            printTable(table)
            print("\n  Сообщение:\n")
            tab = encodeMsg(msg, table)
            printMsg(tab, 2*round(sqrt(len(table))))
    else:
        print("  Не задана таблица для записи")

def createAndEncode():
    global table
    msg = ''.join(list(input("\n  Введите ваше сообщение:\n  ").split()))
    size = round(sqrt(len(msg)))

    if size**2 < len(msg): size += 1
    if size%2 == 1: size += 1

    print("\n  Новая таблица:")
    table = createTable(size)
    printTable(table)
    print("\n  Сообщение:")
    tab = encodeMsg(msg, table)
    printMsg(tab, 2*round(sqrt(len(table))))

def inputAndDecode():
    def rotate90(tab):
        for i in range(len(tab)):
            tab[i] = Point(len(tab) - tab[i].y - 1, tab[i].x)
        return sorted(tab, key = lambda s : Point(s.y, s.x))

    n = int(input("  Введите размер таблицы сообщения:  "))
    tab = [Point(-1, -1) * n]
    print("  Введите число, характеризующее каждую строку таблицы ")
    for i in range(n):
        q = str(bin(int(input())))
        print(q[2:])
    print("  Введите сообщение:\n  ")
    msg = []
    for i in range(n):
        r = input()
        msg += r[:n]
    res = []
    for i in range(4):
        for j in range(len(table)):
            res += [msg[tab[j][1]][tab[j][0]]]


if __name__ == "__main__":
    table = None
    while True:
        printMenu()
        try:
            command = int(input("  Введите команду:  "))
            if command == 1: tableCreation()
            elif command == 2: justEncode()
            elif command == 3: createAndEncode()
            elif command == 4: inputAndDecode()
            elif command == 5: break
            else: raise ValueError
        except ValueError:
            print("  Ошибка ввода")
        except KeyboardInterrupt:
            print("  Ошибка ввода")
