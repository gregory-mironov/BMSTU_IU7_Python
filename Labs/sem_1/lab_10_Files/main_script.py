class Stud(object):
    def __init__(self, family_in, height_in, weight_in):
        self.family = str(family_in)
        self.height = int(height_in)
        self.weight = float(weight_in)
    def __str__(self):
        return str(self.__class__) + '\n'+\
        '\n'.join(('{}:{}'.format(item, self.__dict__[item])\
         for item in sorted(self.__dict__)))
    def __eq__(self, other):
        if isinstance(other, Stud):
            return self.family == other.family and \
            self.height == other.height and \
            self.weight == other.weight
        else:
            return NotImplemented

def sortByFamily(inputStud):
    return  inputStud.family

def sortByHeight(inputStud):
    return inputStud.height

def sortByWeight(inputStud):
    return inputStud.weight

sortType = int(input('Введите тип сортировки файлов:\n\
    1. По фамилии\n\
    2. По росту\n\
    3. По весу\n    '))

with open("StudInput1.txt", "r") as fin1,\
open("StudInput2.txt", "r") as fin2,\
open("StudOutput.txt", "w") as fout:
    res = []
    f1 = [i.replace("\n", "") if i.find("\n") > 0 else i for i in list(fin1)]

    i = 0
    while i < len(f1):
        if f1[i] == str(Stud):

            fam = ""
            height = 0
            weight = 0

            if f1[i+1].startswith("family:"):
                fam = list(f1[i+1].split(":"))[1]
            if f1[i+2].startswith("height:"):
                height = list(f1[i+2].split(":"))[1]
            if f1[i+3].startswith("weight:"):
                weight = list(f1[i+3].split(":"))[1]
            if fam != "" and height != 0 and weight != 0 and \
            not Stud(fam, height, weight) in res:
                res.append(Stud(fam, height, weight))
                i += 4
            else:
                i += 1
        else:
            i += 1

    f2 = [i.replace("\n", "") if i.find("\n") > 0 else i for i in list(fin2)]
    i = 0
    while i < len(f2):
        if f2[i] == str(Stud):
            fam = ""
            height = 0
            weight = 0

            if f2[i+1].startswith("family:"):
                fam = list(f2[i+1].split(":"))[1]
            if f2[i+2].startswith("height:"):
                height = int(list(f2[i+2].split(":"))[1])
            if f2[i+3].startswith("weight:"):
                weight = int(list(f2[i+3].split(":"))[1])
            if fam != "" and height != 0 and weight != 0 and \
            not Stud(fam, height, weight) in res:
                res.append(Stud(fam, height, weight))
                i += 4
            else:
                i += 1
        else:
            i += 1

    if sortType == 3:
        res = sorted(res, key = sortByWeight)
    elif sortType == 2:
        res = sorted(res, key = sortByHeight)
    else:
        res = sorted(res, key = sortByFamily)
    for i in res:
        fout.write(str(i)+'\n')
