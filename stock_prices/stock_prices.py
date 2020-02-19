import argparse


# Stock Prices: You want to write a bot that will automate the task of day-trading for you while you're going
# through Lambda. You decide to have your bot just focus on buying and selling Amazon stock.
#
# Write a function find_max_profit that receives as input a list of stock prices. Your function should return the
# maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is
# allowed here.
#
# For example, find_max_profit([1050, 270, 1540, 3800, 2]) should return 3530, which is the maximum profit that can
# be made from a single buy and then sell of these stock prices.
#
# Hints: For this problem, we essentially want to find the maximum difference between the smallest and largest prices
# in the list of prices, but we also have to make sure that the max profit is computed by subtracting some price by
# another price that comes before it; it can't come after it in the list of prices. So... what if we kept track of the
# current_min_price_so_far and the max_profit_so_far?


def find_max_profit(prices):
    # 1. Keep record of the lowest price running
    # 2. Keep track of the highest price running after the lowest price was set
    # 3. Calculate profit

    # Below is my attempt:
    # lowest_stock_price = sys.maxsize
    # highest_stock_price = 0
    # maximum_profit = 0
    # for stock_price in prices:
    #     print('price: ' + str(stock_price), end=' ')
    #     if stock_price < lowest_stock_price:
    #         lowest_stock_price = stock_price
    #     if stock_price > highest_stock_price:
    #         highest_stock_price = stock_price
    #     maximum_profit = highest_stock_price - lowest_stock_price
    #     print('Profit so far: ' + str(maximum_profit))
    # return highest_stock_price - lowest_stock_price

    # Below: help received
    minimum_price = prices[0]
    maximum_profit = prices[1] - minimum_price
    for i in range(1, len(prices)):
        price = prices[i]
        maximum_profit = max(price - minimum_price, maximum_profit)
        minimum_price = min(price, minimum_price)
    return maximum_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
