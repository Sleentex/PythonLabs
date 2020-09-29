import collections
num = int(input("Input count of candidates: "))

dataDict = dict()

for i in range(num):
    name, point = [x for x in input().split()]
    if name in dataDict:
        dataDict[name] += int(point)
    else:
        dataDict[name] = int(point)

print("\nResult: ")
dataRes = collections.OrderedDict(sorted(dataDict.items()))

for key, value in dataRes.items():
    print(key, value)



