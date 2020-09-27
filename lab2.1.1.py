import numpy as np

A = np.array([[int(v) for v in input().split()] for _ in range(int(input("Enter size of matrix: ")))])
vec = []

for i in range(len(A)):
    if np.all(A[:-1,i]>= A[1:,i]):
        vec.append(i)

for v in [vec[i:i + 10] for i in range(0, len(vec), 10)]:
    print(*v, sep=' ')
