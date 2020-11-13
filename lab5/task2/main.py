import sqlite3, os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
FILENAME = DIR_PATH + '/' + 'bookFund.db'

def getConnection():
    return sqlite3.connect(FILENAME)

def createTables():
    with getConnection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS book_fund (
                _id                 INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name          TEXT,
                last_name           TEXT,
                book_name           TEXT,
                page_count          INTEGER,
                publication_year    INTEGER,
                publisher_name      TEXT,
                receipt_date        DATE
            )
        """)


def deleteTable():
    try:
        with getConnection() as conn:
            cursor = conn.cursor()
            cursor.execute('DROP TABLE book_fund')
    except Exception:
        print('Table book_fund not found')


def insertData():
    try:
        with getConnection() as conn:
            print('----Insert data----')

            _id = None
            first_name = input('first_name: ')
            last_name = input('last_name: ')
            book_name = input('book_name: ')
            page_count = int(input('page_count: '))
            publication_year = int(input('publication_year: '))
            publisher_name = input('publisher_name: ')
            receipt_date = input('receipt_date (y.m.d): ')


            cursor = conn.cursor()
            cursor.execute('INSERT INTO book_fund VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (
                _id, first_name, last_name, book_name, page_count, publication_year, publisher_name, receipt_date
            ))
    except Exception:
        print('Something went wrong')


def showAllData():
    try:
        with getConnection() as conn:
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM book_fund')
            print(cursor.fetchall())
    except Exception:
        print('Something went wrong')


def showData():
    try:
        with getConnection() as conn:
            cursor = conn.cursor()

            cursor.execute('SELECT COUNT(*) FROM (SELECT DISTINCT first_name, last_name FROM book_fund)')
            res = str(cursor.fetchone())
            print("Count of unique Author: ", res[1:-2])

            cursor.execute('SELECT book_name, MIN(publication_year) FROM book_fund')
            res = str(cursor.fetchone())
            print("Oldest book: ", res)
    except Exception:
        print('Something went wrong')


#deleteTable()
createTables()
insertData()
showAllData()
showData()

