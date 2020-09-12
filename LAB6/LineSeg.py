# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 16:05:58 2020

@author: DHRUV
"""


class store_points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def onsegment(p, q, r):
    if ( (min(p.x, q.x) <= r.x <= max(p.x, q.x)) and (min(p.y, q.y) <= r.y <= max(p.y, q.y)) ):
        return True
    return False

def find_direction(p, q, r):
    Rx, Ry = (r.x - p.x), (r.y - p.y)
    Qx, Qy = (q.x - p.x), (q.y - p.y)
    dist = (Rx * Qy) - (Qx * Ry)
    if (dist == 0):
        return 0
    elif (dist > 0):
        return 1
    else:
        return -1
    
def intersection(p1, p2, p3, p4):
    d1 = find_direction(p3, p4, p1)
    d2 = find_direction(p3, p4, p2)
    d3 = find_direction(p1, p2, p3)
    d4 = find_direction(p1, p2, p4)
    
    if (d1 * d2 < 0 and d3 * d4 < 0):
        return True
    elif (d1 == 0 and onsegment(p3, p4, p1)):
        return True
    elif (d2 == 0 and onsegment(p3, p4, p2)):
        return True
    elif (d3 == 0 and onsegment(p1, p2, p3)):
        return True
    elif (d4 == 0 and onsegment(p1, p2, p4)):
        return True
    else:
        return False

if __name__ == "__main__":
    a, b = map(int, input().split())
    p1 = store_points(a, b)
    a, b = map(int, input().split())
    p2 = store_points(a, b)
    a, b = map(int, input().split())
    p3 = store_points(a, b)
    a, b = map(int, input().split())
    p4 = store_points(a, b)

    if (intersection(p1, p2, p3, p4)):
        print("YES")
    else:
        print("NO")

