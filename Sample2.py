# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:22:38 2021

@author: SushiMahi
"""

from bitcoin import *



pub1 = privtopub(random_key())

pub2 = privtopub(random_key())

pub3 = privtopub(random_key())


print("public Key 1 " , pub1)

print("public Key 1 " , pub2)

print("public Key 1 " , pub3)


multi = mk_multisig_script(pub1, pub2, pub3, 2, 3)

print("Multi Key : ", multi)


print("Address of : ", scriptaddr(multi) )