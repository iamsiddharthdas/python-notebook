class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
    #debit method
    def debit(self,amount):
        self.balance -= amount
        print(f'Rs.{amount} was debited')
        print(f'total balance = {self.get_balance()}')
        
    #credit method
    def credit(self,amount):
        self.balance += amount
        print(f'Rs.{amount} was credited')
        print(f'total balance = {self.get_balance()}')
        
    # print balance method
    def get_balance(self):
        return self.balance

acc1 = Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)

'''
Output:

Rs.1000 was debited
total balance = 9000
Rs.500 was credited
total balance = 9500


'''