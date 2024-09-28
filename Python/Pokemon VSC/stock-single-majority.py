def maxProfit(prices):
    buy = 10
    sell = 0
    for i in range(len(prices)):
        if buy > prices[i]:
            buy = prices[i]
        elif prices[i] > buy:
            sell = prices[i]
    if sell - buy < 1:
        buy = 0
    return sell - buy
a = 0
stock = list(input('add your stocks: '))
print(stock)
for i in range(len(stock)):
    i -= a
    try:
        stock[i] = int(stock[i])
        print(i)
    except:
        print(stock[i])
        stock.remove(stock[i])
        a+=1
    print(i)
print(stock)
profit = maxProfit(stock)
print(profit)

# OH, THEY USE NUMBERS, NOW ITS EASY IS IT?
def majority(listing):
    highest_count = 0
    for n in range(9):
        count = 0
        for i in range(len(listing)):
            if str(n) == listing[i]:
                count += 1
        if highest_count < count:
            majority = listing[n]
            highest_count = count
    return majority
def dict_majority(listing):
    print({listing[i]: listing.count(listing[i]) for i in range(len(listing) )if listing[i] != ' '})



number = list(input('add your numbers: '))
most = majority(number)
print('The majority number is', most)
most = dict_majority(number)