
N = abs(int(input('Введите целое число N:\n    ')))

preres = set()
res = set()

while (N > 0):
    if not N % 10 in preres:
        preres.add(N % 10)
    else:
        res.add(N % 10)
    N //= 10

if len(res) > 0:
    for i in res:
        print(i, end=" ")
else:
    print("В числе нет повторяющихся цифр")
