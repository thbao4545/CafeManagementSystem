from Item import Item

class Drink(Item):
    
    def __init__(self, name: str, price: float, is_available: bool, selling_time: str, has_ice: bool):
        
        super().__init__(name, price, is_available, selling_time)
        self.__has_ice = has_ice    
    
    def print_infor(self):
        super().print_infor()
        print(self.__has_ice)
        

