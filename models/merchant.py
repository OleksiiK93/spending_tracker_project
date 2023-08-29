class Merchant:

    def __init__(self, name, deactivated = None, id = None):
        self.name = name
        self.deactivated = deactivated
        self.id = id

    def deactivate(self):
        self.deactivated = True