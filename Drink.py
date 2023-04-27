from Item import Item
# from Session import *
class Drink(Item):
    
    def __init__(self, name: str, price: float, isAvailable: bool, sellingTime: str, shortDes:str, hasIce: bool):
        super().__init__(name, price, isAvailable, sellingTime,shortDes)
        self.__hasIce = hasIce    
    
    def set_has_ice(self, hasIce: bool):
        self.__hasIce = hasIce
        
    def get_has_ice(self):
        return self.__hasIce
    
    def print_infor(self):
        super().print_infor()
        print(self.__hasIce)

#Please remove comments to check        
#Example test program
# drink1= Drink("Coca",10000,True,"sang","Thuc uong co ga",True)
# drink1.print_infor()        

