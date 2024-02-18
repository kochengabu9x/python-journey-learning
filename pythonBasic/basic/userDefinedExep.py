class ExCoffeCold(Exception) :
    def __init__ (self , arg):
        self.msg = arg

class ExCoffeeHot(Exception):
    def __init__ (self, arg):
        self.msg = arg
        

class Coffee:
    def __init__ (self, temperature):
        self.__temperature = temperature
        
    def drink_coffee(self):
        if self.__temperature > 85 :
            raise ExCoffeeHot("tea too hot")
        elif self.__temperature < 65:
            raise ExCoffeCold("tea too cold")
        else :
            print("perfect temperature")


cup = Coffee(100)

cup.drink_coffee()