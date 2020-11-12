from datetime import datetime
from BookFund import BookFund
import shelve, os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
FILENAME = DIR_PATH + '/' + 'db/shelve_db'

def insertData():
    firstName = input('firstName: ')
    lastName = input('lastName: ')
    bookName = input('bookName: ')
    pageCount = int(input('pageCount: '))
    publicationYear = int(input('publicationYear: '))
    publisherName = input('publisherName: ')
    receiptDate = input('receiptDate (y.m.d): ').split('.')

    bookFund = BookFund(
        firstName,
        lastName,
        bookName,
        pageCount,
        publicationYear,
        publisherName,
        datetime(year=int(receiptDate[0]), month=int(receiptDate[1]), day=int(receiptDate[2]))
    )

    with shelve.open(FILENAME) as bookFunds:
        bookFunds[str(hash(bookFund))] = bookFund

    print('Record saved')


def showAllData():
    with shelve.open(FILENAME) as states:
        for key in states:
            print(states[key])

    print()


def showData():
    with shelve.open(FILENAME) as db:
        bookFunds = db.values()

        if bookFunds:
            print("Count of unique Author: ", getCountOfUniqueAuthors(bookFunds))
            print("Oldest book: ", getOldestBook(bookFunds))


def getCountOfUniqueAuthors(bookFunds):
    uniqueAuthors = set()

    for bookFund in bookFunds:
        uniqueAuthors.add(bookFund.firstName + ' ' + bookFund.lastName)

    return len(uniqueAuthors)


def getOldestBook(bookFunds):
    oldestYear = 0
    oldestBook = 'Undefined'
    flag = True

    for bookFund in bookFunds:
        if bookFund.publicationYear < oldestYear or flag:
            flag = False
            oldestYear = bookFund.publicationYear
            oldestBook = bookFund.bookName
            
    return oldestBook + ' ' + str(oldestYear)


insertData()
showAllData()
showData()



