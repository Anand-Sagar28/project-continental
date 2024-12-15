# Write a oops program of camera displaying information about all the oops pillar

# lets create a camera class, ts subclass includes the different cameras brands, functionalities includes shutter speed and the filters

class Camera:
    def __init__(self, shutter_speed = 0, filters = 0):
        self.shutter_speed = shutter_speed
        self.filters = filters

    def pricing(self,price):
        return f"The price of the camera is - {self.price}"
    
    def __str__(self):
        return f"Welcome to camera class.Price is {self.price}"

class Nikon(Camera):
    def __init__(self,comp):
        super().__init__(shutter_speed= 4,filters= 4)
        self.comp = comp
    
    def pricing(self,price = 40000,overpriced = "True"):
        print( f"The price of the camera is - {price}")
        print(f"Overpriced = {overpriced}")
    
    def disp_info(self):
        print(f"the company of the camera is {self.comp}. Shutter speed = {self.shutter_speed}, Filters: {self.filters}")
        self.pricing()
    
    
class Kodak(Camera):
    def __init__(self,comp):
        super().__init__(shutter_speed=2,filters =1)
        self.comp = comp

    def pricing(self, price =  90000):
        return f"The price of the camera is : {price}"
    
    def disp_info(self):
        print(f"the company of the camera is {self.comp}. Its Shutter_speed : {self.shutter_speed}, filters = {self.filters}")
        self.pricing()


Cam1 = Nikon("Nikon")
Cam1.disp_info()
Cam2 = Kodak("KODAK")
Cam2.disp_info()