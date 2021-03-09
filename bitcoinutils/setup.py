
NETWORK = None

networks = {'mainnet', 'testnet', 'regtest'}

def setup(network='mainnet'):
    global NETWORK
    NETWORK = network
    return NETWORK


def get_network():
    global NETWORK
    return NETWORK


def is_mainnet():
    global NETWORK
    if NETWORK == 'mainnet':
        return True
    else:
        return False

def is_testnet():
    global NETWORK
    if NETWORK == 'testnet':
        return True
    else:
        return False

def is_regtest():
    global NETWORK
    if NETWORK == 'regtest':
        return True
    else:
        return False
