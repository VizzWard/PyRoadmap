class node():
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None


    def __repr__(self):
        return self.data