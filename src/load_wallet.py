import pickle
def load_wallet(wallet):
    with open(wallet, 'rb') as f:
        wallet = pickle.load(f)

    return wallet

def save_wallet(wallet, wallet_data):
    with open(wallet, 'wb') as f:
        pickle.dump(wallet_data, f)
