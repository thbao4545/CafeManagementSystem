class Item:
    
    def __init__(self, name: str, price: float, is_available: bool, selling_time: str):
        self.name = name
        self.price = price
        self.is_available = is_available
        self.selling_time = selling_time
        
    
    def print_infor(self):
        print(self.name)
        print(self.price)
        print(self.is_available)
        print(self.selling_time)   
        
a = Item("a", 1.2, True, "all day")
