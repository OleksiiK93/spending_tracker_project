class Transaction:

    def __init__(self, merchant, tag, amount, timestamp, id = None):
        self.merchant = merchant
        self.tag = tag
        self.amount = amount
        self.timestamp = timestamp
        self.id = id