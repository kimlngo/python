blockchain = []


def get_last_blockchain_value():
    """Get the last value in the block chain"""
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_amount():
    """Get the transaction amount"""
    return float(input("Your transaction amount: " ))

#input function
txn_amt = get_transaction_amount()
add_value(txn_amt)

txn_amt = get_transaction_amount()
add_value(txn_amt, get_last_blockchain_value())

txn_amt = get_transaction_amount()
add_value(txn_amt, get_last_blockchain_value())

print(blockchain)


