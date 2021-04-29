class atm(object):
    def __init__(self, cardNo, pinNo, balance):
        self.cardNo = cardNo
        self.pinNo = pinNo
        self.balance = balance
    def BalanceEnquiry(self):
        print("balance:", self.balance)

card1 = atm('234378', '2201', '$120')

print(card1.BalanceEnquiry())