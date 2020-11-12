class BookFund:
    def __init__(self, firstName, lastName, bookName, pageCount, publicationYear, publisherName, receiptDate):
        self.firstName = firstName
        self.lastName = lastName
        self.bookName = bookName
        self.pageCount = pageCount
        self.publicationYear = publicationYear
        self.publisherName = publisherName
        self.receiptDate = receiptDate

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}, {}' \
            .format(self.firstName, self.lastName, self.bookName, self.pageCount, \
                self.publicationYear, self.publisherName, self.receiptDate.date())
