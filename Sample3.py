# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:33:25 2021

@author: SushiMahi
"""

from blockchain import blockexplorer

block = blockexplorer.get_block('000000000000000000043639a106ebd31d6b2c4d59d3ce50913e1d85f70ec956')


print("block fee :" , block.fee)


print("block size :" , block.size)


print("block Transactions :" , block.transactions)



