from copy import deepcopy
from Drink import Drink
from Food import Food

class Menu:
    
    def __init__(self, drinkNumber = 0, foodNumber = 0, drinkList = [], foodList = []):
    
        self.__drinkList = drinkList.copy()
        self.__foodList = foodList.copy()
        
        self.__drinkNumber = drinkNumber
        self.__foodNumber = foodNumber
    
    def get_drinkNumber(self):
        return self.__drinkNumber
        
    def get_foodNumber(self):
        return self.__foodNumber
    
    def get_drinkList(self):
        return self.__drinkList
    
    def get_foodList(self):
        return self.__foodList
    
    def add_drink(self, new_drink: Drink):
        self.__drinkList.append(new_drink)
        self.__drinkNumber += 1
    def add_drink(self, name: str, price: float):
        new_drink = Drink(name, price, True, "24/7","Thuc uong giai khat",True)
        self.__drinkList.append(new_drink)
        self.__drinkNumber += 1
  
    def add_food(self, new_food: Food):
        self.__foodList.append(new_food)
        self.__foodNumber += 1
    def add_food(self, name: str, price: float):
        new_food = Food(name, price, True, "24/7","Do an nhanh",True)
        self.__foodList.append(new_food)
        self.__foodNumber += 1    
        
    def get_drink_by_name(self, drinkName: str):
        result=[]
        for drink in self.__drinkList:
            if drinkName in drink.get_name():
                result.append(drink)
        return result
    
    def get_food_by_name(self, foodName: str):
        result=[]
        for food in self.__foodList:
            if foodName in food.get_name():
                result.append(food)
        return result
    
    def get_drink_by_price(self,minPrice:float,maxPrice:float):
        result=[]
        for drink in self.__drinkList:
            if drink.get_price()>=minPrice and drink.get_price()<maxPrice:
                result.append(drink)
        return result
    def get_food_by_price(self,minPrice:float,maxPrice:float):
        result=[]
        for food in self.__foodList:
            if food.get_price()>=minPrice and food.get_price()<maxPrice:
                result.append(food)
        return result
    
    def sortUP_drink_by_price(self):
        self.__drinkList=sorted(self.get_drinkList(), key=lambda drink: drink.get_price()) 
    def sortDOWN_drink_by_price(self):
        self.sortUP_drink_by_price()
        self.__drinkList.reverse()
        
    def sortUP_food_by_price(self):
        self.__foodList=sorted(self.get_foodList(), key=lambda food: food.get_price())
    def sortDOWN_food_by_price(self):
        self.sortUP_food_by_price()
        self.__foodList.reverse()
            
    def remove_drink(self, drink_name: str):
        for drink in self.__drinkList:
            if drink.get_name() == drink_name:
                self.__drinkList.remove(drink)
                self.__drinkNumber -= 1
                return True
        return False
    
    def remove_food(self, food_name: str):
        for food in self.__foodList:
            if food.get_name() == food_name:
                self.__foodList.remove(food)
                self.__foodNumber -= 1
                return True
        return False
    
#Please remove comments to check
#Example test program
thucDon=Menu()
thucDon.add_drink("Nuoc loc",5000)
thucDon.add_food("Mi xao",15000)
thucDon.add_drink("Coca",12000)
thucDon.add_drink("Nuoc chanh",7000)
thucDon.add_food("Mi trung",20000)
thucDon.add_food("Com",5000)

#Test sort
for food in thucDon.get_foodList():
    print(food.get_name(),food.get_price())

thucDon.sortUP_food_by_price()
print("===================Sau khi sap xep=============================")
for food in thucDon.get_foodList():
    print(food.get_name(),food.get_price())

