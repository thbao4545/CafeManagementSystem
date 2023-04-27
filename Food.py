# from Session import *
from Item import Item

class Food(Item):
    
    def __init__(self, name: str, price: float, isAvailable: bool, sellingTime: str,shortDes:str,isVegetarian: bool):
        super().__init__(name, price, isAvailable, sellingTime, shortDes)
        self.__isVegetarian = isVegetarian    
    
    def set_isVegetarian(self, isVegetarian: bool):
        self.__isVegetarian = isVegetarian
        
    def get_isVegetarian(self):
        return self.__isVegetarian
    
    def print_infor(self):
        super().print_infor()
        print(self.__isVegetarian)

#Please remove comments to check        
#Example test program
# food1= Food("Mi xao",20000,True,"sang","Thuc an nhanh cho nguoi ban ron",False)
# food1.print_infor()