def pri():
    temp = 0
    z = []
    for i in range(2, 7):
        temp=(l[1][0] * l[1][i]) + (l[2][0] * l[2][i])
        z.append(temp)
    print(z)
    print(l)
    sub=[]
    temp = 0
    k = 0
    for i in range(2, 6):
        temp = l[0][i] - z[k]
        k = k + 1
        sub.append(temp)
    print(sub)
    c = 0
    for i in range(0, len(sub)):
        if(sub[i] <= 0):
            c = c + 1
    if(len(sub) == c):
        print("x", l[1][1],l[1][6])
        print("x", l[2][1],l[2][6])
        print("z", z[4])
        return
    enter = 2 + sub.index(max(sub))
    theta1 = l[1][6]/l[1][enter]
    theta2 = l[2][6]/l[2][enter]
    if(theta1 < theta2):
        leave = 1
        asit = 2
    else:
        leave = 2
        asit = 1
    keyele = l[leave][enter]
    keycol = l[asit][enter]
    l[leave][0] = l[0][enter]
    l[leave][1] = enter - 1
    for i in range(2, 7):
        l[asit][i] = l[asit][i] - ((keycol * l[leave][i]) / keyele)
    for i in range(2, 7):
        l[leave][i] = l[leave][i] / keyele
    print("cj - zj", sub)
    print(l)
    pri()
l=[]
for i in range(0, 3):
    x=[int(x) for x in input().split(' ')]
    l.append(x)
pri()
