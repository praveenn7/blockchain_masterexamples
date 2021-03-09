from bitcoinutils.setup import setup
from bitcoinutils.keys import P2pkhAddress, PrivateKey, PublicKey

def main() :
    setup('mainnet')

    priv = PrivateKey(secret_exponent= 1)
    
    print("step 1")

    print("Private Key ", priv.to_wif(compressed=True))


    
    print("step 2")
    
    pub = priv.get_public_key()
    
    print("Public key object :" , pub)
    
    print("Public Key :" , pub.to_hex(compressed=True) )
    
    
    
    address = pub.get_address()
    
    print("Address : " , address.to_string())
    
    print("Address Hash160: " , address.to_hash160())
    
    
    
    message = "Oracle Test Message via blockchain"
    
    
    signature = priv.sign_message(message)
    
    print ("The message to sign " , message )
    
    print("The signature is  : ", signature)
    
    
    
    if PublicKey.verify_message(address.to_string(), signature, message) :
        print(" The signature is valid")
    else :
        print("The signature is not valid")
    

if __name__ == "__main__" :
    main()