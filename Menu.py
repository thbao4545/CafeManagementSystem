from copy import deepcopy
from Drink import Drink
from Food import Food

class Menu:
    
    def __init__(self, drink_number = 0, food_number = 0, drink_list = [], food_list = []):
    
        self.__drink_list = drink_list.copy()
        self.__food_list = food_list.copy()
        
        self.__drink_number = drink_number
        self.__food_number = food_number
    
    def get_drink_number(self):
        return self.__drink_number
        
    def get_food_number(self):
        return self.__food_number
    
    def get_drink_list(self):
        return self.__drink_list
    
    def get_food_list(self):
        return self.__food_list
    
    def add_drink(self, new_drink: Drink):
        self.__drink_list.append(new_drink)
        self.__drink_number += 1
    def add_drink2(self, name: str, price: float):
        new_drink = Drink(name, price, True, "24/7", True)
        self.__drink_list.append(new_drink)
        self.__drink_number += 1
  
    def add_food(self, new_food: Food):
        self.__food_list.append(new_food)
        self.__food_number += 1
    def add_food2(self, name: str, price: float):
        new_food = Drink(name, price, True, "24/7", True)
        self.__food_list.append(new_food)
        self.__food_number += 1    
    def get_drink_by_name(self, drink_name: str):
        for drink in self.drink_list:
            if drink.__name == drink_name:
                return drink
                break
        return None
    
    def get_food_by_name(self, food_name: str):
        for food in self.__food_list:
            if food.__name == food_name:
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
    def remove_drink(self, drink_name: str):
        for drink in self.__drink_list:
            if drink.get_name() == drink_name:
                self.__drink_list.remove(drink)
                self.__drink_number -= 1
                break
    
    def remove_food(self, food_name: str):
        for food in self.__food_list:
            if food.get_name() == food_name:
                self.__food_list.remove(food)
                self.__food_number -= 1
                break


