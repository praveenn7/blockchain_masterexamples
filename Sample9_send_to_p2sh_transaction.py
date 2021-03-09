# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:27:00 2021

@author: SushiMahi
"""

import binascii
from bitcoinutils.utils import to_satoshis
from bitcoinutils.setup import setup
from bitcoinutils.transactions import Transaction, TxInput, TxOutput, Sequence
from bitcoinutils.keys import P2pkhAddress, P2shAddress, PrivateKey
from bitcoinutils.script import Script
from bitcoinutils.constants import TYPE_RELATIVE_TIMELOCK


def main() :
    setup('testnet')
    
    txin = TxInput('76464c2b9e2af4d63ef38a77964b3b77e629dddefc5cb9eb1a3645b1608b790f', 0)
    
   
    
    from_addr = P2pkhAddress('n4bkvTyU1dVdzsrhWBqBw8fEMbHjJvtmJR')
    
    print("From Address  : " , from_addr)
    
    sk = PrivateKey('cTALNpTpRbbxTCJ2A5Vq88UxT44w1PE2cYqiB3n4hRvzyCev1Wwo')
    
    
    
    
    
    p2pk_sk = PrivateKey('cRvyLwCPLU88jsyj94L7iJjQX5C2f8koG4G2gevN4BeSGcEvfKe9')
    
    p2pk_pk = p2pk_sk.get_public_key().to_hex()
    
    
    
    
    redeem_script = Script([p2pk_pk, 'OP_CHECKSIG'])
    
    txout = TxOutput(to_satoshis(0.09), redeem_script.to_p2sh_script_pub_key())
    
   
    
    
    
    
    
    tx = Transaction([txin], [txout])
    
    print("Raw transaction" , tx.serialize())
    
    
    
    
    
    
    
    





if __name__ == "__main__" :
    main()