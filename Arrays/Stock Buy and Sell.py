#Solution

def buy_sell(prices):
    n = len(prices)
    max_profit = 0
    min_profit = float("inf")
    for i in range(0,n):
        min_profit = min(min_profit, prices[i])
        max_profit = max(max_profit, prices[i] - min_profit)
    return max_profit

prices = [7,1,5,3,6,4]
print(buy_sell(prices))