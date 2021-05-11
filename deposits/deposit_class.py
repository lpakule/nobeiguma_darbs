class DepositClass:
    def __init__(self, deposit, term, rate):
        self.deposit = deposit
        self.term = term
        self.rate = rate
    def interest(self):
        interest = self.deposit
        iii = self.term
        for i in range(1, iii+1):
            interest = interest*(self.rate+1)
        return interest



jauns = DepositClass(deposit=1000, term=3, rate=0.05)
print(jauns.interest())
