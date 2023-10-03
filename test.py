class Lamp:
    MIN_HEIGHT = 1

    #constructor
    def __init__(self):
        self.__color = "NOT GIVEN"
        self.height = self.MIN_HEIGHT
        self.isBulbOn = False
        self.isPluggedIn = False

    #parametrized conductor     
    def __init__(self, color, height, bulbOn, pluggedIn):
        self.__color = color
        self._height = height
        self._isBulbOn = bulbOn
        self._isPluggedIn = pluggedIn
    

    #a method for displaying the state of the object
    def show(self):
        print(self.__color, self.height, self.isBulbOn, self.isPluggedIn)

    def toggle_on_off(self):
        if self.is_bulb_on: 
            self.is_bulb_on = False
            message = "The lamp is now off"
        else:
            self.is_bulb_on = True
            message = "The lamp is now on"
        return message 

    
#===========MAIN PROGRAM===========
if __name__ == "__main__":
    #Create an Object
    deskLamp = Lamp("green", 24, False, True)
    #display the state of my deskLamp object 
    #deskLamp.show()


    #create another object 
    kitchenLamp = Lamp("pink", 32, False, True)
    #print(kitchenLamp.__color)
    #print(kitchenLamp._Lamp__color)
    kitchenLamp.__color = "Blue"
    kitchenLamp.height = 5
    kitchenLamp.isPluggedIn = True

    kitchenLamp.show()
     #you can create instance variables through the object 
    kitchenLamp.shadeColor = "black"
    print(kitchenLamp.shadeColor)
    #print(deskLamp.shadeColor)
    print(deskLamp.__dict__)
    print(kitchenLamp.__dict__)

    print(Lamp.__dict__)

    #access a class variable through the class
    print(Lamp.MIN_HEIGHT)
    print(kitchenLamp.MIN_HEIGHT)

    
if __name__ == "__main__":
    print(Lamp.__doc__)

    kitchenLamp = Lamp()
    kitchenLamp.show()
    print(kitchenLamp.toggle_on_off)