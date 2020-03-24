fin = open("fill.txt", "r")
fout = open("qt.txt", "w")

for i in reversed(tuple(fin)):
    if i[-1] != '\n':
        i += '\n'
    fout.write(i)

fin.close()
fout.close()
