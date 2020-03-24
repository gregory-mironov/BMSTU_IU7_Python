def printMenu():
    print("  Меню")
    print(" "*4 + "1. Выбор файла")
    print(" "*4 + "2. Создание нового файла")
    print(" "*4 + "3. Добавление записи в файл")
    print(" "*4 + "4. Вывод всех записей")
    print(" "*4 + "5. Поиск по 1 полю")
    print(" "*4 + "6. Поиск по 2 полям")
    print(" "*4 + "0. Выход")
    print()

def printRecordType():
    print()
    print(" "*4 + "1. Фамилия")
    print(" "*4 + "2. Имя")
    print(" "*4 + "3. Должность")
    print(" "*4 + "4. Зарплата")
    print(" "*4 + "5. Компания\n")

def printRecordTable():
    print("\n  {:^10} {:^10} {:^10} {:^10} {:^10}\n".format(\
    "Фамилия", "Имя", "Должность", "Зарплата", "Компания") )

def chooseFile():
    global fileName
    tempName = input("  Введите название искомого файла или 'exit' для отмены: ")
    if not tempName == "exit":
        try:
            fin = open(tempName, "r")
            fin.close()
            fileName = tempName
        except FileNotFoundError:
            print("  Данного файла не существует")

def createFile():
    global fileName
    tempname = input("  Введите название файла или 'exit' для отмены:  ")
    if tempname != "exit":
        fin = open(tempname, "w")
        fin.close()
        fileName = tempname
        print("  Файл успешно создан")

def appendFile(filename):
    if type(filename) == str:
        with open(filename, 'a') as fin:
            print(" "*4 + "  Создание новой записи\n    ")
            family = input("  Фамилия:  ")
            name = input("  Имя:  ")
            position = input("  Должность:  ")
            salary = input("  Зарплата:  ")
            company = input("  Компания:  ")
            fin.write(family + " " + name + " " +  position + \
            " " + salary + " " + company + "\n")
            print("  Запись успешно добавлена")
    else:
        print("  Сначала необходимо выбрать файл")

def readAllFile(filename):
    if type(filename) == str:
        print("  Записи в файле " + filename + " :", end = "\n\n")
        with open(filename, 'r') as fin:
            f1 = [i.split() for i in list(fin)]
            if len(f1) > 0:
                printRecordTable()
                for i in sorted(f1):
                    print("  ", end = "")
                    for j in i:
                        print("{:^10}".format(j), end=" ")
                    print()
            print()
    else:
        print("\n  Сначала необходимо выбрать файл")

def searchByOneField(filename):
    if type(filename) == str:
        with open(filename, 'r') as fin:
            printRecordType()
            n = int(input("    Поле для поиска:  "))
            target = input("  Введите значение для поиска:  ")
            f1 = [i.split() for i in list(fin)]
            print()
            if len(f1) > 0:
                isFounded = False
                printRecordTable()
                for i in sorted(f1):
                    if target.lower() == i[n-1].lower():
                        print("  ", end = "")
                        for j in i:
                            print("{:^10}".format(j), end=" ")
                        print()
                        isFounded = True
                if not isFounded:
                    print("  Записи не найдены\n")
                else:
                    print()
            else:
                print("  В файле нет записей\n")
    else:
        print("  Сначала необходимо выбрать файл")

def searchByTwoFields(filename):
    if type(filename) == str:
        with open(filename, 'r') as fin:
            printRecordType()
            n, m = map(int, input("    Поля для поиска:  ").split());
            print("  Введите значения для поиска:")

            target1 = input("  Первое:  ")
            target2 = input("  Второе:  ")
            f1 = [i.split() for i in list(fin)]
            print()
            if len(f1) > 0:
                isFounded = False
                for i in sorted(f1):
                    if target1.lower() == i[n-1].lower()\
                     and target2.lower() == i[m-1].lower():
                        print("  ", end = "")
                        for j in i:
                            print("{:^10}".format(j), end=" ")
                        print()
                        isFounded = True
                if not isFounded:
                    print("  Записи не найдены\n")
                else:
                    print()
            else:
                print("  В файле нет записей\n")
    else:
        print("  Сначала необходимо выбрать файл")

if __name__ == "__main__":
    fin = None
    fileName = None
    while True:
        printMenu()
        try:
            command = int(input("  Введите команду:  "))
            if command == 1: chooseFile()
            elif command == 2: createFile()
            elif command == 3: appendFile(fileName)
            elif command == 4: readAllFile(fileName)
            elif command == 5: searchByOneField(fileName)
            elif command == 6: searchByTwoFields(fileName)
            elif command == 0: break
            else: raise ValueError
        except ValueError:
            print("  Неверная команда")
