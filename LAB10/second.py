#Author : Dhruv B Kakadiya

def find_max(matrix):
    maximum_degree = 0
    maximum_Node = 0

    for i in range(len(matrix)):
        countD = matrix[i].count(1)
        if countD > maximum_degree:
            maximum_degree = countD
            maximum_Node = i
    return maximum_degree, maximum_Node

def removeEdge(matrix, n):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == n or j == n:
                matrix[i][j] = 0

def anyEdgeLeft(matrix):
    left = False
    for i in range(len(matrix)):
        if matrix[i].count(1) > 0:
            left = True
    return left

if __name__ == "__main__":
    n = int(input("Enter number of vertex :- \n"))
    print("Enter matrix :- \n")
    matrix = []
    maximum_degree = 0
    maximum_Node = -1
    Ran_approx = []

    for i in range(n):
        temp = list(map(int, input().split()))
        matrix.append(temp)

    while anyEdgeLeft(matrix):
        maximum_degree, maximum_Node = find_max(matrix)
        Ran_approx.append(maximum_Node)
        removeEdge(matrix, maximum_Node)

    print("Min vertex cover:", Ran_approx)