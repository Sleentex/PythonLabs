from person import Person

class BankCustomer(Person):
    def __init__(self, lastName, firstName, surname, birthday, passportSeries, sex, sumCredit, phoneNumber):
        Person.__init__(self, lastName, firstName, surname, birthday)

        self.passportSeries = passportSeries
        self.sex = sex
        self.sumCredit = sumCredit
        self.phoneNumber = phoneNumber