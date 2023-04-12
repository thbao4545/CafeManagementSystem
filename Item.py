class Item:
    
    def __init__(self, name: str, price: float, is_available: bool, selling_time: str):
        self.__name = name
        self.__price = price
        self.__is_available = is_available
        self.__selling_time = selling_time
        
    def set_name(self, name: str):
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def set_price(self, price: float):
        self.__price = price
    
    def get_price(self):
        return self.__price
    
    def set_available(self, is_available: bool):
        self.__is_available = is_available
        
    def get_available(self):
        return self.__is_available
    
    def set_selling_time(self, selling_time: str):
        self.__selling_time = selling_time

    def get_selling_time(self):
        return self.__selling_time
    
    def print_infor(self):
        print(self.__name)
        print(self.__price)
        print(self.__is_available)
        print(self.__selling_time)   
        

