from copy import deepcopy
from Drink import Drink
from Food import Food

class Menu:
    
    def __init__(self, drink_number = 0, food_number = 0, drink_list = [], food_list = []):
    
        self.drink_list = drink_list.copy()
        self.food_list = food_list.copy()
        
        self.drink_number = drink_number
        self.food_number = food_number
    
    def get_drink_number(self):
        return self.drink_number
        
    def get_food_number(self):
        return self.food_number
    
    def get_drink_list(self):
        return self.drink_list
    
    def get_food_list(self):
        return self.food_list
    
    def add_drink(self, new_drink: Drink):
        self.drink_list.append(new_drink)
        self.drink_number += 1
        
    def add_food(self, new_food: Food):
        self.food_list.append(new_food)
        self.food_number += 1
        
    def get_drink_by_name(self, drink_name: str):
        for drink in self.drink_list:
            if drink.name == drink_name:
                return drink
                break
        return None
    
    def get_food_by_name(self, food_name: str):
        for food in self.food_list:
            if food.name == food_name:
                return food
                break
        return None
    
    def get_drink_by_price(self):
        pass
    
    def get_food_by_price(self):
        pass
    
    def sort_drink_by_price(self):
        pass 
    
    def sort_food_by_price(self):
        pass
       
# Testing    
soda = Drink("soda", 10, True, "all day", False)
coke = Drink("coke", 10, True, "morning", True)

menu1 = Menu()
menu1.add_drink(soda)
menu1.add_drink(coke)



menu2 = Menu(2, 0, menu1.drink_list, [])

for drink in menu2.drink_list:
    drink.print_infor()
    print("------------------------")



