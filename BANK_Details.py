class Bank:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.bal = balance

    def deposits(self, deposit):
        self.bal += deposit
        return self.bal

    def Withdrawel(self, withdraw):
        if withdraw > self.bal:
            return "Insufficient balance to withdraw"
        elif withdraw>100000:
            return "your limit exceeds"

        else:
            self.bal -= withdraw
            return self.bal

    def checkbalance(self):
        return self.bal, self.name, self.age



bank = Bank("hari", 23, 30000000)

depo=bank.deposits(10000000000000) 
print("balace after deposit",depo)
withdraw_result = bank.Withdrawel(1000000000)  
print("!",withdraw_result)  
print("your banking details with balance: ",bank.checkbalance())  
