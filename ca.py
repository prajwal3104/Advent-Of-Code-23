class Stock:
    def __init__(self, cp=0.0, no_of_shares=0):
        self.cp = cp
        self.no_of_shares = no_of_shares

    def set_stock(self, cp, no_of_shares):
        self.cp = cp
        self.no_of_shares = no_of_shares

    def calculate_portfolio_value(self):
        return self.cp * self.no_of_shares


class Profit(Stock):
    def __init__(self, bp=0.0):
        super().__init__()
        self.bp = bp

    def set_bp(self, bp):
        self.bp = bp

    def calculate_profit(self):
        return (self.cp - self.bp) * self.no_of_shares


def calculate_portfolio_and_profit(cp, bp, no_of_shares):
    stock = Stock()
    stock.set_stock(cp, no_of_shares)

    profit = Profit()
    profit.set_stock(cp, no_of_shares)
    profit.set_bp(bp)

    portfolio_value = stock.calculate_portfolio_value()
    profit_value = profit.calculate_profit()

    return portfolio_value, profit_value

if __name__ == "__main__":
    cp = float(input())
    bp = float(input())
    NoOfShare = int(input())

    result = calculate_portfolio_and_profit(cp, bp, NoOfShare)

    print(f"Portfolio Value: {result[0]:.2f}")
    print(f"Profit: {result[1]:.2f}")
