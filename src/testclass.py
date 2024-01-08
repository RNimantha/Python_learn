class Bank:
    def __init__(self, owner, blance=0):
        self.owner = owner
        self.balance = blance
    
    def deposit(self, amount):
        return f'{self.owner} has deposit LKR:{amount} and his available balnce is now LKR:{self.balance + amount}'
        
    def withdrawal(self, amount):
        pass
    
        