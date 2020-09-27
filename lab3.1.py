n, k = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]

nmin = min(numbers)
nmax = max(numbers)

intervalDown_min = nmin - k
intervalDown_max = nmin + k

intervalUp_min = nmax - k
intervalUp_max = nmax + k

uniq = set()
print(intervalUp_min, intervalUp_max)
for x in range(intervalUp_min, intervalUp_max + 1):  
    for y in range(intervalDown_min, intervalDown_max + 1) :
        if y == 0: continue
        if x // y: uniq.add(y)

print(uniq)


