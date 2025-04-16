def maximum_toys(prices, k):
    toys = 0
    for i in sorted(prices):
        if k > i:
            toys += 1
            k = k - i
    return toys


if __name__ == "__main__":
    toy_prices = [1, 12, 5, 111, 200, 1000, 10]
    budget = 50

    res = maximum_toys(toy_prices, budget)
    print(res)
