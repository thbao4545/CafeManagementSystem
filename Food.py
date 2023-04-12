from Item import Item

class Food(Item):
    
    def __init__(self, name: str, price: float, is_available: bool, selling_time: str, is_vegetarian: bool):
        
        super().__init__(name, price, is_available, selling_time)
        self.__is_vegetarian = is_vegetarian    
    
    def set_is_vegetarian(self, is_vegetarian: bool):
        self.__is_vegetarian = is_vegetarian
        
    def get_is_vegetarian(self):
        return self.__is_vegetarian
    
    def print_infor(self):
        super().print_infor()
        print(self.__is_vegetarian)