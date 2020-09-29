import re
a = re.split('[.,!?/<>1234567890 ]+', input())
print(a)

for i in range(0, len(a)):
    if len(a[i]) % 2 != 0:
        midlen = len(a[i])//2  
        print(a[i][:midlen] + a[i][midlen+1:] , end=" ")


 