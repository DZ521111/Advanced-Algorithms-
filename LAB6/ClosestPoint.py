import math as m

class points():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    return m.sqrt(((p1.x - p2.x) ** 2) + ((p1.y - p2.y) ** 2))

def find_distance(p, n):
    min_ = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if (distance(p[i], p[j]) < min_):
                min_ = distance(p[i], p[j])
                point1, point2 = (p[i].x, p[i].y), (p[j].x, p[j].y)
    return min_, point1, point2

def closest_point(p, n):
    p.sort(key = lambda point : point.x)
    return find_distance(p, n)

P = []
point = int(input("Enter the number of points : "))
for _ in range(point):
    a, b = map(int, input().split())
    P.append(points(a, b))

closest_distance, point1, point2 = closest_point(P, len(P))
print(f"Closest Distance is : {closest_distance} between {point1} and {point2}")


