main_text = [
"  - Я действительно устал от боли, которую слышу и чувствую босс. Я устал от",
"того, что постоянно куда-то иду, одинокий, всеми покинутый. У меня никогда не",
"было друга, который составил бы мне компанию, сказал, куда мы идём и зачем. Я",
"устал от людей, которые так ненавидят друг друга. Их мысли режут меня, как",
"осколки стекла. Яяяяяяяяяяяяяяяяяяяяяяяяяяя устал от того, что часто хотел помочь и не смог. Я устал от",
"тьмы, которая окружает меня. Но больше всего устал от боли. Её слишком много.",
"Если бы я мог положить ей конец, мне захотелось бы жить дальше. Но я не могу.",
"Слова Джона Коффи из Зеленой мили Стивена Кинга, изданной в 1900 + 100 - 4 году."]

def printMenu():
    print("\n  1. Вывести текст\n  \
2. Выравнивание по ширине\n  3. Выравнивание по левому краю\n  \
4. Выравнивание по правому краю\n  5. Замена слова в тексте\n  \
6. Удаление слова из текста\n  7. Вычислить арифм. выражения\n  \
8. Индивидуальное задание\n  0. Выход")

def printText(text):
    print()
    for string in text:
        print("  " + string)
    print()

def roundWidth():
    global main_text
    text = main_text[:]
    maxLen = 0
    for i in range(len(text)):
        string = text[i]
        start = 0
        end = len(string)
        for j in range(len(string)):
            if string[j] == " ":
                start += 1
            else:
                break
        for j in range(len(string) - 1, 0, -1):
            if string[j] == " ":
                end -= 1
            else:
                break
        string = string[start:end]

        for j in range(len(string) - 1, 0, -1):
            if string[j] == " " and string[j - 1] == " ":
                string = string[:j-1] + string[j+1:]
        maxLen = max(len(string), maxLen)
        text[i] = string

    for string in text:
        lSpFrBeg = lSpFrEnd = -1
        spacesCount = maxLen - len(string)
        first = 0
        last = len(string) - 1

        for i in range(spacesCount):
            if first > last:
                first = 0
                last = len(string) - 1
            if i % 2 == 0:
                for j in range(first, len(string)):
                    if string[j] == " " and not string[j + 1] == " ":
                        string = string[:j] + " " + string[j:]
                        first = j + 2
                        break
            else:
                for j in range(last, 0, -1):
                    if string[j] == " " and not string[j - 1] == " ":
                        string = string[:j] + " " + string[j:]
                        last = j - 1
                        break
        print("  "  + string)

def roundLeft():
    global main_text
    spacesCount = 0;
    for i in main_text[0]:
        if i == " ":
            spacesCount += 1
        else:
            break

    for i in main_text:
        firstNonSpace = 0
        for j in i:
            if j == " ":
                firstNonSpace += 1
            else:
                break
        print("  " + " "*spacesCount + i[firstNonSpace:])

def roundRight():
    global main_text
    neccecaryLength = 0
    for i in main_text:
        if len(i) > neccecaryLength:
            neccecaryLength = len(i)

    for i in main_text:
        print("  " + " "*(neccecaryLength - len(i)) + i)

def exchangeWord():
    global main_text

    exchWord = input("\n  Введите заменяемое слово:  ")
    newWord = input("  Введите новое слово:  ")

    lettersList = [chr(c) for c in range(ord('а'), ord('б')+1)]
    for string in main_text:
        string = " " + string + " "
        for i in range(len(string) - len(exchWord), 1, -1):
            if string[i:i + len(exchWord)] == exchWord and \
            not string[i - 1].lower() in lettersList and \
            not string[i + len(exchWord) + 1].lower() in lettersList and \
            not string[i - 1].lower() in lettersList and \
            not string[i + len(exchWord) + 1].lower() in lettersList:
                string = string[:i] + newWord + string[i + len(exchWord):]
        print("  " + string[1:len(string)-1])

