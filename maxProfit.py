def maxProfit(prices):
    minPrice = prices[0]
    n = len(prices)
    maxP = 0
    for i in range(1, n):
        if prices[i] < minPrice:
            minPrice = prices[i]
        else:
            newPrice = prices[i] - minPrice
            maxP = max(maxP, newPrice)
    return maxP


print(maxProfit([7,6,4,3,1]))