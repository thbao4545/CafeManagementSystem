class Item:
    
    def __init__(self, name: str, price: float, is_available: bool, selling_time: str):
        self.__name = name
        self.__price = price
        self.__is_available = is_available
        self.__selling_time = selling_time
        
    
    def print_infor(self):
        print(self.__name)
        print(self.__price)
        print(self.__is_available)
        print(self.__selling_time)   
        
a = Item("a", 1.2, True, "all day")