def removeWord():
    global main_text

    removeWord = input("\n  Введите удаляемое слово:  ")

    lettersList = [chr(c) for c in range(ord('а'), ord('б')+1)]
    for string in main_text:
        string = " " + string + " "
        for i in range(len(string) - len(removeWord), 0, -1):
            if string[i:i + len(removeWord)] == removeWord and \
            not string[i - 1].lower() in lettersList and \
            not string[i + len(removeWord) + 1].lower() in lettersList and \
            not string[i - 1].lower() in lettersList and \
            not string[i + len(removeWord) + 1].lower() in lettersList:
                string = string[:i] + string[i + len(removeWord):]

        print("  " + string[1:len(string)-1])

def arifmRes():
    global main_text

    lettersList = [chr(c) for c in range(ord('a'), ord('b')+1)]
    numsList = [chr(c) for c in range(ord('0'), ord('9')+1)]
    for string in main_text:
        string = " " + string + " "
        for i in range(len(string) - 1, 1, -1):
            if string[i] == "+" or string[i] == "-":
                first = second = ""
                fend = fbegin = send = sbegin = -1
                for j in range(i, 1, -1):
                    if string[j] in numsList and \
                    not string[j + 1] in lettersList + numsList: fend = j

                    if string[j] in numsList and \
                    not string[j - 1] in lettersList + numsList: fbegin = j

                    if not fbegin == -1 and not fend == -1:
                        first = string[fbegin : fend + 1]
                        break

                for j in range(i, len(string)):
                    if string[j] in numsList and \
                    not string[j - 1] in lettersList + numsList: sbegin = j

                    if string[j] in numsList \
                    and not string[j + 1] in lettersList + numsList: send = j

                    if not sbegin == -1 and not send == -1:
                        second = string[sbegin : send + 1]
                        break

                if not first == "" and not second == "":
                    if string[i] == "+":
                        string = string[:fbegin] + \
                        str(int(first) + int(second)) + \
                        string[send + 1:]
                    else:
                        string = string[:fbegin] + \
                        str(int(first) - int(second)) + \
                        string[send + 1:]
        print("  " + string[1:len(string)-1])

def replaceSentences():
    global main_text
    text = ' '.join(main_text)
    text = text.split(".")
    maxSogl = maxGl = 0
    maxSoglI = maxGlI = 0
    glList = "ауоыиэяюёе"
    symbList = ",- 1234567890+-"
    for i in range(len(text)):
        string = text[i]
        sogl = gl = 0
        for letter in string:
            if letter in glList and not letter in symbList:
                gl += 1
            if letter not in glList and not letter in symbList:
                sogl += 1
        if gl > maxGl:
            maxGl, maxGlI = gl, i
        if sogl > maxSogl:
            maxSogl, maxSoglI = sogl, i

    text[maxGlI], text[maxSoglI] = text[maxSoglI], text[maxGlI]

    text = '.'.join(text).split()

    strlen = 90
    for word in text:
        if strlen + len(word) < 79:
            print(word + " ", end ="")
            strlen += len(word) + 2
        else:
            print("\n  " + word + " ", end = "")
            strlen = len(word) + 1
    print()

while True:
    printMenu()

    try:
        command = int(input("\n  Введите команду:  "))
        if command == 1: printText(main_text)
        elif command == 2:
            printText(main_text)
            roundWidth()
        elif command == 3:
            printText(main_text)
            roundLeft()
        elif command == 4:
            printText(main_text)
            roundRight()
        elif command == 5:
            printText(main_text)
            exchangeWord()
        elif command == 6:
            printText(main_text)
            removeWord()
        elif command == 7:
            printText(main_text)
            arifmRes()
        elif command == 8:
            printText(main_text)
            replaceSentences()
        elif command == 0:
            break
        else: raise ValueError
    except ValueError:
        print("\n  Неверная команда")
