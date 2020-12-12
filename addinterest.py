def addInterest(balance, rate):
    newBalance = balance * (1+rate)
    return newBalance
def test():
    amount = 1000
    rate = .05
    print(amount)
    amount = addInterest(amount, rate)
    print(amount)

test()
