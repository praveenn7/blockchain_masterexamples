from bitcoin import *

priv = random_key()

print("Private Key : ", priv)




pub = privtopub(priv)

print("Public Key : ", pub)



addr = pubtoaddr(pub)
print("Address : " + addr)
