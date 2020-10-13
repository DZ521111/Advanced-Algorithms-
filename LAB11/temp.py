def set_cover(X, f):
    U = X.copy()
    e = []
    while len(U) != 0:
        s = findIntersaction(f, U)
        f.remove(s)
        U = [x for x in U if x not in s]
        e.append(s)
    return e
def findIntersaction(F, u):
    index = 0
    max = 0
    for i in range(len(F)):
        temp = set(F[i]).intersection(set(u))
        if len(temp) > max:
            max = len(temp)
            index = i
        return F[index]
X = [int(i) for i in input().split()]
n = int(input("Enter number of subsets\n"))
f = []
for _ in range(n):
    temp = [int(i) for i in input().split()]
    f.append(temp)
result = set_cover(X, f)
print(result)