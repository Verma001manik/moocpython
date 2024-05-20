class CheckList :
    def __init__(self,header,entries: list ) :
        self.header = header
        self.list = list

class Customer:
    def __init__(self, id: str, balance: float, discount: int):
        self.id = id
        self.balance = balance 
        self.discount = discount

class Cable:
    def __init__(self, model: str, length: float, max_speed : int, bidirectional: bool):
        self.model = model 
        self.length = length 
        self.max_speed = max_speed
        self.bidirectional = bidirectional
        