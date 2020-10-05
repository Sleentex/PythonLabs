from datetime import datetime
from bankCustomer import BankCustomer

myFile = open('D:\\university\Python\lab4\data.txt', encoding='utf-8')
customers = []

for row in myFile:
    data = row.split(';')
    customer = BankCustomer(data[0], data[1], data[2], datetime(year=int(data[3]), month=int(data[4]), day=int(data[5])), data[6], data[7], int(data[8]), data[9])
    customers.append(customer)

totalSumCredit, sumAge, countMale = 0, 0, 0

for customer in customers:
    totalSumCredit += customer.sumCredit

    if customer.sex == 'male':
        sumAge += customer.getAge()
        countMale += 1

middleAge = 0

if countMale != 0:
    middleAge = sumAge / countMale

print('\nCередній вік усіх чоловіків-клієнтів банку: ', middleAge)
print('Загальна сума кредиту: ', totalSumCredit)