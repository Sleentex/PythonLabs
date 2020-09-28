import numpy as np

def numberOfColToVec(A):
    vec = []
    for j in range(len(A)):
        flag = True

        for i in range(len(A) - 1):
            if A[i][j] < A[i + 1][j]:
                flag = False
                break
            
        if flag == True:
            vec.append(j)
    return vec

def printVec(vec):
    k = 0
    for i in vec:
        print(i, end=" ")
        k += 1
        if k == 10:
            print()

A = np.array([[int(v) for v in input().split()] for y in range(int(input("Enter size of matrix: ")))])
printVec(numberOfColToVec(A))



