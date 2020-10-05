import math as mt

def ak(k):
    if k == 0: return 1
    return (1 + pow(-1, k) / mt.factorial(k + 1)) * ak(k - 1)

n = int(input("Enter n: "))
sum = 0

for k in range(1, n+1):
    sum += ak(k) / mt.factorial(k + 1)
print(sum)



"""
def akk(k):
    sum = 1

    while k != 0:
        sum *= 1 + pow(-1, k) / mt.factorial(k + 1)
        k -= 1
    return sum
"""