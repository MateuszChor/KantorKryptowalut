import pickle
def load_wallet(wallet):

    try:
        with open(wallet, 'rb') as f:
            wallet = pickle.load(f)

        return wallet

    except FileNotFoundError:
        return None



def save_wallet(wallet, wallet_data):
    with open(wallet, 'wb') as f:
        pickle.dump(wallet_data, f)
