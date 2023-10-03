class Lamp:
    #Class Variables
    MIN_HEIGHT = 1
    Max_HEIGHT = 10
    number_object_created = 0

    #constructor
    def __init__(self):
        self._color = "NOT GIVEN"
        self._height = self.MIN_HEIGHT #you can also access through Lamp.MIN_HEIGHT
        self._is_bulb_on = False
        self._is_plugged_in = False
        Lamp.number_object_created += 1 #if you want to seet the value of the class
        #variable you need to use the class name and npt the object name!
        #if you use self instead of Lamp above it would create a new data memeber
        #and thos is not what we want 

    def __init__(self, color = "NOT GIVEN", height = MIN_HEIGHT, bulb_on = False, plugged_in = False):
        self._color = color
        self._height = height
        self._is_bulb_on = bulb_on
        self._is_plugged_in = plugged_in

#Mutator Methots (setters)
    def set_color(self, color):
        self._color = color

    
def set_height(self, height):
    if height >= self.MIN_HEIGHT and height <= self.MAX_HEIGHT:
        self._height = height
    elif height > self.MAX_HEIGHT:
        self.height = self.MAX_HEIGHT
    else:
        self._height = self.MIN_HEIGHT

def set_is_bulb_on(self, is_bulb_on):
    self._is_bulb_on = is_bulb_on

def set_is_plugged_in(self, is_plugged_in):
    self._is_plugged_in = is_plugged_in

#Acessor Methods (getter)
    def get_color(self):
        return self.color      
    
def get_height(self):
    return self.height

def get_is_bulb_on(self):
    return self._is_bulb_on

def get_is_plugged_in(self):
    return self._is_bulb_on


    #a method for displaying the state of the object
    def show(self):
        print(self.get_color, self.get_height, self.get_is_bulb_on, self.get_is_plugged_in)

    def toggle_on_off(self):
        if self._is_bulb_on: 
            self._is_bulb_on = False
            message = "The lamp is now off"
        else: 
            self._is_bulb_on = True
            message = "The lamp is now on"
        return message


#===========MAIN PROGRAM===========
if __name__ == "__main__":
    #print(Lamp.__doc__)

    print("Number of objectes created: ", Lamp.number_object_created)
    kitchen_lamp = Lamp("Blue", 9, True, True)
    kitchen_lamp.show()

    print(kitchen_lamp.toggle_on_off())
    print(kitchen_lamp.toggle_on_off())
    print(kitchen_lamp.toggle_on_off())
    print("Number of objectes created: ", kitchen_lamp.number_object_created)

    #print(kitchen_lamp.__dict__)
    #print(Lamp.__dict__)
    #The following statement creates an instance variable for kitchen_lamp
    #and does NOT update the class vaiable
    #kitchen_lamp.number_objects_created +=1

    #print(kitchen_lamp.__dict__)
    #print(Lamp.__dict__)

    #There are multiple ways to create your objects
    #bedroom_lamp = Lamp()
    #bedroom_lamp = ("Blue", 8)
    bedroom_lamp = Lamp(bulb_on=True, color="Red")
    bedroom_lamp.show()
    bedroom_lamp.set_height(19)
    bedroom_lamp.show()






