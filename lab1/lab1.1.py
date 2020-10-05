import math as mt

def formula(x, a, k):
    return mt.cos(a ** k + x ** k) / mt.factorial(k ** 2)

print("Enter x a eps: ")
x, a, eps = (float(v) for v in input().split())

prev_sum, now_sum, k = formula(x, a, 0), formula(x, a, 0) + formula(x, a, 1), 2

while mt.fabs(now_sum - prev_sum) >= eps:
    prev_sum = now_sum
    now_sum += formula(x, a, k)
    k += 1

print("Sum = " + str(now_sum) + "\nk = " + str(k))