# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:55:08 2021

@author: SushiMahi
"""

from blockchain import statistics 

stats = statistics.get()

print("BitCoin trade volume : " , stats.trade_volume_btc)


print("BitCoin btc_mined : " , stats.btc_mined)


print("BitCoin estimated_btc_sent : " , stats.estimated_btc_sent)


print("BitCoin estimated_transaction_volume_usd : " , stats.estimated_transaction_volume_usd)


print("BitCoin market_price_usd : " , stats.market_price_usd)



print("BitCoin number_of_transactions : " , stats.number_of_transactions)


print("BitCoin total_fees_btc : " , stats.total_fees_btc)