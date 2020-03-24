from math import atan2, fabs

def vectorProduct(a, b, c):
    # bc x ac
    return a.x*b.y - a.x*c.y - b.x*a.y + b.x*c.y + c.x*a.y - c.x*b.y

def scalProduct(a, b, c):
    return (c.x - b.x)*(a.x - b.x) + (c.y - b.y)*(a.y - b.y)

class Point(object):
    def __init__(self, x, y):
        self.x = x; self.y = y
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

class Segment(object):
    def __init__(self, point1, point2):
        if atan2(point1.y, point1.x) > atan2(point2.y, point2.x) or \
        atan2(point1.y, point1.x) == atan2(point2.y, point2.x) and \
        (point1.x**2 + point1.y**2) < (point2.x**2 + point2.y**2):
            self.A = point1
            self.B = point2
        else:
            self.A = point2
            self.B = point1
    #ABC(A=y2-y1, B=x1-x2, C=-A*x1-B*y1)
    #A1x+B1y+C1=0
    #A2x+B2y+C2=0
    def findIntersection(self, other):
        A1, B1 = self.B.y - self.A.y, self.A.x - self.B.x
        A2, B2 = other.B.y - other.A.y, other.A.x - other.B.x
        C1, C2 = -(A1*self.A.x + B1*self.A.y), -(A2*other.A.x + B2*other.A.y)
        DET = A1 * B2 - A2 * B1
        if fabs(DET) > 1e-9:
            a = Point(-(C1 * B2 - C2 * B1) / DET, -(A1 * C2 - A2 * C1) / DET)

            minX = max(self.A.x, other.A.x)
            maxX = min(self.B.x, other.B.x)
            minY = max(min(self.A.y, self.B.y), min(other.A.y, other.B.y))
            maxY = min(max(self.A.y, self.B.y), max(other.A.y, other.B.y))

            if minX <= a.x <= maxX and minY <= a.y <= maxY:
                return a
        return 0

class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getSquare(self):
        return 0.5 * abs((self.a.x - self.c.x)*(self.b.y - self.c.y) -\
         (self.b.x - self.c.x)*(self.a.y - self.c.y))

    def getVerticles(self):
        return [self.a, self.b, self.c]

    def isPointInTriangle(self, point):
        p1 = vectorProduct(point, self.a, self.b)
        p2 = vectorProduct(point, self.b, self.c)
        p3 = vectorProduct(point, self.c, self.a)
        res = False
        if(p1 < 0 and p2 < 0 and p3 < 0) or \
        (p1 > 0 and p2 > 0 and p3 > 0):
            res = True
        else:
            if p1 == 0:
                res = min(self.a.x, self.b.x) <= point.x <= max(self.a.x, self.b.x) and\
                min(self.a.y, self.b.y) <= point.y <= max(self.a.y, self.b.y)
            elif p2 == 0:
                res = min(self.b.x, self.c.x) <= point.x <= max(self.b.x, self.c.x) and\
                min(self.b.y, self.c.y) <= point.y <= max(self.b.y, self.c.y)
            elif p3 == 0:
                res = min(self.c.x, self.a.x) <= point.x <= max(self.c.x, self.a.x) and\
                min(self.c.y, self.a.y) <= point.y <= max(self.c.y, self.a.y)
        return res

    def findIntersectionSquare(self, other):
        intersection = []
        selfCorners = self.getVerticles()
        otherCorners = other.getVerticles()
        for i in range(3):
            if not (otherCorners[i] in intersection) and \
            (self.isPointInTriangle(otherCorners[i])):
                intersection.append(otherCorners[i])

            if not (selfCorners[i] in intersection) and \
            (other.isPointInTriangle(selfCorners[i])):
                intersection.append(selfCorners[i])

        for i in range(3):
            for j in range(3):
                d = Segment(\
                selfCorners[i], \
                selfCorners[(i + 1) % 3]).\
                findIntersection(Segment(\
                otherCorners[j], \
                otherCorners[(j + 1) % 3]))
                if (type(d) is Point) and not (d in intersection):
                    intersection.append(d)

        if len(intersection) > 0:
            intersection = sortVerticesByClockwise(intersection)
        return getSquareByVertices(intersection)

def getSquareByVertices(Vertices):
    square = 0
    VerticesNum = len(Vertices)
    for i in range(VerticesNum):
        square += 0.5 * (
        (Vertices[i].x + Vertices[(i + 1) % VerticesNum].x)*
        (Vertices[i].y - Vertices[(i + 1) % VerticesNum].y)
        )
    return square

def getXorPolygonsSquare(p1, p2):
    square = 0
    for j in p1:
        freeSquare = j.getSquare()
        for k in p2:
            freeSquare -= j.findIntersectionSquare(k)
        if freeSquare > 0:
            square += freeSquare
    return square

def sortVerticesByClockwise(vertices):
    basePoint = min(vertices, key = lambda point: (point.y, point.x))

    def comparePointWithBase(a):
        a = Point(a.x - basePoint.x, a.y - basePoint.y)
        return (atan2(a.y, a.x), (a.x**2 + a.y**2))

    return sorted(vertices, key = comparePointWithBase, reverse=True)

def triangulation(vertices):
    triangles = []
    firstPoint = 0
    secondPoint = 1
    thirdPoint = 2

    while(len(vertices) > 3):
        if(vectorProduct(vertices[firstPoint], \
        vertices[secondPoint], \
        vertices[thirdPoint]) < 0):
            newTriangle = True
            triang = Triangle(vertices[firstPoint], \
            vertices[secondPoint], \
            vertices[thirdPoint])
            for i in range(thirdPoint + 1, len(vertices)):
                if triang.isPointInTriangle(vertices[i]):
                    newTriangle = False
                    firstPoint += 1
                    break;
            if newTriangle:
                triangles.append(triang)
                del vertices[secondPoint]
            else:
                secondPoint = thirdPoint
                thirdPoint += 1
        else:
            firstPoint = secondPoint
            secondPoint = thirdPoint
            thirdPoint += 1

    triang = Triangle(vertices[0], vertices[1], vertices[2])
    triangles.append(triang)

    return triangles

with open("input.txt", "r") as fin:
    fin = list(fin)
    i = 0
    while True:
        t = list(map(int, fin[i].split()))
        if t[0] == 0:
            break
        else:
            polygon1 = triangulation([Point(t[j], t[j+1]) for j in range(1, 2*t[0] + 1, 2)])
            t = list(map(int, fin[i + 1].split()))
            polygon2 = triangulation([Point(t[j], t[j+1]) for j in range(1, 2*t[0] + 1, 2)])

            xorSquare = getXorPolygonsSquare(polygon1, polygon2) + \
            getXorPolygonsSquare(polygon2, polygon1)

            print("{:>8.2f}".format(xorSquare), end = "")
        i += 2
