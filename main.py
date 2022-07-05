from func import *
from math import floor

coin_list = ['ADA', 'SOL', 'SAND', 'XRP']
coin_balance = {}
coin_price = {}
coin_ma_ratio = {}
balance_EURO = get_balance('EUR')
print('--------------------')
# balances, prices and MA's
for each in coin_list:
	coin_balance[each] = get_balance(each)
	coin_price[each] = get_price(each)
	coin_ma_ratio[each] = moving_averages_ratio(each, 6, 18, '1h')


# determine amount to invest in
count = 0
if balance_EURO > 10:
	for each in coin_list:
		if (coin_balance[each] == 0) & (coin_ma_ratio[each] > 1):
			count += 1
try:
	spend = balance_EURO / count
	print(f'Divide {balance_EURO} by: {count} makes: €{spend}', end="\n--------------------\n")
except Exception as e:
	print(e)
	spend = 0
	print(f'{balance_EURO} cannot be divided by {count}. Spending is €{spend}', end="\n--------------------\n")


# LOG items: Action, Pair, Amount, Error, datetime
for each in coin_list:
	if (coin_ma_ratio[each] >= 1) & (coin_balance[each] == 0) & (spend != 0):
		print(trade_market_order(each, 'buy', spend, coin_price[each]))
	elif (coin_ma_ratio[each] < 1) & (coin_balance[each] > 0):
		print(trade_market_order(each, 'sell', coin_balance[each], coin_price[each]))
	else:
		log(f'Do nothing,{each}-EUR,0,{coin_price[each]},none', 'log')
		print(f'{each}: Do nothing')
