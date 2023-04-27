#from Session import * 
class Item:
    
    def __init__(self, name: str, price: float, isAvailable: bool, sellingTime: str, shortDes: str):
        self.__name = name
        self.__price = price
        self.__isAvailable = isAvailable
        self.__sellingTime = sellingTime
        self.__shortDes=shortDes
        
    def set_name(self, name: str):
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def set_price(self, price: float):
        self.__price = price
    
    def get_price(self):
        return self.__price
    
    def set_available(self, isAvailable: bool):
        self.__isAvailable = isAvailable
        
    def get_available(self):
        return self.__isAvailable
    
    def set_selling_time(self, sellingTime: str):
        self.__sellingTime = sellingTime

    def get_selling_time(self):
        return self.__sellingTime
    
    def set_short_description(self, shortDes: str):
        self.__shortDes=shortDes
    
    def get_short_description(self):
        return self.__shortDes
        
    def print_infor(self):
        print(self.__name)
        print(self.__price)
        print(self.__isAvailable)
        print(self.__sellingTime)   
        print(self.__shortDes)

#Please remove comments to check
#Example test program
# item1= Item("Mi xao",20000,True,"sang","Thuc an nhanh cho nguoi ban ron")
# item1.print_infor()