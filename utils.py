from firstrade import account, order, symbols

def get_best_stock():
    # Get the top 5 stocks
    top_stocks = symbols.get_top_movers()
    return top_stocks[0]

