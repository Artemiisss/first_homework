""" Exersice 1 """
coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')
match = {}
for index, value in enumerate(coin):
    match[value] = code[index]
print(match)
