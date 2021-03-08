# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:03:46 2021

@author: SushiMahi
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os;

with open("aes.key", "wb") as file_out:
    key = get_random_bytes(16)
    file_out.write(key)

data = "Oracle text for "
iv = os.urandom(16)
cipher = AES.new(key, AES.MODE_CBC, iv)
cipher.encrypt(data)

    
    
print("Data is encrypted and stored in a file")