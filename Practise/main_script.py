from collections import namedtuple
from math import atan2, fabs
Point = namedtuple('Point', ['x', 'y'])

def isPointInPolygon(M, vertices):
    isNotBelow, isNotOver, isOnTheSide = True, True, False
    vertNum = len(vertices)
    for i in range(vertNum):
        A = vertices[i]
        B = vertices[(i+1)%vertNum]
        p = M.x*A.y - M.x*B.y - A.x*M.y + A.x*B.y + B.x*M.y - B.x*A.y

        if p > 0:
            isNotOver = False
        elif p < 0:
            isNotBelow = False
        elif min(A.x, B.x) <= M.x <= max(A.x, B.x) and\
        min(A.y, B.y) <= M.y <= max(A.y, B.y):
            isOnTheSide = True

    return isNotOver or isNotBelow or isOnTheSide

def getSegmentsIntersecting(A, B, C, D):
    A, B = (B, A) if A.x > B.x else (A, B)
    C, D = (D, C) if C.x > D.x else (C, D)

    A1, B1 = B.y - A.y, A.x - B.x
    A2, B2 = D.y - C.y, C.x - D.x
    C1, C2 = -(A1*A.x + B1*A.y), -(A2*C.x + B2*C.y)
    DET = A1 * B2 - A2 * B1
    if fabs(DET) > 1e-9:
        a = Point(-(C1 * B2 - C2 * B1) / DET, -(A1 * C2 - A2 * C1) / DET)

        minX = max(A.x, C.x)
        maxX = min(B.x, D.x)
        minY = max(min(A.y, B.y), min(C.y, D.y))
        maxY = min(max(A.y, B.y), max(C.y, D.y))

        if minX <= a.x <= min(B.x, D.x) and minY <= a.y <= maxY:
            return a
    return 0

def sortVerticesByClockwise(vertices):
    basePoint = min(vertices, key = lambda point: (point.y, point.x))

    def comparePointWithBase(a):
        a = Point(a.x - basePoint.x, a.y - basePoint.y)
        return (atan2(a.y, a.x), (a.x**2 + a.y**2))

    return sorted(vertices, key = comparePointWithBase, reverse=True)

def getPolygonSquare(Vertices):
    square = 0; VerticesNum = len(Vertices)
    for i in range(VerticesNum):
        square += 0.5 * (
        (Vertices[i].x + Vertices[(i + 1) % VerticesNum].x)*
        (Vertices[i].y - Vertices[(i + 1) % VerticesNum].y)
        )
    return square

with open("input.txt", "r") as fin:
    fin = list(fin); i = 0
    while True:
        t = list(map(int, fin[i].split()))
        if t[0] == 0:
            break
        polygon1 = [Point(t[j], t[j+1]) for j in range(1, 2*t[0] + 1, 2)]
        t = list(map(int, fin[i + 1].split()))
        polygon2 = [Point(t[j], t[j+1]) for j in range(1, 2*t[0] + 1, 2)]

        totalSquare = getPolygonSquare(polygon1) + \
        getPolygonSquare(polygon2)
        i += 2

        interseption = set(j for j in polygon1 \
        if isPointInPolygon(j, polygon2)) | \
        set(j for j in polygon2 \
        if isPointInPolygon(j, polygon1))

        for j in range(len(polygon1)):
            for k in range(len(polygon2)):
                d = getSegmentsIntersecting(\
                polygon1[j], polygon1[(j+1)%len(polygon1)], \
                polygon2[k], polygon2[(k+1)%len(polygon2)])
                if type(d) == Point:
                    interseption.add(d)

        intersectionSquare = getPolygonSquare(\
        sortVerticesByClockwise(interseption))

        print("{:>8.2f}".format(totalSquare - 2 * intersectionSquare), end = "")
