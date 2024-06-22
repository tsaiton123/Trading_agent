class agent:
    def __init__(self, name, cash, stocks):
        self.name = name
        self.cash = cash
        self.stocks = stocks

    def buy(self, stock, amount):
        self.cash -= stock.price * amount
        self.stocks[stock] = self.stocks.get(stock, 0) + amount

    def sell(self, stock, amount):
        self.cash += stock.price * amount
        self.stocks[stock] -= amount
        if self.stocks[stock] == 0:
            del self.stocks[stock]

    def __str__(self):
        return f'{self.name} has {self.cash} cash and {self.stocks} stocks'

    def __repr__(self):
        return str(self)
    

if __name__ == '__main__':
    a = agent('Alice', 1000, {})
    print(a)